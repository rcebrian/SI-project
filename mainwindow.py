# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1221, 700)
        MainWindow.setMinimumSize(QtCore.QSize(910, 512))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_search = QtWidgets.QWidget()
        self.tab_search.setObjectName("tab_search")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_search)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gb_options = QtWidgets.QGroupBox(self.tab_search)
        self.gb_options.setMaximumSize(QtCore.QSize(16777215, 120))
        self.gb_options.setObjectName("gb_options")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.gb_options)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.GL_options = QtWidgets.QGridLayout()
        self.GL_options.setObjectName("GL_options")
        self.HL_search = QtWidgets.QHBoxLayout()
        self.HL_search.setObjectName("HL_search")
        self.lbl_query = QtWidgets.QLabel(self.gb_options)
        self.lbl_query.setObjectName("lbl_query")
        self.HL_search.addWidget(self.lbl_query)
        self.tf_search = QtWidgets.QLineEdit(self.gb_options)
        self.tf_search.setObjectName("tf_search")
        self.HL_search.addWidget(self.tf_search)
        self.btn_search = QtWidgets.QPushButton(self.gb_options)
        self.btn_search.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_search.setObjectName("btn_search")
        self.HL_search.addWidget(self.btn_search)
        self.GL_options.addLayout(self.HL_search, 1, 0, 1, 1)
        self.HL_opt = QtWidgets.QHBoxLayout()
        self.HL_opt.setObjectName("HL_opt")
        self.lbl_top = QtWidgets.QLabel(self.gb_options)
        self.lbl_top.setObjectName("lbl_top")
        self.HL_opt.addWidget(self.lbl_top)
        self.cb_top = QtWidgets.QComboBox(self.gb_options)
        self.cb_top.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_top.setObjectName("cb_top")
        self.cb_top.addItem("")
        self.cb_top.addItem("")
        self.cb_top.addItem("")
        self.cb_top.addItem("")
        self.cb_top.addItem("")
        self.cb_top.addItem("")
        self.HL_opt.addWidget(self.cb_top)
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.HL_opt.addItem(spacerItem)
        self.lbl_filter = QtWidgets.QLabel(self.gb_options)
        self.lbl_filter.setObjectName("lbl_filter")
        self.HL_opt.addWidget(self.lbl_filter)
        self.cb_filter = QtWidgets.QComboBox(self.gb_options)
        self.cb_filter.setMinimumSize(QtCore.QSize(150, 0))
        self.cb_filter.setObjectName("cb_filter")
        self.cb_filter.addItem("")
        self.cb_filter.addItem("")
        self.cb_filter.addItem("")
        self.cb_filter.addItem("")
        self.HL_opt.addWidget(self.cb_filter)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.HL_opt.addItem(spacerItem1)
        self.btn_make_analysis = QtWidgets.QPushButton(self.gb_options)
        self.btn_make_analysis.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_make_analysis.setObjectName("btn_make_analysis")
        self.HL_opt.addWidget(self.btn_make_analysis)
        self.GL_options.addLayout(self.HL_opt, 2, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.GL_options)
        self.verticalLayout_3.addWidget(self.gb_options)
        self.HL_bottom = QtWidgets.QHBoxLayout()
        self.HL_bottom.setObjectName("HL_bottom")
        self.gb_ranking = QtWidgets.QGroupBox(self.tab_search)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_ranking.sizePolicy().hasHeightForWidth())
        self.gb_ranking.setSizePolicy(sizePolicy)
        self.gb_ranking.setObjectName("gb_ranking")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gb_ranking)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_search_rank = QtWidgets.QTableWidget(self.gb_ranking)
        self.table_search_rank.setAlternatingRowColors(True)
        self.table_search_rank.setObjectName("table_search_rank")
        self.table_search_rank.setColumnCount(0)
        self.table_search_rank.setRowCount(0)
        self.verticalLayout.addWidget(self.table_search_rank)
        self.HL_bottom.addWidget(self.gb_ranking)
        self.gb_article = QtWidgets.QGroupBox(self.tab_search)
        self.gb_article.setObjectName("gb_article")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gb_article)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tx_search_article_result = QtWidgets.QTextEdit(self.gb_article)
        self.tx_search_article_result.setObjectName("tx_search_article_result")
        self.verticalLayout_5.addWidget(self.tx_search_article_result)
        self.HL_bottom.addWidget(self.gb_article)
        self.verticalLayout_3.addLayout(self.HL_bottom)
        self.tabWidget.addTab(self.tab_search, "")
        self.tab_scrapers = QtWidgets.QWidget()
        self.tab_scrapers.setObjectName("tab_scrapers")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_scrapers)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gb_scrapers_elPais = QtWidgets.QGroupBox(self.tab_scrapers)
        self.gb_scrapers_elPais.setObjectName("gb_scrapers_elPais")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.gb_scrapers_elPais)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.cb_scrapers_elPais = QtWidgets.QComboBox(self.gb_scrapers_elPais)
        self.cb_scrapers_elPais.setObjectName("cb_scrapers_elPais")
        self.cb_scrapers_elPais.addItem("")
        self.cb_scrapers_elPais.addItem("")
        self.cb_scrapers_elPais.addItem("")
        self.cb_scrapers_elPais.addItem("")
        self.verticalLayout_11.addWidget(self.cb_scrapers_elPais)
        self.btn_scrapers_elPais_run = QtWidgets.QPushButton(self.gb_scrapers_elPais)
        self.btn_scrapers_elPais_run.setObjectName("btn_scrapers_elPais_run")
        self.verticalLayout_11.addWidget(self.btn_scrapers_elPais_run)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_scrapers_elPais_science_result = QtWidgets.QLabel(self.gb_scrapers_elPais)
        self.lbl_scrapers_elPais_science_result.setObjectName("lbl_scrapers_elPais_science_result")
        self.gridLayout_3.addWidget(self.lbl_scrapers_elPais_science_result, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lbl_scrapers_elPais_tech_result = QtWidgets.QLabel(self.gb_scrapers_elPais)
        self.lbl_scrapers_elPais_tech_result.setObjectName("lbl_scrapers_elPais_tech_result")
        self.gridLayout_3.addWidget(self.lbl_scrapers_elPais_tech_result, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lbl_scrapers_elPais_health_result = QtWidgets.QLabel(self.gb_scrapers_elPais)
        self.lbl_scrapers_elPais_health_result.setObjectName("lbl_scrapers_elPais_health_result")
        self.gridLayout_3.addWidget(self.lbl_scrapers_elPais_health_result, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_19 = QtWidgets.QLabel(self.gb_scrapers_elPais)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gb_scrapers_elPais)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gb_scrapers_elPais)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gb_scrapers_elPais)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)
        self.lbl_scrapers_elPais_total_result = QtWidgets.QLabel(self.gb_scrapers_elPais)
        self.lbl_scrapers_elPais_total_result.setObjectName("lbl_scrapers_elPais_total_result")
        self.gridLayout_3.addWidget(self.lbl_scrapers_elPais_total_result, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_11.addLayout(self.gridLayout_3)
        self.gridLayout_5.addWidget(self.gb_scrapers_elPais, 0, 2, 1, 1)
        self.gb_scrapers_elMundo = QtWidgets.QGroupBox(self.tab_scrapers)
        self.gb_scrapers_elMundo.setObjectName("gb_scrapers_elMundo")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.gb_scrapers_elMundo)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.cb_scrapers_elMundo = QtWidgets.QComboBox(self.gb_scrapers_elMundo)
        self.cb_scrapers_elMundo.setObjectName("cb_scrapers_elMundo")
        self.cb_scrapers_elMundo.addItem("")
        self.cb_scrapers_elMundo.addItem("")
        self.cb_scrapers_elMundo.addItem("")
        self.cb_scrapers_elMundo.addItem("")
        self.verticalLayout_9.addWidget(self.cb_scrapers_elMundo)
        self.btn_scrapers_elMundo_run = QtWidgets.QPushButton(self.gb_scrapers_elMundo)
        self.btn_scrapers_elMundo_run.setObjectName("btn_scrapers_elMundo_run")
        self.verticalLayout_9.addWidget(self.btn_scrapers_elMundo_run)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_scrapers_elMundo_health_result = QtWidgets.QLabel(self.gb_scrapers_elMundo)
        self.lbl_scrapers_elMundo_health_result.setObjectName("lbl_scrapers_elMundo_health_result")
        self.gridLayout_2.addWidget(self.lbl_scrapers_elMundo_health_result, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(self.gb_scrapers_elMundo)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gb_scrapers_elMundo)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gb_scrapers_elMundo)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gb_scrapers_elMundo)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 1, 1, 1)
        self.lbl_scrapers_elMundo_science_result = QtWidgets.QLabel(self.gb_scrapers_elMundo)
        self.lbl_scrapers_elMundo_science_result.setObjectName("lbl_scrapers_elMundo_science_result")
        self.gridLayout_2.addWidget(self.lbl_scrapers_elMundo_science_result, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.lbl_scrapers_elMundo_tech_result = QtWidgets.QLabel(self.gb_scrapers_elMundo)
        self.lbl_scrapers_elMundo_tech_result.setObjectName("lbl_scrapers_elMundo_tech_result")
        self.gridLayout_2.addWidget(self.lbl_scrapers_elMundo_tech_result, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.lbl_scrapers_elMundo_total_result = QtWidgets.QLabel(self.gb_scrapers_elMundo)
        self.lbl_scrapers_elMundo_total_result.setObjectName("lbl_scrapers_elMundo_total_result")
        self.gridLayout_2.addWidget(self.lbl_scrapers_elMundo_total_result, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_9.addLayout(self.gridLayout_2)
        self.gridLayout_5.addWidget(self.gb_scrapers_elMundo, 0, 1, 1, 1)
        self.gb_scrapers_20m = QtWidgets.QGroupBox(self.tab_scrapers)
        self.gb_scrapers_20m.setObjectName("gb_scrapers_20m")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.gb_scrapers_20m)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cb_scrapers_20m = QtWidgets.QComboBox(self.gb_scrapers_20m)
        self.cb_scrapers_20m.setObjectName("cb_scrapers_20m")
        self.cb_scrapers_20m.addItem("")
        self.cb_scrapers_20m.addItem("")
        self.cb_scrapers_20m.addItem("")
        self.cb_scrapers_20m.addItem("")
        self.verticalLayout_8.addWidget(self.cb_scrapers_20m)
        self.btn_scrapers_20m_run = QtWidgets.QPushButton(self.gb_scrapers_20m)
        self.btn_scrapers_20m_run.setObjectName("btn_scrapers_20m_run")
        self.verticalLayout_8.addWidget(self.btn_scrapers_20m_run)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gb_scrapers_20m)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gb_scrapers_20m)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lbl_scrapers_20m_health_result = QtWidgets.QLabel(self.gb_scrapers_20m)
        self.lbl_scrapers_20m_health_result.setObjectName("lbl_scrapers_20m_health_result")
        self.gridLayout.addWidget(self.lbl_scrapers_20m_health_result, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.gb_scrapers_20m)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gb_scrapers_20m)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lbl_scrapers_20m_science_result = QtWidgets.QLabel(self.gb_scrapers_20m)
        self.lbl_scrapers_20m_science_result.setObjectName("lbl_scrapers_20m_science_result")
        self.gridLayout.addWidget(self.lbl_scrapers_20m_science_result, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lbl_scrapers_20m_tech_result = QtWidgets.QLabel(self.gb_scrapers_20m)
        self.lbl_scrapers_20m_tech_result.setObjectName("lbl_scrapers_20m_tech_result")
        self.gridLayout.addWidget(self.lbl_scrapers_20m_tech_result, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lbl_scrapers_20m_total_result = QtWidgets.QLabel(self.gb_scrapers_20m)
        self.lbl_scrapers_20m_total_result.setObjectName("lbl_scrapers_20m_total_result")
        self.gridLayout.addWidget(self.lbl_scrapers_20m_total_result, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addLayout(self.gridLayout)
        self.gridLayout_5.addWidget(self.gb_scrapers_20m, 0, 0, 1, 1)
        self.btn_scrapers_run_all = QtWidgets.QPushButton(self.tab_scrapers)
        self.btn_scrapers_run_all.setObjectName("btn_scrapers_run_all")
        self.gridLayout_5.addWidget(self.btn_scrapers_run_all, 1, 0, 1, 2)
        self.btn_scrapers_refresh_sta = QtWidgets.QPushButton(self.tab_scrapers)
        self.btn_scrapers_refresh_sta.setObjectName("btn_scrapers_refresh_sta")
        self.gridLayout_5.addWidget(self.btn_scrapers_refresh_sta, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.tab_scrapers, "")
        self.tab_compare = QtWidgets.QWidget()
        self.tab_compare.setObjectName("tab_compare")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_compare)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gb_references = QtWidgets.QGroupBox(self.tab_compare)
        self.gb_references.setObjectName("gb_references")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gb_references)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.HL_search_2 = QtWidgets.QHBoxLayout()
        self.HL_search_2.setObjectName("HL_search_2")
        self.lbl_ref_source = QtWidgets.QLabel(self.gb_references)
        self.lbl_ref_source.setObjectName("lbl_ref_source")
        self.HL_search_2.addWidget(self.lbl_ref_source)
        self.cb_ref_source = QtWidgets.QComboBox(self.gb_references)
        self.cb_ref_source.setObjectName("cb_ref_source")
        self.cb_ref_source.addItem("")
        self.cb_ref_source.addItem("")
        self.cb_ref_source.addItem("")
        self.cb_ref_source.addItem("")
        self.HL_search_2.addWidget(self.cb_ref_source)
        self.verticalLayout_4.addLayout(self.HL_search_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_ref_cat = QtWidgets.QLabel(self.gb_references)
        self.lbl_ref_cat.setObjectName("lbl_ref_cat")
        self.horizontalLayout_6.addWidget(self.lbl_ref_cat)
        self.cb_ref_cat = QtWidgets.QComboBox(self.gb_references)
        self.cb_ref_cat.setObjectName("cb_ref_cat")
        self.cb_ref_cat.addItem("")
        self.cb_ref_cat.addItem("")
        self.cb_ref_cat.addItem("")
        self.cb_ref_cat.addItem("")
        self.horizontalLayout_6.addWidget(self.cb_ref_cat)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_ref_top = QtWidgets.QLabel(self.gb_references)
        self.lbl_ref_top.setObjectName("lbl_ref_top")
        self.horizontalLayout_7.addWidget(self.lbl_ref_top)
        self.cb_ref_top = QtWidgets.QComboBox(self.gb_references)
        self.cb_ref_top.setObjectName("cb_ref_top")
        self.cb_ref_top.addItem("")
        self.cb_ref_top.addItem("")
        self.cb_ref_top.addItem("")
        self.cb_ref_top.addItem("")
        self.cb_ref_top.addItem("")
        self.cb_ref_top.addItem("")
        self.horizontalLayout_7.addWidget(self.cb_ref_top)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.btn_ref_search = QtWidgets.QPushButton(self.gb_references)
        self.btn_ref_search.setObjectName("btn_ref_search")
        self.verticalLayout_4.addWidget(self.btn_ref_search)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.VL_ref_articles = QtWidgets.QVBoxLayout()
        self.VL_ref_articles.setObjectName("VL_ref_articles")
        self.lbl_prev_articles = QtWidgets.QLabel(self.gb_references)
        self.lbl_prev_articles.setObjectName("lbl_prev_articles")
        self.VL_ref_articles.addWidget(self.lbl_prev_articles)
        self.scroll_ref_articles = QtWidgets.QScrollArea(self.gb_references)
        self.scroll_ref_articles.setWidgetResizable(True)
        self.scroll_ref_articles.setObjectName("scroll_ref_articles")
        self.scroll_ref_articles_items = QtWidgets.QWidget()
        self.scroll_ref_articles_items.setGeometry(QtCore.QRect(0, 0, 336, 216))
        self.scroll_ref_articles_items.setObjectName("scroll_ref_articles_items")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scroll_ref_articles_items)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.table_compare_ref_articles = QtWidgets.QTableWidget(self.scroll_ref_articles_items)
        self.table_compare_ref_articles.setObjectName("table_compare_ref_articles")
        self.table_compare_ref_articles.setColumnCount(0)
        self.table_compare_ref_articles.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.table_compare_ref_articles)
        self.scroll_ref_articles.setWidget(self.scroll_ref_articles_items)
        self.VL_ref_articles.addWidget(self.scroll_ref_articles)
        self.horizontalLayout_5.addLayout(self.VL_ref_articles)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.lbl_ref_preview = QtWidgets.QLabel(self.gb_references)
        self.lbl_ref_preview.setObjectName("lbl_ref_preview")
        self.verticalLayout_6.addWidget(self.lbl_ref_preview)
        self.tx_compare_preview = QtWidgets.QTextEdit(self.gb_references)
        self.tx_compare_preview.setObjectName("tx_compare_preview")
        self.verticalLayout_6.addWidget(self.tx_compare_preview)
        self.horizontalLayout.addWidget(self.gb_references)
        self.gb_results = QtWidgets.QGroupBox(self.tab_compare)
        self.gb_results.setObjectName("gb_results")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.gb_results)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.HL_results = QtWidgets.QHBoxLayout()
        self.HL_results.setObjectName("HL_results")
        self.lbl_res_source = QtWidgets.QLabel(self.gb_results)
        self.lbl_res_source.setObjectName("lbl_res_source")
        self.HL_results.addWidget(self.lbl_res_source)
        self.cb_res_source = QtWidgets.QComboBox(self.gb_results)
        self.cb_res_source.setObjectName("cb_res_source")
        self.cb_res_source.addItem("")
        self.cb_res_source.addItem("")
        self.cb_res_source.addItem("")
        self.cb_res_source.addItem("")
        self.HL_results.addWidget(self.cb_res_source)
        self.VL_res_rank = QtWidgets.QVBoxLayout()
        self.VL_res_rank.setObjectName("VL_res_rank")
        self.lbl_res_rank = QtWidgets.QLabel(self.gb_results)
        self.lbl_res_rank.setObjectName("lbl_res_rank")
        self.VL_res_rank.addWidget(self.lbl_res_rank)
        self.scroll_res_rank = QtWidgets.QScrollArea(self.gb_results)
        self.scroll_res_rank.setWidgetResizable(True)
        self.scroll_res_rank.setObjectName("scroll_res_rank")
        self.scroll_res_rank_items = QtWidgets.QWidget()
        self.scroll_res_rank_items.setGeometry(QtCore.QRect(0, 0, 354, 216))
        self.scroll_res_rank_items.setObjectName("scroll_res_rank_items")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.scroll_res_rank_items)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.table_compare_ref_rank = QtWidgets.QTableWidget(self.scroll_res_rank_items)
        self.table_compare_ref_rank.setObjectName("table_compare_ref_rank")
        self.table_compare_ref_rank.setColumnCount(0)
        self.table_compare_ref_rank.setRowCount(0)
        self.verticalLayout_12.addWidget(self.table_compare_ref_rank)
        self.scroll_res_rank.setWidget(self.scroll_res_rank_items)
        self.VL_res_rank.addWidget(self.scroll_res_rank)
        self.HL_results.addLayout(self.VL_res_rank)
        self.verticalLayout_7.addLayout(self.HL_results)
        self.lbl_result_article = QtWidgets.QLabel(self.gb_results)
        self.lbl_result_article.setObjectName("lbl_result_article")
        self.verticalLayout_7.addWidget(self.lbl_result_article)
        self.tx_compare_article = QtWidgets.QTextEdit(self.gb_results)
        self.tx_compare_article.setObjectName("tx_compare_article")
        self.verticalLayout_7.addWidget(self.tx_compare_article)
        self.horizontalLayout.addWidget(self.gb_results)
        self.tabWidget.addTab(self.tab_compare, "")
        self.verticalLayout_10.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lexical Analysis"))
        self.gb_options.setTitle(_translate("MainWindow", "Options"))
        self.lbl_query.setText(_translate("MainWindow", "Query"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.lbl_top.setText(_translate("MainWindow", "Top N"))
        self.cb_top.setItemText(0, _translate("MainWindow", "Select"))
        self.cb_top.setItemText(1, _translate("MainWindow", "1"))
        self.cb_top.setItemText(2, _translate("MainWindow", "2"))
        self.cb_top.setItemText(3, _translate("MainWindow", "3"))
        self.cb_top.setItemText(4, _translate("MainWindow", "4"))
        self.cb_top.setItemText(5, _translate("MainWindow", "5"))
        self.lbl_filter.setText(_translate("MainWindow", "Filter"))
        self.cb_filter.setItemText(0, _translate("MainWindow", "All Souces"))
        self.cb_filter.setItemText(1, _translate("MainWindow", "20 Minutos"))
        self.cb_filter.setItemText(2, _translate("MainWindow", "El Mundo"))
        self.cb_filter.setItemText(3, _translate("MainWindow", "El Pais"))
        self.btn_make_analysis.setText(_translate("MainWindow", "Make Analysis"))
        self.gb_ranking.setTitle(_translate("MainWindow", "Ranking"))
        self.gb_article.setTitle(_translate("MainWindow", "Article"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_search), _translate("MainWindow", "Search"))
        self.gb_scrapers_elPais.setTitle(_translate("MainWindow", "El Pais"))
        self.cb_scrapers_elPais.setItemText(0, _translate("MainWindow", "All Categories"))
        self.cb_scrapers_elPais.setItemText(1, _translate("MainWindow", "Health"))
        self.cb_scrapers_elPais.setItemText(2, _translate("MainWindow", "Science"))
        self.cb_scrapers_elPais.setItemText(3, _translate("MainWindow", "Technology"))
        self.btn_scrapers_elPais_run.setText(_translate("MainWindow", "Launch"))
        self.lbl_scrapers_elPais_science_result.setText(_translate("MainWindow", "0"))
        self.lbl_scrapers_elPais_tech_result.setText(_translate("MainWindow", "0"))
        self.lbl_scrapers_elPais_health_result.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "Science"))
        self.label_21.setText(_translate("MainWindow", "Technology"))
        self.label_18.setText(_translate("MainWindow", "Health"))
        self.label_23.setText(_translate("MainWindow", "Total"))
        self.lbl_scrapers_elPais_total_result.setText(_translate("MainWindow", "0"))
        self.gb_scrapers_elMundo.setTitle(_translate("MainWindow", "El Mundo"))
        self.cb_scrapers_elMundo.setItemText(0, _translate("MainWindow", "All Categories"))
        self.cb_scrapers_elMundo.setItemText(1, _translate("MainWindow", "Health"))
        self.cb_scrapers_elMundo.setItemText(2, _translate("MainWindow", "Science"))
        self.cb_scrapers_elMundo.setItemText(3, _translate("MainWindow", "Technology"))
        self.btn_scrapers_elMundo_run.setText(_translate("MainWindow", "Launch"))
        self.lbl_scrapers_elMundo_health_result.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "Technology"))
        self.label_11.setText(_translate("MainWindow", "Science"))
        self.label_10.setText(_translate("MainWindow", "Health"))
        self.label_13.setText(_translate("MainWindow", "Total"))
        self.lbl_scrapers_elMundo_science_result.setText(_translate("MainWindow", "0"))
        self.lbl_scrapers_elMundo_tech_result.setText(_translate("MainWindow", "0"))
        self.lbl_scrapers_elMundo_total_result.setText(_translate("MainWindow", "0"))
        self.gb_scrapers_20m.setTitle(_translate("MainWindow", "20 Minutos"))
        self.cb_scrapers_20m.setItemText(0, _translate("MainWindow", "All Categories"))
        self.cb_scrapers_20m.setItemText(1, _translate("MainWindow", "Health"))
        self.cb_scrapers_20m.setItemText(2, _translate("MainWindow", "Science"))
        self.cb_scrapers_20m.setItemText(3, _translate("MainWindow", "Technology"))
        self.btn_scrapers_20m_run.setText(_translate("MainWindow", "Launch"))
        self.label.setText(_translate("MainWindow", "Health"))
        self.label_2.setText(_translate("MainWindow", "Science"))
        self.lbl_scrapers_20m_health_result.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Technology"))
        self.label_5.setText(_translate("MainWindow", "Total"))
        self.lbl_scrapers_20m_science_result.setText(_translate("MainWindow", "0"))
        self.lbl_scrapers_20m_tech_result.setText(_translate("MainWindow", "0"))
        self.lbl_scrapers_20m_total_result.setText(_translate("MainWindow", "0"))
        self.btn_scrapers_run_all.setText(_translate("MainWindow", "Launch All"))
        self.btn_scrapers_refresh_sta.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scrapers), _translate("MainWindow", "Scrapers"))
        self.gb_references.setTitle(_translate("MainWindow", "Reference"))
        self.lbl_ref_source.setText(_translate("MainWindow", "Source"))
        self.cb_ref_source.setItemText(0, _translate("MainWindow", "All Sources"))
        self.cb_ref_source.setItemText(1, _translate("MainWindow", "20 Minutos"))
        self.cb_ref_source.setItemText(2, _translate("MainWindow", "El Mundo"))
        self.cb_ref_source.setItemText(3, _translate("MainWindow", "El Pais"))
        self.lbl_ref_cat.setText(_translate("MainWindow", "Category"))
        self.cb_ref_cat.setItemText(0, _translate("MainWindow", "All Categories"))
        self.cb_ref_cat.setItemText(1, _translate("MainWindow", "Health"))
        self.cb_ref_cat.setItemText(2, _translate("MainWindow", "Science"))
        self.cb_ref_cat.setItemText(3, _translate("MainWindow", "Technology"))
        self.lbl_ref_top.setText(_translate("MainWindow", "Top N"))
        self.cb_ref_top.setItemText(0, _translate("MainWindow", "Select"))
        self.cb_ref_top.setItemText(1, _translate("MainWindow", "1"))
        self.cb_ref_top.setItemText(2, _translate("MainWindow", "2"))
        self.cb_ref_top.setItemText(3, _translate("MainWindow", "3"))
        self.cb_ref_top.setItemText(4, _translate("MainWindow", "4"))
        self.cb_ref_top.setItemText(5, _translate("MainWindow", "5"))
        self.btn_ref_search.setText(_translate("MainWindow", "Search"))
        self.lbl_prev_articles.setText(_translate("MainWindow", "Articles"))
        self.lbl_ref_preview.setText(_translate("MainWindow", "Preview"))
        self.gb_results.setTitle(_translate("MainWindow", "Results"))
        self.lbl_res_source.setText(_translate("MainWindow", "Source"))
        self.cb_res_source.setItemText(0, _translate("MainWindow", "All Categories"))
        self.cb_res_source.setItemText(1, _translate("MainWindow", "20 Minutos"))
        self.cb_res_source.setItemText(2, _translate("MainWindow", "El Mundo"))
        self.cb_res_source.setItemText(3, _translate("MainWindow", "El Pais"))
        self.lbl_res_rank.setText(_translate("MainWindow", "Ranking"))
        self.lbl_result_article.setText(_translate("MainWindow", "Article"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_compare), _translate("MainWindow", "Compare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
