# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 326)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mkeylogger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet(_fromUtf8("background-color: #2c3e50;\n"
"color: #bdc3c7;"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.keystokesText = QtGui.QTextEdit(Form)
        self.keystokesText.setStyleSheet(_fromUtf8("background-position: center;\n"
"border: 1px outset;\n"
"border-color: #0F2D40;\n"
"border-radius: 2px;\n"
"color: rgb(178, 197, 214);\n"
"background-color: #34495e;\n"
"font: 75 9pt \"MS Shell Dlg 2\";"))
        self.keystokesText.setDocumentTitle(_fromUtf8(""))
        self.keystokesText.setUndoRedoEnabled(False)
        self.keystokesText.setReadOnly(True)
        self.keystokesText.setObjectName(_fromUtf8("keystokesText"))
        self.gridLayout.addWidget(self.keystokesText, 1, 0, 1, 8)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.alwaysTopButton = QtGui.QPushButton(Form)
        self.alwaysTopButton.setMinimumSize(QtCore.QSize(0, 24))
        self.alwaysTopButton.setStyleSheet(_fromUtf8("QPushButton#alwaysTopButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#alwaysTopButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.alwaysTopButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/always_top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alwaysTopButton.setIcon(icon1)
        self.alwaysTopButton.setIconSize(QtCore.QSize(18, 18))
        self.alwaysTopButton.setCheckable(True)
        self.alwaysTopButton.setObjectName(_fromUtf8("alwaysTopButton"))
        self.gridLayout.addWidget(self.alwaysTopButton, 0, 7, 1, 1)
        self.startKeyloggingButton = QtGui.QPushButton(Form)
        self.startKeyloggingButton.setMinimumSize(QtCore.QSize(0, 0))
        self.startKeyloggingButton.setAcceptDrops(False)
        self.startKeyloggingButton.setStatusTip(_fromUtf8(""))
        self.startKeyloggingButton.setAutoFillBackground(False)
        self.startKeyloggingButton.setStyleSheet(_fromUtf8("QPushButton#startKeyloggingButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#startKeyloggingButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.startKeyloggingButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startKeyloggingButton.setIcon(icon2)
        self.startKeyloggingButton.setIconSize(QtCore.QSize(18, 18))
        self.startKeyloggingButton.setCheckable(True)
        self.startKeyloggingButton.setObjectName(_fromUtf8("startKeyloggingButton"))
        self.gridLayout.addWidget(self.startKeyloggingButton, 0, 0, 1, 1)
        self.stopKeyloggingButton = QtGui.QPushButton(Form)
        self.stopKeyloggingButton.setMinimumSize(QtCore.QSize(0, 0))
        self.stopKeyloggingButton.setStyleSheet(_fromUtf8("QPushButton#stopKeyloggingButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#stopKeyloggingButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.stopKeyloggingButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopKeyloggingButton.setIcon(icon3)
        self.stopKeyloggingButton.setIconSize(QtCore.QSize(18, 18))
        self.stopKeyloggingButton.setCheckable(True)
        self.stopKeyloggingButton.setChecked(True)
        self.stopKeyloggingButton.setObjectName(_fromUtf8("stopKeyloggingButton"))
        self.gridLayout.addWidget(self.stopKeyloggingButton, 0, 1, 1, 1)
        self.saveButton = QtGui.QPushButton(Form)
        self.saveButton.setStyleSheet(_fromUtf8("QPushButton#saveButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#saveButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.saveButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon4)
        self.saveButton.setIconSize(QtCore.QSize(18, 18))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout.addWidget(self.saveButton, 0, 3, 1, 1)
        self.smileyButton = QtGui.QPushButton(Form)
        self.smileyButton.setStyleSheet(_fromUtf8("QPushButton#smileyButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#smileyButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.smileyButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/smiley.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.smileyButton.setIcon(icon5)
        self.smileyButton.setIconSize(QtCore.QSize(18, 18))
        self.smileyButton.setCheckable(True)
        self.smileyButton.setObjectName(_fromUtf8("smileyButton"))
        self.gridLayout.addWidget(self.smileyButton, 0, 4, 1, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 2, 1, 1)
        self.bottomButton = QtGui.QPushButton(Form)
        self.bottomButton.setStyleSheet(_fromUtf8("QPushButton#bottomButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#bottomButton:checked {\n"
"            border-color: #27ae60;\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.bottomButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/bottom.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bottomButton.setIcon(icon6)
        self.bottomButton.setIconSize(QtCore.QSize(18, 18))
        self.bottomButton.setCheckable(True)
        self.bottomButton.setChecked(True)
        self.bottomButton.setObjectName(_fromUtf8("bottomButton"))
        self.gridLayout.addWidget(self.bottomButton, 0, 5, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.keystokesText.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.alwaysTopButton.setToolTip(_translate("Form", "Always Top", None))
        self.startKeyloggingButton.setToolTip(_translate("Form", "Start", None))
        self.stopKeyloggingButton.setToolTip(_translate("Form", "Stop", None))
        self.saveButton.setToolTip(_translate("Form", "Save", None))
        self.smileyButton.setToolTip(_translate("Form", "Smilies Detection", None))
        self.bottomButton.setToolTip(_translate("Form", "Alway Bottom", None))
