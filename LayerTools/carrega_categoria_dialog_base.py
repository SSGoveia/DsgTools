# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carrega_categoria_dialog_base.ui'
#
# Created: Thu Nov 06 20:07:26 2014
#      by: PyQt4 UI code generator 4.10.2
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
        Form.resize(500, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 400))
        Form.setMaximumSize(QtCore.QSize(500, 400))
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 440, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.arquivoLineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.arquivoLineEdit.setObjectName(_fromUtf8("arquivoLineEdit"))
        self.horizontalLayout.addWidget(self.arquivoLineEdit)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonBuscarArquivo = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonBuscarArquivo.setObjectName(_fromUtf8("pushButtonBuscarArquivo"))
        self.horizontalLayout.addWidget(self.pushButtonBuscarArquivo)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 90, 440, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.coordSysLineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.coordSysLineEdit.setObjectName(_fromUtf8("coordSysLineEdit"))
        self.horizontalLayout_2.addWidget(self.coordSysLineEdit)
        spacerItem3 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButtonBuscarSistCoord = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonBuscarSistCoord.setObjectName(_fromUtf8("pushButtonBuscarSistCoord"))
        self.horizontalLayout_2.addWidget(self.pushButtonBuscarSistCoord)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 250, 181))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 237, 161))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.listWidgetOrigemCategoria = QtGui.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidgetOrigemCategoria.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidgetOrigemCategoria.setObjectName(_fromUtf8("listWidgetOrigemCategoria"))
        self.horizontalLayout_3.addWidget(self.listWidgetOrigemCategoria)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButtonSelecionaTodas = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonSelecionaTodas.setObjectName(_fromUtf8("pushButtonSelecionaTodas"))
        self.verticalLayout.addWidget(self.pushButtonSelecionaTodas)
        self.pushButtonSelecionaUma = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonSelecionaUma.setObjectName(_fromUtf8("pushButtonSelecionaUma"))
        self.verticalLayout.addWidget(self.pushButtonSelecionaUma)
        self.pushButtonDeselecionaUma = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonDeselecionaUma.setObjectName(_fromUtf8("pushButtonDeselecionaUma"))
        self.verticalLayout.addWidget(self.pushButtonDeselecionaUma)
        self.pushButtonDeselecionaTodas = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButtonDeselecionaTodas.setObjectName(_fromUtf8("pushButtonDeselecionaTodas"))
        self.verticalLayout.addWidget(self.pushButtonDeselecionaTodas)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.listWidgetDestinoCategoria = QtGui.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidgetDestinoCategoria.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidgetDestinoCategoria.setObjectName(_fromUtf8("listWidgetDestinoCategoria"))
        self.horizontalLayout_3.addWidget(self.listWidgetDestinoCategoria)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 150, 201, 181))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 191, 161))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBoxPonto = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxPonto.setObjectName(_fromUtf8("checkBoxPonto"))
        self.verticalLayout_2.addWidget(self.checkBoxPonto)
        self.checkBoxLinha = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxLinha.setObjectName(_fromUtf8("checkBoxLinha"))
        self.verticalLayout_2.addWidget(self.checkBoxLinha)
        self.checkBoxArea = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxArea.setObjectName(_fromUtf8("checkBoxArea"))
        self.verticalLayout_2.addWidget(self.checkBoxArea)
        self.checkBoxTodos = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxTodos.setObjectName(_fromUtf8("checkBoxTodos"))
        self.verticalLayout_2.addWidget(self.checkBoxTodos)
        self.checkBoxSomenteElementos = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxSomenteElementos.setObjectName(_fromUtf8("checkBoxSomenteElementos"))
        self.verticalLayout_2.addWidget(self.checkBoxSomenteElementos)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 350, 441, 31))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pushButtonOk = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout_4.addWidget(self.pushButtonOk)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pushButtonCancelar = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.horizontalLayout_4.addWidget(self.pushButtonCancelar)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButtonCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Load by Category", None))
        self.label.setText(_translate("Form", "File                                 ", None))
        self.pushButtonBuscarArquivo.setText(_translate("Form", "Search", None))
        self.label_2.setText(_translate("Form", "Coordinate System", None))
        self.pushButtonBuscarSistCoord.setText(_translate("Form", "Search", None))
        self.groupBox.setTitle(_translate("Form", "Load by Category", None))
        self.pushButtonSelecionaTodas.setToolTip(_translate("Form", "Select all categories in the database", None))
        self.pushButtonSelecionaTodas.setText(_translate("Form", ">>", None))
        self.pushButtonSelecionaUma.setToolTip(_translate("Form", "Select only the selected", None))
        self.pushButtonSelecionaUma.setText(_translate("Form", ">", None))
        self.pushButtonDeselecionaUma.setToolTip(_translate("Form", "Remove from list only the selected categories", None))
        self.pushButtonDeselecionaUma.setText(_translate("Form", "<", None))
        self.pushButtonDeselecionaTodas.setToolTip(_translate("Form", "Remove all categories", None))
        self.pushButtonDeselecionaTodas.setText(_translate("Form", "<<", None))
        self.groupBox_2.setTitle(_translate("Form", "Group by Geometry Type", None))
        self.checkBoxPonto.setText(_translate("Form", "Point", None))
        self.checkBoxLinha.setText(_translate("Form", "Line", None))
        self.checkBoxArea.setText(_translate("Form", "Polygon", None))
        self.checkBoxTodos.setText(_translate("Form", "Select All", None))
        self.checkBoxSomenteElementos.setText(_translate("Form", "Only layers with Elements", None))
        self.pushButtonOk.setText(_translate("Form", "Ok", None))
        self.pushButtonCancelar.setText(_translate("Form", "Cancel", None))
