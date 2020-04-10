from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from analysis import utils as la
from files import utils as jsonutils
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

        # analysis TAB
        self.ui.btn_search.clicked.connect(self.make_search)
        # self.ui.table_search_rank.itemClicked.connect()  # todo

        # scrapers TAB
        self.ui.btn_scrapers_20m_run.clicked.connect(self.scraper_20m)
        self.ui.btn_scrapers_elPais_run.clicked.connect(self.scraper_elPais)
        self.ui.btn_scrapers_elMundo_run.clicked.connect(self.scraper_elMundo)
        self.ui.btn_scrapers_run_all.clicked.connect(self.scraper_run_all)
        self.ui.btn_scrapers_refresh_sta.clicked.connect(self.refresh)
        self.refresh()

    def get_categories(self, opt):
        categories = []
        if opt is 0:
            categories.append('salud')
            categories.append('ciencia')
            categories.append('tecnologia')
        elif opt is 1:
            categories.append('salud')
        elif opt is 2:
            categories.append('ciencia')
        elif opt is 3:
            categories.append('tecnologia')
        return categories

    def get_sources(self, opt):
        categories = []
        if opt is 0:
            categories.append('20Minutos')
            categories.append('elMundo')
            categories.append('elPais')
        elif opt is 1:
            categories.append('20Minutos')
        elif opt is 2:
            categories.append('elMundo')
        elif opt is 3:
            categories.append('elPais')
        return categories

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
        self.ui.lbl_scrapers_20m_health_result.setNum(jsonutils.count_files('20Minutos', 'salud'))
        self.ui.lbl_scrapers_20m_science_result.setNum(jsonutils.count_files('20Minutos', 'ciencia'))
        self.ui.lbl_scrapers_20m_tech_result.setNum(jsonutils.count_files('20Minutos', 'tecnologia'))
        self.ui.lbl_scrapers_20m_total_result.setNum(
            int(self.ui.lbl_scrapers_20m_health_result.text()) +
            int(self.ui.lbl_scrapers_20m_science_result.text()) +
            int(self.ui.lbl_scrapers_20m_tech_result.text()))

        self.ui.lbl_scrapers_elMundo_health_result.setNum(jsonutils.count_files('elMundo', 'salud'))
        self.ui.lbl_scrapers_elMundo_science_result.setNum(jsonutils.count_files('elMundo', 'ciencia'))
        self.ui.lbl_scrapers_elMundo_tech_result.setNum(jsonutils.count_files('elMundo', 'tecnologia'))
        self.ui.lbl_scrapers_elMundo_total_result.setNum(
            int(self.ui.lbl_scrapers_elMundo_health_result.text()) +
            int(self.ui.lbl_scrapers_elMundo_science_result.text()) +
            int(self.ui.lbl_scrapers_elMundo_tech_result.text()))

        self.ui.lbl_scrapers_elPais_health_result.setNum(jsonutils.count_files('elPais', 'salud'))
        self.ui.lbl_scrapers_elPais_science_result.setNum(jsonutils.count_files('elPais', 'ciencia'))
        self.ui.lbl_scrapers_elPais_tech_result.setNum(jsonutils.count_files('elPais', 'tecnologia'))
        self.ui.lbl_scrapers_elPais_total_result.setNum(
            int(self.ui.lbl_scrapers_elPais_health_result.text()) +
            int(self.ui.lbl_scrapers_elPais_science_result.text()) +
            int(self.ui.lbl_scrapers_elPais_tech_result.text()))

    def create_alert_window(self, title, content):
        QMessageBox.about(self, title, content)

    def make_search(self):
        self.create_alert_window("Processing", "Please wait for the process to finish")
        top = self.ui.cb_top.currentIndex()
        filter = self.get_sources(self.ui.cb_filter.currentIndex())
        query = self.ui.tf_search.text()
        categories = ['ciencia', 'salud', 'tecnologia']
        df = la.total_result_wm(filter, categories, la.total_idf(filter, categories), la.get_query_tf_idf(query), top)
        self.set_ranking_table(df)

    def set_ranking_table(self, df_results):
        rows = len(df_results)

        self.ui.table_search_rank.setRowCount(rows)
        self.ui.table_search_rank.setColumnCount(1)

        for row in range(rows):
            item = QTableWidgetItem(
                'ARTICLE' + str(row + 1) + '- SIMILARITY' + str(round(df_results['similarity'][row] * 100, 2)) + '%')
            item.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.ui.table_search_rank.setItem(row, 0, item)
        self.create_alert_window("Finish", "The process has finished")


def run():
    """
    Runs the main window
    """
    app = QtWidgets.QApplication([])
    application = MainController()
    application.show()
    app.exec()
