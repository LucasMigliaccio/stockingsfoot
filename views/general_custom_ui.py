from PySide6.QtCore import Qt

from PySide6.QtWidgets import QGraphicsDropShadowEffect

class GeneralCustomUi():
    def __init__(self, ui):
        self.ui= ui

        self.remove_default_title_bar()
        self.ui.frame_nav.mouseMoveEvent = self.move_window
        self.set_window_shadow()
        self.set_frame_nav_actions()


#maximizar
    def maximize_window(self):
        self.ui.showMaximized()
        self.ui.maximize_button.setVisible(False)
        self.ui.shadow_layout.setContentsMargins(0,0,0,0)

#restaurar
    def restore_window(self):
        self.ui.showNormal()
        self.ui.maximize_button.setVisible(True)
        self.ui.shadow_layout.setContentsMargins(10,10,10,10)

#nav buttons
    def set_frame_nav_actions(self):
        self.ui.close_button.clicked.connect(self.ui.close)
        self.ui.minimize_button.clicked.connect(self.ui.showMinimized)
        self.ui.maximize_button.clicked.connect(self.maximize_window)
        self.ui.restore_button.clicked.connect(self.restore_window)


#remueve la barra de titulo
    def remove_default_title_bar(self):
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.setWindowFlag(Qt.FramelessWindowHint)

    def mouse_press_event(self, event):
        #posicion de la ventana arrastrada
        self.drag_pos = event.globalPos()

#arrastrar ventanas
    def move_window(self, event):
        #mientras se mueva dentro presionando la nav, la ventana va a moverse
        if event.buttons() == Qt.LeftButton:
            self.ui.move(self.ui.pos() + event.globalPos() -  self.drag_pos)
            self.drag_pos = event.globalPos()

#shadow de la ventana
    def set_window_shadow(self):
        shadow=QGraphicsDropShadowEffect(self.ui)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#000000")
        self.ui.background_frame.setGraphicsEffect(shadow)
