# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(853, 712)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(MainWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(0, 0))
        self.content_frame.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.content_frame)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.frame_nav = QFrame(self.content_frame)
        self.frame_nav.setObjectName(u"frame_nav")
        self.frame_nav.setMinimumSize(QSize(0, 40))
        self.frame_nav.setMaximumSize(QSize(16777215, 40))
        self.frame_nav.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_nav.setFrameShape(QFrame.StyledPanel)
        self.frame_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_nav)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_tittle = QLabel(self.frame_nav)
        self.label_tittle.setObjectName(u"label_tittle")
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        self.label_tittle.setFont(font)
        self.label_tittle.setStyleSheet(u"color: rgb(255, 255, 255) ;")

        self.horizontalLayout_6.addWidget(self.label_tittle)

        self.butttons_holder_frame = QFrame(self.frame_nav)
        self.butttons_holder_frame.setObjectName(u"butttons_holder_frame")
        self.butttons_holder_frame.setMinimumSize(QSize(110, 30))
        self.butttons_holder_frame.setMaximumSize(QSize(110, 16777215))
        self.butttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.butttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.butttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(0, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./assets/icons/minimize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_button.setIcon(icon)
        self.restore_button = QToolButton(self.butttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(30, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/restore-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_button.setIcon(icon1)
        self.maximize_button = QToolButton(self.butttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(30, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/maximize-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_button.setIcon(icon2)
        self.close_button = QToolButton(self.butttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(60, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/close-window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.butttons_holder_frame)


        self.verticalLayout_7.addWidget(self.frame_nav)

        self.frame_superior = QFrame(self.content_frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMaximumSize(QSize(16777215, 65))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(212, 172, 13 );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(154, 125, 10);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.genero_button = QPushButton(self.frame_superior)
        self.genero_button.setObjectName(u"genero_button")
        self.genero_button.setMinimumSize(QSize(170, 0))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT Condensed Extra Bold"])
        font1.setPointSize(10)
        self.genero_button.setFont(font1)
        self.genero_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(60, 76, 116 );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(39, 49, 73 );\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.genero_button)

        self.categorias_vendidas_button = QPushButton(self.frame_superior)
        self.categorias_vendidas_button.setObjectName(u"categorias_vendidas_button")
        self.categorias_vendidas_button.setMinimumSize(QSize(170, 0))
        self.categorias_vendidas_button.setFont(font1)
        self.categorias_vendidas_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(148, 52, 68  );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(97, 35, 45);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.categorias_vendidas_button)

        self.marca_button = QPushButton(self.frame_superior)
        self.marca_button.setObjectName(u"marca_button")
        self.marca_button.setMinimumSize(QSize(170, 0))
        self.marca_button.setFont(font1)
        self.marca_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(60, 76, 116 );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(39, 49, 73 );\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.marca_button)

        self.importes_button = QPushButton(self.frame_superior)
        self.importes_button.setObjectName(u"importes_button")
        self.importes_button.setMinimumSize(QSize(170, 0))
        self.importes_button.setFont(font1)
        self.importes_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(148, 52, 68  );\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(97, 35, 45);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.importes_button)

        self.recuento_button = QPushButton(self.frame_superior)
        self.recuento_button.setObjectName(u"recuento_button")
        self.recuento_button.setMinimumSize(QSize(35, 0))
        self.recuento_button.setMaximumSize(QSize(16777215, 16777215))
        self.recuento_button.setFont(font1)
        self.recuento_button.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(98, 98, 98);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.recuento_button)


        self.verticalLayout_7.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.content_frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_calzados = QFrame(self.frame_inferior)
        self.frame_calzados.setObjectName(u"frame_calzados")
        self.frame_calzados.setStyleSheet(u"background-color: rgb(60, 76, 116);")
        self.frame_calzados.setFrameShape(QFrame.StyledPanel)
        self.frame_calzados.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_calzados)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.calzados_pushButton = QPushButton(self.frame_calzados)
        self.calzados_pushButton.setObjectName(u"calzados_pushButton")
        self.calzados_pushButton.setMinimumSize(QSize(0, 205))

        self.verticalLayout_3.addWidget(self.calzados_pushButton)


        self.horizontalLayout.addWidget(self.frame_calzados)

        self.frame_medias = QFrame(self.frame_inferior)
        self.frame_medias.setObjectName(u"frame_medias")
        self.frame_medias.setStyleSheet(u"background-color: rgb(228, 228, 228);")
        self.frame_medias.setFrameShape(QFrame.StyledPanel)
        self.frame_medias.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_medias)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.medias_pushButton = QPushButton(self.frame_medias)
        self.medias_pushButton.setObjectName(u"medias_pushButton")
        self.medias_pushButton.setMinimumSize(QSize(0, 205))

        self.verticalLayout_4.addWidget(self.medias_pushButton)


        self.horizontalLayout.addWidget(self.frame_medias)

        self.frame_vacio = QFrame(self.frame_inferior)
        self.frame_vacio.setObjectName(u"frame_vacio")
        self.frame_vacio.setStyleSheet(u"background-color: black;")
        self.frame_vacio.setFrameShape(QFrame.StyledPanel)
        self.frame_vacio.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_vacio)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_logo = QLabel(self.frame_vacio)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setStyleSheet(u"QLabel{\n"
"image:url(:/imagess/strip.png);\n"
"}")

        self.verticalLayout_9.addWidget(self.label_logo)


        self.horizontalLayout.addWidget(self.frame_vacio)


        self.verticalLayout_7.addWidget(self.frame_inferior)

        self.frame_action = QFrame(self.content_frame)
        self.frame_action.setObjectName(u"frame_action")
        self.frame_action.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_action.setFrameShape(QFrame.StyledPanel)
        self.frame_action.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_action)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(72, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.porcentajes_label = QLabel(self.frame_action)
        self.porcentajes_label.setObjectName(u"porcentajes_label")
        self.porcentajes_label.setMinimumSize(QSize(550, 0))
        self.porcentajes_label.setFont(font1)
        self.porcentajes_label.setStyleSheet(u"color: white;")
        self.porcentajes_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.porcentajes_label)

        self.horizontalSpacer_3 = QSpacerItem(72, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addWidget(self.frame_action)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.label_tittle.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.genero_button.setText(QCoreApplication.translate("MainWindow", u"Generos + Vendidas", None))
        self.categorias_vendidas_button.setText(QCoreApplication.translate("MainWindow", u"Categor\u00edas + Vendidas", None))
        self.marca_button.setText(QCoreApplication.translate("MainWindow", u"Marcas + Vendidas", None))
        self.importes_button.setText(QCoreApplication.translate("MainWindow", u"Importes", None))
        self.recuento_button.setText(QCoreApplication.translate("MainWindow", u"RECUENTO", None))
        self.calzados_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.medias_pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.porcentajes_label.setText("")
    # retranslateUi

