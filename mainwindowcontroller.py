# -*- encoding: utf-8 -*-

import os

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from analysis import utils as la
from files import utils as jsutils
from mainwindow import Ui_MainWindow
from scrapers import scrapers as scr
from recommendations import utils as recom


class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        """
        Initialize the MainController
        """
        super(MainController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.df_search = pd.DataFrame(columns=['file', 'similarity'])
        self.df_compare = pd.DataFrame(columns=['file', 'similarity'])
        self.df_recom = pd.DataFrame(columns=['filepath', 'tags', 'similarity'])
        self.CATEGORIES = ['ciencia', 'salud', 'tecnologia']
        self.SOURCES = ['20Minutos', 'elMundo', 'elPais']
        self.selected_file = ""
        self.pre_process_all_files()

        # analysis TAB
        self.ui.btn_search.clicked.connect(self.tab_search_results)
        self.ui.table_search_rank.itemClicked.connect(self.write_article_rank)

        # scrapers TAB
        self.ui.btn_scrapers_20m_run.clicked.connect(self.scraper_20m)
        self.ui.btn_scrapers_elPais_run.clicked.connect(self.scraper_elPais)
        self.ui.btn_scrapers_elMundo_run.clicked.connect(self.scraper_elMundo)
        self.ui.btn_scrapers_run_all.clicked.connect(self.scraper_run_all)
        self.ui.btn_scrapers_refresh_sta.clicked.connect(self.refresh)
        self.ui.btn_make_analysis.clicked.connect(self.pre_process_all_files)  # btn to tokenize all files
        self.refresh()

        # compare TAB
        self.ui.cb_ref_source.currentIndexChanged.connect(self.select_sources_compare)
        self.ui.cb_ref_cat.currentIndexChanged.connect(self.select_categories_compare)
        self.ui.table_compare_ref_articles.itemClicked.connect(self.tab_compare_write_article)
        self.ui.table_compare_ref_rank.itemClicked.connect(self.write_article_ref_rank)
        self.ui.btn_ref_search.clicked.connect(self.tab_compare_results)
        self.select_categories_compare(0)

        # recommendations TAB
        self.ui.cb_reco_ref_source.currentIndexChanged.connect(self.select_sources_reco)
        self.ui.cb_reco_ref_cat.currentIndexChanged.connect(self.select_categories_reco)
        self.ui.table_reco_ref_articles.itemClicked.connect(self.tab_reco_write_article)
        self.ui.table_reco_ref_rank.itemClicked.connect(self.write_article_reco_rank)
        self.select_categories_reco(0)

    def create_alert_window(self, title, content):
        QMessageBox.about(self, title, content)

    def get_categories(self, opt):
        categories = []
        if opt == 0:
            categories = self.CATEGORIES
        elif opt == 1:
            categories.append('salud')
        elif opt == 2:
            categories.append('ciencia')
        elif opt == 3:
            categories.append('tecnologia')
        return categories

    def get_sources(self, opt):
        sources = []
        if opt == 0:
            sources = self.SOURCES
        elif opt == 1:
            sources.append('20Minutos')
        elif opt == 2:
            sources.append('elMundo')
        elif opt == 3:
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
        table.append("<html><b>TAGS: </b>" + "".join([str(x) + ', ' for x in js['tags']]) + "</p></html>")

    # # # # # # # # # # # # # # # # # # # # # # # # # # SEARCH TAB # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def write_article_rank(self, index):
        self.write_article(self.ui.tx_search_article_result, self.df_search['file'][index.row()])

    def make_analysis(self, df, table, sources, categories, query, top):
        self.create_alert_window("Processing", "Please wait for the process to finish")
        df = la.query_similarity(sources=sources,
                                 categories=categories,
                                 total_idf=la.total_idf(sources, categories, query),
                                 query_tf=la.get_query_tf(query),
                                 top=top)
        rows = len(df)
        table.setRowCount(rows)
        table.setColumnCount(1)
        for row in range(rows):
            item = QTableWidgetItem(
                df['file'][row][7:-5] + '     -     SIMILARITY ' + str(round(df['similarity'][row] * 100, 2)) + '%')
            table.setItem(row, 0, item)
        self.create_alert_window("Finish", "The process has finished")
        return df

    def tab_search_results(self):
        self.df_search = self.make_analysis(df=self.df_search,
                                            table=self.ui.table_search_rank,
                                            sources=self.get_sources(self.ui.cb_filter.currentIndex()),
                                            categories=self.CATEGORIES,
                                            query=self.ui.tf_search.text(),
                                            top=self.ui.cb_top.currentIndex())

    # # # # # # # # # # # # # # # # # # # # # # # # # # SCRAPERS TAB # # # # # # # # # # # # # # # # # # # # # # # # # #
    def scraper_20m(self):
        scr.scraper_20minutos(self.get_categories(self.ui.cb_scrapers_20m.currentIndex()))
        self.pre_process_all_files()
        self.refresh()

    def scraper_elMundo(self):
        scr.scraper_elMundo(self.get_categories(self.ui.cb_scrapers_elMundo.currentIndex()))
        self.pre_process_all_files()
        self.refresh()

    def scraper_elPais(self):
        scr.scraper_elPais(self.get_categories(self.ui.cb_scrapers_elPais.currentIndex()))
        self.pre_process_all_files()
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

    def pre_process_all_files(self):
        la.pre_process_all_files()

    # # # # # # # # # # # # # # # # # # # # # # # # # # COMPARE TAB # # # # # # # # # # # # # # # # # # # # # # # # # #
    def select_sources_compare(self, index):
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

    def select_categories_compare(self, index):
        sources = self.get_sources(self.ui.cb_ref_source.currentIndex())
        categories = self.get_categories(self.ui.cb_ref_cat.currentIndex())

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

    def tab_compare_results(self):
        self.df_compare = self.make_analysis(df=self.df_compare,
                                             table=self.ui.table_compare_ref_rank,
                                             sources=self.get_sources(self.ui.cb_res_source.currentIndex()),
                                             categories=self.CATEGORIES,
                                             query=jsutils.read_json(self.selected_file)['content'],
                                             top=self.ui.cb_res_top.currentIndex())

    def write_article_ref_rank(self, index):
        self.write_article(self.ui.tx_compare_article, self.df_compare['file'][index.row()])

    # # # # # # # # # # # # # # # # # # # # # # # # # # RECO TAB # # # # # # # # # # # # # # # # # # # # # # # # # #
    def select_sources_reco(self, index):
        sources = self.get_sources(self.ui.cb_reco_ref_source.currentIndex())

        self.ui.table_reco_ref_articles.setRowCount(0)
        self.ui.table_reco_ref_articles.setColumnCount(1)
        self.ui.table_reco_ref_articles.clear()
        row = 0
        for source in sources:
            for category in self.CATEGORIES:
                path = './data/' + source + '/' + category + '/'
                for file in os.listdir(path):
                    filepath = path + file
                    self.ui.table_reco_ref_articles.setRowCount(self.ui.table_reco_ref_articles.rowCount() + 1)
                    item = QTableWidgetItem(filepath[7:-5])
                    self.ui.table_reco_ref_articles.setItem(row, 0, item)
                    row += 1

    def select_categories_reco(self, index):
        sources = self.get_sources(self.ui.cb_reco_ref_source.currentIndex())
        categories = self.get_categories(self.ui.cb_reco_ref_cat.currentIndex())

        self.ui.table_reco_ref_articles.setRowCount(0)
        self.ui.table_reco_ref_articles.setColumnCount(1)
        self.ui.table_reco_ref_articles.clear()
        row = 0
        for source in sources:
            for category in categories:
                path = './data/' + source + '/' + category + '/'
                for file in os.listdir(path):
                    filepath = path + file
                    self.ui.table_reco_ref_articles.setRowCount(self.ui.table_reco_ref_articles.rowCount() + 1)
                    item = QTableWidgetItem(filepath[7:-5])
                    self.ui.table_reco_ref_articles.setItem(row, 0, item)
                    row += 1

    def tab_reco_write_article(self, index):
        self.selected_file = './data/' + str(self.ui.table_reco_ref_articles.currentItem().text()) + '.json'
        self.write_article(self.ui.tx_reco_preview, self.selected_file)

        self.df_recom = recom.all_sim(self.selected_file, self.SOURCES, self.CATEGORIES)
        rows = len(self.df_recom)
        self.ui.table_reco_ref_rank.setRowCount(rows)
        self.ui.table_reco_ref_rank.setColumnCount(1)
        for row in range(rows):
            item = QTableWidgetItem(str(round(self.df_recom['similarity'][row] * 100, 2)) + ' % - ' + self.df_recom['tags'][row])
            self.ui.table_reco_ref_rank.setItem(row, 0, item)

    def write_article_reco_rank(self, index):
        self.write_article(self.ui.tx_reco_article, self.df_recom['file'][index.row()])


def run():
    """
    Runs the main window
    """
    app = QtWidgets.QApplication([])
    application = MainController()
    application.show()
    app.exec()
