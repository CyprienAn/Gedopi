# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\opeInventaireRechercheForm.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgInventRechercheForm(object):
    def setupUi(self, dlgInventRechercheForm):
        dlgInventRechercheForm.setObjectName("dlgInventRechercheForm")
        dlgInventRechercheForm.resize(375, 530)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dlgInventRechercheForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(dlgInventRechercheForm)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 355, 510))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.btnEt = QtWidgets.QPushButton(self.groupBox_2)
        self.btnEt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnEt.setObjectName("btnEt")
        self.horizontalLayout_12.addWidget(self.btnEt)
        self.btnOu = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnOu.setObjectName("btnOu")
        self.horizontalLayout_12.addWidget(self.btnOu)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.leCodeOpe = QtWidgets.QLineEdit(self.groupBox_2)
        self.leCodeOpe.setMinimumSize(QtCore.QSize(150, 0))
        self.leCodeOpe.setObjectName("leCodeOpe")
        self.horizontalLayout_13.addWidget(self.leCodeOpe)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.btnCode = QtWidgets.QPushButton(self.groupBox_2)
        self.btnCode.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnCode.setObjectName("btnCode")
        self.horizontalLayout_13.addWidget(self.btnCode)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.spnId = QtWidgets.QSpinBox(self.groupBox_2)
        self.spnId.setMaximum(100000)
        self.spnId.setObjectName("spnId")
        self.horizontalLayout_6.addWidget(self.spnId)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.btnId = QtWidgets.QPushButton(self.groupBox_2)
        self.btnId.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnId.setObjectName("btnId")
        self.horizontalLayout_6.addWidget(self.btnId)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.dateInventaire = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateInventaire.setObjectName("dateInventaire")
        self.horizontalLayout_7.addWidget(self.dateInventaire)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.btnDate = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDate.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnDate.setObjectName("btnDate")
        self.horizontalLayout_7.addWidget(self.btnDate)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.cmbRiviere = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbRiviere.sizePolicy().hasHeightForWidth())
        self.cmbRiviere.setSizePolicy(sizePolicy)
        self.cmbRiviere.setObjectName("cmbRiviere")
        self.horizontalLayout_8.addWidget(self.cmbRiviere)
        self.btnRiviere = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRiviere.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnRiviere.setObjectName("btnRiviere")
        self.horizontalLayout_8.addWidget(self.btnRiviere)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.cmbPdpg = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbPdpg.sizePolicy().hasHeightForWidth())
        self.cmbPdpg.setSizePolicy(sizePolicy)
        self.cmbPdpg.setObjectName("cmbPdpg")
        self.horizontalLayout_9.addWidget(self.cmbPdpg)
        self.btnPdpg = QtWidgets.QPushButton(self.groupBox_2)
        self.btnPdpg.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnPdpg.setObjectName("btnPdpg")
        self.horizontalLayout_9.addWidget(self.btnPdpg)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.cmbAappma = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbAappma.sizePolicy().hasHeightForWidth())
        self.cmbAappma.setSizePolicy(sizePolicy)
        self.cmbAappma.setObjectName("cmbAappma")
        self.horizontalLayout_10.addWidget(self.cmbAappma)
        self.btnAappma = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAappma.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnAappma.setObjectName("btnAappma")
        self.horizontalLayout_10.addWidget(self.btnAappma)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.cmbMeau = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbMeau.sizePolicy().hasHeightForWidth())
        self.cmbMeau.setSizePolicy(sizePolicy)
        self.cmbMeau.setObjectName("cmbMeau")
        self.horizontalLayout_14.addWidget(self.cmbMeau)
        self.btnMeau = QtWidgets.QPushButton(self.groupBox_2)
        self.btnMeau.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnMeau.setObjectName("btnMeau")
        self.horizontalLayout_14.addWidget(self.btnMeau)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.txtSql = QtWidgets.QTextEdit(self.groupBox_4)
        self.txtSql.setMaximumSize(QtCore.QSize(16777215, 100))
        self.txtSql.setObjectName("txtSql")
        self.verticalLayout_3.addWidget(self.txtSql)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btnPrevisualiser = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnPrevisualiser.setObjectName("btnPrevisualiser")
        self.horizontalLayout_11.addWidget(self.btnPrevisualiser)
        self.btnExec = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnExec.setObjectName("btnExec")
        self.horizontalLayout_11.addWidget(self.btnExec)
        self.btnRaz = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnRaz.setObjectName("btnRaz")
        self.horizontalLayout_11.addWidget(self.btnRaz)
        self.btnAnnuler = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnAnnuler.setObjectName("btnAnnuler")
        self.horizontalLayout_11.addWidget(self.btnAnnuler)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(dlgInventRechercheForm)
        QtCore.QMetaObject.connectSlotsByName(dlgInventRechercheForm)

    def retranslateUi(self, dlgInventRechercheForm):
        _translate = QtCore.QCoreApplication.translate
        dlgInventRechercheForm.setWindowTitle(_translate("dlgInventRechercheForm", "Recherche d\'inventaire(s)"))
        self.groupBox_2.setTitle(_translate("dlgInventRechercheForm", "Critère(s) :"))
        self.btnEt.setText(_translate("dlgInventRechercheForm", "Et"))
        self.btnOu.setText(_translate("dlgInventRechercheForm", "Ou"))
        self.label_12.setText(_translate("dlgInventRechercheForm", "Code Opération :"))
        self.btnCode.setText(_translate("dlgInventRechercheForm", "Ajouter"))
        self.label_7.setText(_translate("dlgInventRechercheForm", "ID :"))
        self.btnId.setText(_translate("dlgInventRechercheForm", "Ajouter"))
        self.label_8.setText(_translate("dlgInventRechercheForm", "Année :"))
        self.dateInventaire.setDisplayFormat(_translate("dlgInventRechercheForm", "yyyy"))
        self.btnDate.setText(_translate("dlgInventRechercheForm", "Ajouter"))
        self.label_9.setText(_translate("dlgInventRechercheForm", "Rivière :"))
        self.btnRiviere.setText(_translate("dlgInventRechercheForm", "Ajouter"))
        self.label_10.setText(_translate("dlgInventRechercheForm", "Contexte PDPG :"))
        self.btnPdpg.setText(_translate("dlgInventRechercheForm", "Ajouter"))
        self.label_11.setText(_translate("dlgInventRechercheForm", "AAPPMA :"))
        self.btnAappma.setText(_translate("dlgInventRechercheForm", "Ajouter"))
        self.label_13.setText(_translate("dlgInventRechercheForm", "Masse d\'eau :"))
        self.btnMeau.setText(_translate("dlgInventRechercheForm", "Ajouter"))
        self.groupBox_4.setTitle(_translate("dlgInventRechercheForm", "Requête SQL :"))
        self.label_6.setText(_translate("dlgInventRechercheForm", "<html><head/><body><p align=\"justify\"><span style=\" font-size:7pt;\">Attention : les modifications dans la requête sont possibles mais peuvent faire échouer celle-ci voir endommager la base de données ! ! !</span></p></body></html>"))
        self.txtSql.setHtml(_translate("dlgInventRechercheForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.btnPrevisualiser.setText(_translate("dlgInventRechercheForm", "Prévisualisation"))
        self.btnExec.setText(_translate("dlgInventRechercheForm", "Exécuter"))
        self.btnRaz.setText(_translate("dlgInventRechercheForm", "Réinitialiser"))
        self.btnAnnuler.setText(_translate("dlgInventRechercheForm", "Annuler"))

