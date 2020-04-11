import os

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from analysis import utils as la
from files import utils as jsutils
from mainwindow import Ui_MainWindow
from scrapers import scrapers as scr


class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the MainController
        """
        super(MainController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_make_analysis.clicked.connect(la.pre_process_all_files)  # btn to tokenize all files
        self.df = pd.DataFrame(columns=['file', 'similarity'])
        self.df_compare = pd.DataFrame(columns=['file', 'similarity'])
        self.CATEGORIES = ['ciencia', 'salud', 'tecnologia']
        self.SOURCES = ['20Minutos', 'elMundo', 'elPais']
        self.selected_file = ""

        # analysis TAB
        self.ui.btn_search.clicked.connect(self.make_search)
        self.ui.table_search_rank.itemClicked.connect(self.write_article_rank)
        # todo remove
        self.ui.tf_search.setText(
            'El Gobierno calcula que España retornará a la vida normal, de forma escalonada, a partir del 26 de abril')

        # scrapers TAB
        self.ui.btn_scrapers_20m_run.clicked.connect(self.scraper_20m)
        self.ui.btn_scrapers_elPais_run.clicked.connect(self.scraper_elPais)
        self.ui.btn_scrapers_elMundo_run.clicked.connect(self.scraper_elMundo)
        self.ui.btn_scrapers_run_all.clicked.connect(self.scraper_run_all)
        self.ui.btn_scrapers_refresh_sta.clicked.connect(self.refresh)
        self.refresh()

        # compare TAB
        self.ui.cb_ref_source.currentIndexChanged.connect(self.select_sources)
        self.ui.cb_ref_cat.currentIndexChanged.connect(self.select_categories)
        self.ui.table_compare_ref_articles.itemClicked.connect(self.tab_compare_write_article)
        self.ui.table_compare_ref_rank.itemClicked.connect(self.write_article_ref_rank)
        self.ui.btn_ref_search.clicked.connect(self.compare_articles)

    def create_alert_window(self, title, content):
        QMessageBox.about(self, title, content)

    def get_categories(self, opt):
        categories = []
        if opt is 0:
            categories = self.CATEGORIES
        elif opt is 1:
            categories.append('salud')
        elif opt is 2:
            categories.append('ciencia')
        elif opt is 3:
            categories.append('tecnologia')
        return categories

    def get_sources(self, opt):
        sources = []
        if opt is 0:
            sources = self.SOURCES
        elif opt is 1:
            sources.append('20Minutos')
        elif opt is 2:
            sources.append('elMundo')
        elif opt is 3:
            sources.append('elPais')
        return sources

    def write_article(self, table, filepath):
        table.clear()
        js = jsutils.read_json(filepath)
        table.setText("<html><h3><b>" + str(js['title']) + "</b></h3></html>")
        table.append(
            "<html><h6><b>" + str(js['author']) + "</b> " + str(js['date']) + " " + str(js['time']) + "</h6></html>")
        table.append("<html><h6><b>" + str(js['subtitle']) + "</b></h6></html>")
        table.append("<html><p>" + str(js['content']) + "</p></html>")

    # # # # # # # # # # # # # # # # # # # # # # # # # # SEARCH TAB # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def write_article_rank(self, index):
        self.write_article(self.ui.tx_search_article_result, self.df['file'][index.row()])

    def set_ranking_table(self):
        rows = len(self.df)
        self.ui.table_search_rank.setRowCount(rows)
        self.ui.table_search_rank.setColumnCount(1)
        for row in range(rows):
            item = QTableWidgetItem(self.df['file'][row][7:-5] + '     -     SIMILARITY ' + str(
                round(self.df['similarity'][row] * 100, 2)) + '%')
            self.ui.table_search_rank.setItem(row, 0, item)
        self.create_alert_window("Finish", "The process has finished")

    def make_search(self):
        self.create_alert_window("Processing", "Please wait for the process to finish")
        top = self.ui.cb_top.currentIndex()
        filter = self.get_sources(self.ui.cb_filter.currentIndex())
        query = self.ui.tf_search.text()
        self.df = la.query_similarity(filter, self.CATEGORIES, la.total_idf(filter, self.CATEGORIES),
                                      la.get_query_tf_idf(query), top)
        self.set_ranking_table()

    # # # # # # # # # # # # # # # # # # # # # # # # # # SCRAPERS TAB # # # # # # # # # # # # # # # # # # # # # # # # # #
    def scraper_20m(self):
        scr.scraper_20minutos(self.get_categories(self.ui.cb_scrapers_20m.currentIndex()))
        self.refresh()

    def scraper_elMundo(self):
        scr.scraper_elMundo(self.get_categories(self.ui.cb_scrapers_elMundo.currentIndex()))
        self.refresh()

    def scraper_elPais(self):
        scr.scraper_elPais(self.get_categories(self.ui.cb_scrapers_elPais.currentIndex()))
        self.refresh()

    def scraper_run_all(self):
        self.scraper_20m()
        self.scraper_elMundo()
        self.scraper_elPais()

    def refresh(self):
        self.ui.lbl_scrapers_20m_health_result.setNum(jsutils.count_files('20Minutos', 'salud'))
        self.ui.lbl_scrapers_20m_science_result.setNum(jsutils.count_files('20Minutos', 'ciencia'))
        self.ui.lbl_scrapers_20m_tech_result.setNum(jsutils.count_files('20Minutos', 'tecnologia'))
        self.ui.lbl_scrapers_20m_total_result.setNum(
            int(self.ui.lbl_scrapers_20m_health_result.text()) +
            int(self.ui.lbl_scrapers_20m_science_result.text()) +
            int(self.ui.lbl_scrapers_20m_tech_result.text()))

        self.ui.lbl_scrapers_elMundo_health_result.setNum(jsutils.count_files('elMundo', 'salud'))
        self.ui.lbl_scrapers_elMundo_science_result.setNum(jsutils.count_files('elMundo', 'ciencia'))
        self.ui.lbl_scrapers_elMundo_tech_result.setNum(jsutils.count_files('elMundo', 'tecnologia'))
        self.ui.lbl_scrapers_elMundo_total_result.setNum(
            int(self.ui.lbl_scrapers_elMundo_health_result.text()) +
            int(self.ui.lbl_scrapers_elMundo_science_result.text()) +
            int(self.ui.lbl_scrapers_elMundo_tech_result.text()))

        self.ui.lbl_scrapers_elPais_health_result.setNum(jsutils.count_files('elPais', 'salud'))
        self.ui.lbl_scrapers_elPais_science_result.setNum(jsutils.count_files('elPais', 'ciencia'))
        self.ui.lbl_scrapers_elPais_tech_result.setNum(jsutils.count_files('elPais', 'tecnologia'))
        self.ui.lbl_scrapers_elPais_total_result.setNum(
            int(self.ui.lbl_scrapers_elPais_health_result.text()) +
            int(self.ui.lbl_scrapers_elPais_science_result.text()) +
            int(self.ui.lbl_scrapers_elPais_tech_result.text()))

    # # # # # # # # # # # # # # # # # # # # # # # # # # COMPARE TAB # # # # # # # # # # # # # # # # # # # # # # # # # #
    def select_sources(self, index):
        sources = self.get_sources(self.ui.cb_ref_source.currentIndex())

        self.ui.table_compare_ref_articles.setRowCount(0)
        self.ui.table_compare_ref_articles.setColumnCount(1)
        self.ui.table_compare_ref_articles.clear()
        row = 0
        for source in sources:
            for category in self.CATEGORIES:
                path = './data/' + source + '/' + category + '/'
                for file in os.listdir(path):
                    filepath = path + file
                    self.ui.table_compare_ref_articles.setRowCount(self.ui.table_compare_ref_articles.rowCount() + 1)
                    item = QTableWidgetItem(filepath[7:-5])
                    self.ui.table_compare_ref_articles.setItem(row, 0, item)
                    row += 1

    def select_categories(self, index):
        sources = self.get_sources(self.ui.cb_ref_source.currentIndex())
        categories = self.get_categories(self.ui.cb_ref_source.currentIndex())

        self.ui.table_compare_ref_articles.setRowCount(0)
        self.ui.table_compare_ref_articles.setColumnCount(1)
        self.ui.table_compare_ref_articles.clear()
        row = 0
        for source in sources:
            for category in categories:
                path = './data/' + source + '/' + category + '/'
                for file in os.listdir(path):
                    filepath = path + file
                    self.ui.table_compare_ref_articles.setRowCount(self.ui.table_compare_ref_articles.rowCount() + 1)
                    item = QTableWidgetItem(filepath[7:-5])
                    self.ui.table_compare_ref_articles.setItem(row, 0, item)
                    row += 1

    def tab_compare_write_article(self, index):
        self.selected_file = './data/' + str(self.ui.table_compare_ref_articles.currentItem().text()) + '.json'
        self.write_article(self.ui.tx_compare_preview, self.selected_file)

    def set_results_ranking_table(self):
        rows = len(self.df_compare)
        self.ui.table_compare_ref_rank.setRowCount(rows)
        self.ui.table_compare_ref_rank.setColumnCount(1)
        for row in range(rows):
            item = QTableWidgetItem(self.df_compare['file'][row][7:-5] + '     -     SIMILARITY ' + str(
                round(self.df_compare['similarity'][row] * 100, 2)) + '%')
            self.ui.table_compare_ref_rank.setItem(row, 0, item)
        self.create_alert_window("Finish", "The process has finished")

    def compare_articles(self):
        self.create_alert_window("Processing", "Please wait for the process to finish")
        sources = self.get_sources(self.ui.cb_res_source.currentIndex())
        top = self.ui.cb_res_top.currentIndex()

        query = jsutils.read_json(self.selected_file)['content']
        self.df_compare = la.query_similarity(sources, self.CATEGORIES, la.total_idf(sources, self.CATEGORIES),
                                              la.get_query_tf_idf(query), top)
        self.set_results_ranking_table()

    def write_article_ref_rank(self, index):
        self.write_article(self.ui.tx_search_article_result, self.df_compare['file'][index.row()])


def run():
    """
    Runs the main window
    """
    app = QtWidgets.QApplication([])
    application = MainController()
    application.show()
    app.exec()
