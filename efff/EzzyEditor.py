from PyQt5.QtWidgets import (
    QApplication, QWidget,QFileDialog,QLabel,QPushButton, QListWidget,QHBoxLayout,QVBoxLayout
)
app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle("Easy Editor")

but_folder = QPushButton("Папка")
but_left = QPushButton("Вліво")
but_right = QPushButton("Вправо")
but_mirrow = QPushButton("Дзеркально")
but_blur = QPushButton("Різкість")
but_bw = QPushButton("Ч/Б")

list = QListWidget()
label_img =QLabel("Kartunka")
lineH = QHBoxLayout()
lineH2 = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()

lineV1.addWidget(but_folder)
lineV1.addWidget(list)
lineH2.addWidget(but_left)
lineH2.addWidget(but_right)
lineH2.addWidget(but_mirrow)
lineH2.addWidget(but_blur)
lineH2.addWidget(but_bw)
lineV2.addWidget(label_img)
lineV2.addLayout(lineH2)

lineH.addLayout(lineV1,25)
lineH.addLayout(lineV2,75)

win.setLayout(lineH)

win.show()
app.exec_()
