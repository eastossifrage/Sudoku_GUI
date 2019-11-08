# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QApplication)
from PyQt5.QtGui import (QBitmap, QPainter, QPixmap)


class Sudoku(QWidget):
    def __init__(self):
        super(Sudoku, self).__init__()
        self.pix = QBitmap("./images/数独背景.jpg")
        self.resize(self.pix.size())
        self.setMask(self.pix)
        self.show()

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap("./images/数独界面.jpg"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sudoku()
    sys.exit(app.exec_())