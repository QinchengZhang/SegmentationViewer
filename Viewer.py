# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import glob
import os

import numpy as np
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBitmap, QPixmap, QIcon
from PyQt5.QtWidgets import QFileDialog
import evaluate


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 629)
        MainWindow.setAnimated(True)
        MainWindow.setWindowIcon(QIcon('viewer.ico'))
        MainWindow.setWindowTitle("SegmentationViewer1.0")
        self.image_list = []
        self.current_image_mark = 0
        self.path_image = None
        self.path_mask_GT = None
        self.path_mask_pred = None

        self.data = {'image': None, 'GT': None, 'pred': None}

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_path = QtWidgets.QLabel(self.main_widget)
        self.file_path.setObjectName("file_path")
        self.verticalLayout.addWidget(self.file_path)
        self.progressBar = QtWidgets.QProgressBar(self.main_widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setFormat('%v/%m')
        self.verticalLayout.addWidget(self.progressBar)
        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.image = QtWidgets.QLabel(self.tab)
        self.image.setFixedSize(341, 251)
        self.image.move(10, 50)
        self.image.setObjectName("image")
        self.mask_GT = QtWidgets.QLabel(self.tab)
        self.mask_GT.setFixedSize(341, 251)
        self.mask_GT.move(360, 50)
        self.mask_GT.setObjectName("GT")
        self.mask_pred = QtWidgets.QLabel(self.tab)
        self.mask_pred.setFixedSize(341, 251)
        self.mask_pred.move(710, 50)
        self.mask_pred.setObjectName("predict")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(140, 20, 81, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(490, 20, 81, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(840, 20, 81, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(630, 320, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(630, 350, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setEnabled(False)
        self.label_6.setGeometry(QtCore.QRect(630, 380, 54, 12))
        self.label_6.setObjectName("label_6")
        self.accuracy = QtWidgets.QLabel(self.tab)
        self.accuracy.setGeometry(QtCore.QRect(740, 320, 54, 12))
        self.accuracy.setObjectName("accuracy")
        self.dice = QtWidgets.QLabel(self.tab)
        self.dice.setGeometry(QtCore.QRect(740, 350, 54, 12))
        self.dice.setObjectName("dice")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.merge = QtWidgets.QLabel(self.tab_2)
        self.merge.setFixedSize(511, 431)
        self.merge.move(10, 0)
        self.merge.setObjectName("merge")
        self.merge_pred = QtWidgets.QLabel(self.tab_2)
        self.merge_pred.setFixedSize(511, 431)
        self.merge_pred.move(530, 0)
        self.merge_pred.setObjectName("merge_pred")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.widget = QtWidgets.QWidget(self.main_widget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Last = QtWidgets.QPushButton(self.widget)
        self.Last.setObjectName("Last")
        self.Last.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.Last)
        self.Next = QtWidgets.QPushButton(self.widget)
        self.Next.setObjectName("Next")
        self.Next.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.Next)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.main_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.ChooseImageDir = QtWidgets.QAction(MainWindow)
        self.ChooseImageDir.setObjectName("OpenDir")
        self.ChooseGTDir = QtWidgets.QAction(MainWindow)
        self.ChooseGTDir.setObjectName("action_GT_mask")
        self.ChoosePredDir = QtWidgets.QAction(MainWindow)
        self.ChoosePredDir.setObjectName("action_mask")
        self.menu.addAction(self.ChooseImageDir)
        self.menu.addSeparator()
        self.menu.addAction(self.ChooseGTDir)
        self.menu.addSeparator()
        self.menu.addAction(self.ChoosePredDir)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged['int'].connect(
            self.tabWidget.setCurrentIndex)
        self.tabWidget.tabBarClicked['int'].connect(
            self.tabWidget.setCurrentIndex)
        self.tabWidget.tabBarDoubleClicked['int'].connect(
            self.tabWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ChooseImageDir.triggered.connect(lambda: self.chooseImageDir())
        self.ChooseGTDir.triggered.connect(lambda: self.chooseGTDir())
        self.ChoosePredDir.triggered.connect(lambda: self.choosePredDir())

        self.Next.clicked.connect(lambda: self.next_image())
        self.Last.clicked.connect(lambda: self.last_image())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_path.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Image"))
        self.label_2.setText(_translate("MainWindow", "GT"))
        self.label_3.setText(_translate("MainWindow", "Predict"))
        self.label_4.setText(_translate("MainWindow", "Pixel Accuracy"))
        self.label_5.setText(_translate("MainWindow", "Dice Coefficient"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.accuracy.setText(_translate("MainWindow", "None"))
        self.dice.setText(_translate("MainWindow", "None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "对比模式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "合并模式"))
        self.Last.setText(_translate("MainWindow", "上一张"))
        self.Next.setText(_translate("MainWindow", "下一张"))
        self.menu.setTitle(_translate("MainWindow", "打开"))
        self.ChooseImageDir.setText(_translate("MainWindow", "选择图片文件夹"))
        self.ChooseGTDir.setText(_translate("MainWindow", "对比模式"))
        self.ChoosePredDir.setText(_translate("MainWindow", "合并模式"))
        self.ChooseGTDir.setText(_translate("MainWindow", "选择标注mask文件夹"))
        self.ChoosePredDir.setText(_translate("MainWindow", "选择预测mask文件夹"))

    def chooseImageDir(self):
        self.path_image = QFileDialog.getExistingDirectory(
            self.main_widget, "选择图片文件夹", "/")
        self.image_list = glob.glob(
            self.path_image + '/*.*[png, tiff, jpg, tif]')
        self.show('image')

    def chooseGTDir(self):
        self.path_mask_GT = QFileDialog.getExistingDirectory(
            self.main_widget, "选择标注文件夹", "/")
        self.check_path()
        self.show('GT')
        self.show_merge('GT')

    def choosePredDir(self):
        self.path_mask_pred = QFileDialog.getExistingDirectory(
            self.main_widget, "选择预测文件夹", "/")
        self.check_path(flag='pred')
        self.show('pred')
        self.show_merge('pred')

    def check_path(self, flag='GT'):
        for name in self.image_list:
            basename = os.path.basename(name)
            if not os.path.exists(os.path.join(self.path_mask_GT if flag == 'GT' else self.path_mask_pred, basename)):
                self.image_list.remove(name)
        self.progressBar.setMaximum(len(self.image_list))

    def show_image(self):
        if self.path_image is not None:
            self.show('image')
            if self.path_mask_GT is not None:
                self.show('GT')
                self.show_merge('GT')
            if self.path_mask_pred is not None:
                self.show('pred')
                self.show_merge('pred')
        else:
            raise('at least you choose image dir!')

    def show(self, flag='image'):
        (_, name) = os.path.split(self.image_list[self.current_image_mark])
        if flag == 'image':
            path = self.path_image
            plotwindow = self.image
        elif flag == 'GT':
            path = self.path_mask_GT
            plotwindow = self.mask_GT
        elif flag == 'pred':
            path = self.path_mask_pred
            plotwindow = self.mask_pred
        try:
            img = Image.open(os.path.join(path, name))
            self.data[flag] = np.array(img)
            if (flag == 'GT' and self.data['pred'] is not None) or (flag=='pred' and self.data['GT'] is not None):
                dice = evaluate.DiceCoeff(self.data['pred'], self.data['GT'])
                acc = evaluate.PixelAccuracy(self.data['pred'], self.data['GT'])
                self.dice.setText('{}'.format(dice))
                self.accuracy.setText('{}'.format(acc))
            self.progressBar.setValue(self.current_image_mark+1)
            img = img.resize((341, 251))
            self.file_path.setText(self.image_list[self.current_image_mark])
            plotwindow.setPixmap(img.toqpixmap())
            self.check_LastAndNext()
        except FileNotFoundError as e:
            raise(e)

    def show_merge(self, flag='GT'):
        if flag == 'GT':
            path = self.path_mask_GT
            plotwindow = self.merge
        elif flag == 'pred':
            path = self.path_mask_pred
            plotwindow = self.merge_pred
        (_, name) = os.path.split(self.image_list[self.current_image_mark])
        try:
            mask = Image.open(os.path.join(path, name))
            image = Image.open(self.image_list[self.current_image_mark])
            mask = mask.resize((511, 431))
            image = image.resize((511, 431))
            merge = np.array(image)
            mask_arr = np.array(mask)
            merge[mask_arr == 0] = [0, 0, 0]
            merge = Image.fromarray(merge)
            plotwindow.setPixmap(merge.toqpixmap())
        except FileNotFoundError as e:
            pass

    def next_image(self):
        self.current_image_mark += 1
        self.progressBar.setValue(self.current_image_mark+1)
        self.show_image()

    def last_image(self):
        self.current_image_mark -= 1
        self.progressBar.setValue(self.current_image_mark+1)
        self.show_image()

    def check_LastAndNext(self):
        if self.current_image_mark < len(self.image_list) - 1:
            self.Next.setEnabled(True)
        else:
            self.Next.setEnabled(False)
        if self.current_image_mark > 0:
            self.Last.setEnabled(True)
        else:
            self.Last.setEnabled(False)
