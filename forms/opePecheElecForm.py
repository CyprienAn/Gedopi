# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\opePecheElecForm.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dwcPecheMainForm(object):
    def setupUi(self, dwcPecheMainForm):
        dwcPecheMainForm.setObjectName("dwcPecheMainForm")
        dwcPecheMainForm.resize(518, 529)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dwcPecheMainForm.sizePolicy().hasHeightForWidth())
        dwcPecheMainForm.setSizePolicy(sizePolicy)
        dwcPecheMainForm.setMinimumSize(QtCore.QSize(518, 300))
        self.dwc_peche_elec_form = QtWidgets.QWidget()
        self.dwc_peche_elec_form.setObjectName("dwc_peche_elec_form")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.dwc_peche_elec_form)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.scrollArea = QtWidgets.QScrollArea(self.dwc_peche_elec_form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -387, 483, 944))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setContentsMargins(0, 1, 0, 1)
        self.horizontalLayout_41.setSpacing(2)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.btnFiltreCartoManuel = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnFiltreCartoManuel.setEnabled(False)
        self.btnFiltreCartoManuel.setMinimumSize(QtCore.QSize(120, 30))
        self.btnFiltreCartoManuel.setObjectName("btnFiltreCartoManuel")
        self.horizontalLayout_41.addWidget(self.btnFiltreCartoManuel)
        self.chkFiltreCartoAuto = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chkFiltreCartoAuto.setMinimumSize(QtCore.QSize(130, 0))
        self.chkFiltreCartoAuto.setObjectName("chkFiltreCartoAuto")
        self.horizontalLayout_41.addWidget(self.chkFiltreCartoAuto)
        self.btnFiltreAttributaire = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnFiltreAttributaire.setMinimumSize(QtCore.QSize(97, 30))
        self.btnFiltreAttributaire.setObjectName("btnFiltreAttributaire")
        self.horizontalLayout_41.addWidget(self.btnFiltreAttributaire)
        self.btnDeleteFiltrage = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnDeleteFiltrage.setEnabled(False)
        self.btnDeleteFiltrage.setMinimumSize(QtCore.QSize(110, 30))
        self.btnDeleteFiltrage.setObjectName("btnDeleteFiltrage")
        self.horizontalLayout_41.addWidget(self.btnDeleteFiltrage)
        self.verticalLayout.addLayout(self.horizontalLayout_41)
        self.chkVerrouAuto = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chkVerrouAuto.setChecked(True)
        self.chkVerrouAuto.setObjectName("chkVerrouAuto")
        self.verticalLayout.addWidget(self.chkVerrouAuto)
        self.chkVerrouModif = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.chkVerrouModif.setChecked(True)
        self.chkVerrouModif.setObjectName("chkVerrouModif")
        self.verticalLayout.addWidget(self.chkVerrouModif)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_commune = QtWidgets.QLabel(self.groupBox)
        self.lbl_commune.setObjectName("lbl_commune")
        self.horizontalLayout_3.addWidget(self.lbl_commune)
        self.cmbRiviere = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbRiviere.sizePolicy().hasHeightForWidth())
        self.cmbRiviere.setSizePolicy(sizePolicy)
        self.cmbRiviere.setMinimumSize(QtCore.QSize(170, 0))
        self.cmbRiviere.setObjectName("cmbRiviere")
        self.horizontalLayout_3.addWidget(self.cmbRiviere)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnStation = QtWidgets.QPushButton(self.groupBox)
        self.btnStation.setObjectName("btnStation")
        self.horizontalLayout_6.addWidget(self.btnStation)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_section = QtWidgets.QLabel(self.groupBox)
        self.lbl_section.setMinimumSize(QtCore.QSize(50, 0))
        self.lbl_section.setObjectName("lbl_section")
        self.horizontalLayout_5.addWidget(self.lbl_section)
        self.cmbStation = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbStation.sizePolicy().hasHeightForWidth())
        self.cmbStation.setSizePolicy(sizePolicy)
        self.cmbStation.setObjectName("cmbStation")
        self.horizontalLayout_5.addWidget(self.cmbStation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.leCodeOpe = QtWidgets.QLineEdit(self.groupBox_3)
        self.leCodeOpe.setAlignment(QtCore.Qt.AlignCenter)
        self.leCodeOpe.setObjectName("leCodeOpe")
        self.horizontalLayout_8.addWidget(self.leCodeOpe)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_20.addWidget(self.label_21)
        self.datePeche = QtWidgets.QDateEdit(self.groupBox_3)
        self.datePeche.setCalendarPopup(True)
        self.datePeche.setObjectName("datePeche")
        self.horizontalLayout_20.addWidget(self.datePeche)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem1)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_20)
        self.verticalLayout_8.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.chkComplete = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkComplete.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkComplete.setObjectName("chkComplete")
        self.horizontalLayout_27.addWidget(self.chkComplete)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.spnNbreAnode = QtWidgets.QSpinBox(self.groupBox_3)
        self.spnNbreAnode.setObjectName("spnNbreAnode")
        self.horizontalLayout_9.addWidget(self.spnNbreAnode)
        self.horizontalLayout_27.addLayout(self.horizontalLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_22.addWidget(self.label_23)
        self.cmbCondition = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbCondition.sizePolicy().hasHeightForWidth())
        self.cmbCondition.setSizePolicy(sizePolicy)
        self.cmbCondition.setObjectName("cmbCondition")
        self.horizontalLayout_22.addWidget(self.cmbCondition)
        self.horizontalLayout_28.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_21.addWidget(self.label_22)
        self.cmbMotif = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbMotif.sizePolicy().hasHeightForWidth())
        self.cmbMotif.setSizePolicy(sizePolicy)
        self.cmbMotif.setObjectName("cmbMotif")
        self.horizontalLayout_21.addWidget(self.cmbMotif)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem3)
        self.horizontalLayout_28.addLayout(self.horizontalLayout_21)
        self.verticalLayout_8.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_25.addWidget(self.label_26)
        self.tbvOperateur = QtWidgets.QTableView(self.groupBox_3)
        self.tbvOperateur.setObjectName("tbvOperateur")
        self.horizontalLayout_25.addWidget(self.tbvOperateur)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btnAjoutOperateur = QtWidgets.QPushButton(self.groupBox_3)
        self.btnAjoutOperateur.setMaximumSize(QtCore.QSize(25, 16777215))
        self.btnAjoutOperateur.setObjectName("btnAjoutOperateur")
        self.verticalLayout_10.addWidget(self.btnAjoutOperateur)
        self.btnSuppOperateur = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSuppOperateur.setMaximumSize(QtCore.QSize(25, 16777215))
        self.btnSuppOperateur.setObjectName("btnSuppOperateur")
        self.verticalLayout_10.addWidget(self.btnSuppOperateur)
        self.horizontalLayout_25.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_32.addWidget(self.label_28)
        self.tbvMoa = QtWidgets.QTableView(self.groupBox_3)
        self.tbvMoa.setObjectName("tbvMoa")
        self.horizontalLayout_32.addWidget(self.tbvMoa)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btnAjoutMoa = QtWidgets.QPushButton(self.groupBox_3)
        self.btnAjoutMoa.setMaximumSize(QtCore.QSize(25, 16777215))
        self.btnAjoutMoa.setObjectName("btnAjoutMoa")
        self.verticalLayout_9.addWidget(self.btnAjoutMoa)
        self.btnSuppMoa = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSuppMoa.setMaximumSize(QtCore.QSize(25, 16777215))
        self.btnSuppMoa.setObjectName("btnSuppMoa")
        self.verticalLayout_9.addWidget(self.btnSuppMoa)
        self.horizontalLayout_32.addLayout(self.verticalLayout_9)
        self.verticalLayout_8.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.spnLongueur = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.spnLongueur.setMaximum(9999.99)
        self.spnLongueur.setObjectName("spnLongueur")
        self.horizontalLayout_12.addWidget(self.spnLongueur)
        self.horizontalLayout_34.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.spnLargeur = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.spnLargeur.setDecimals(1)
        self.spnLargeur.setMaximum(200.0)
        self.spnLargeur.setObjectName("spnLargeur")
        self.horizontalLayout_14.addWidget(self.spnLargeur)
        self.horizontalLayout_34.addLayout(self.horizontalLayout_14)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.spnSurfacePeche = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.spnSurfacePeche.setMaximum(9999.99)
        self.spnSurfacePeche.setObjectName("spnSurfacePeche")
        self.horizontalLayout_15.addWidget(self.spnSurfacePeche)
        self.horizontalLayout_35.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.spnProfondeur = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.spnProfondeur.setMaximum(9999.99)
        self.spnProfondeur.setObjectName("spnProfondeur")
        self.horizontalLayout_13.addWidget(self.spnProfondeur)
        self.horizontalLayout_35.addLayout(self.horizontalLayout_13)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_18.addWidget(self.label_19)
        self.spnPente = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.spnPente.setMaximum(99999.99)
        self.spnPente.setObjectName("spnPente")
        self.horizontalLayout_18.addWidget(self.spnPente)
        self.btnPente = QtWidgets.QPushButton(self.groupBox_3)
        self.btnPente.setObjectName("btnPente")
        self.horizontalLayout_18.addWidget(self.btnPente)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_17.addWidget(self.label_18)
        self.txtObservation = QtWidgets.QTextEdit(self.groupBox_3)
        self.txtObservation.setMinimumSize(QtCore.QSize(360, 0))
        self.txtObservation.setObjectName("txtObservation")
        self.horizontalLayout_17.addWidget(self.txtObservation)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnExcel = QtWidgets.QPushButton(self.groupBox_3)
        self.btnExcel.setObjectName("btnExcel")
        self.horizontalLayout_2.addWidget(self.btnExcel)
        self.btnAjoutFiche = QtWidgets.QPushButton(self.groupBox_3)
        self.btnAjoutFiche.setMinimumSize(QtCore.QSize(65, 0))
        self.btnAjoutFiche.setMaximumSize(QtCore.QSize(65, 20))
        self.btnAjoutFiche.setObjectName("btnAjoutFiche")
        self.horizontalLayout_2.addWidget(self.btnAjoutFiche)
        self.btnRetraitFiche = QtWidgets.QPushButton(self.groupBox_3)
        self.btnRetraitFiche.setMinimumSize(QtCore.QSize(65, 0))
        self.btnRetraitFiche.setMaximumSize(QtCore.QSize(65, 20))
        self.btnRetraitFiche.setObjectName("btnRetraitFiche")
        self.horizontalLayout_2.addWidget(self.btnRetraitFiche)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.chkNtt = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkNtt.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkNtt.setObjectName("chkNtt")
        self.horizontalLayout_30.addWidget(self.chkNtt)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_19.addWidget(self.label_20)
        self.spnNtt = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.spnNtt.setMaximum(99.99)
        self.spnNtt.setObjectName("spnNtt")
        self.horizontalLayout_19.addWidget(self.spnNtt)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_19)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_26.addWidget(self.label_27)
        self.spnIpr = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.spnIpr.setDecimals(3)
        self.spnIpr.setMaximum(999.99)
        self.spnIpr.setObjectName("spnIpr")
        self.horizontalLayout_26.addWidget(self.spnIpr)
        self.horizontalLayout_31.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_29.addWidget(self.label_17)
        self.cmbIpr = QtWidgets.QComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbIpr.sizePolicy().hasHeightForWidth())
        self.cmbIpr.setSizePolicy(sizePolicy)
        self.cmbIpr.setMinimumSize(QtCore.QSize(100, 0))
        self.cmbIpr.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cmbIpr.setObjectName("cmbIpr")
        self.horizontalLayout_29.addWidget(self.cmbIpr)
        self.horizontalLayout_31.addLayout(self.horizontalLayout_29)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_31)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.tbvEspece = QtWidgets.QTableView(self.groupBox_4)
        self.tbvEspece.setObjectName("tbvEspece")
        self.verticalLayout_6.addWidget(self.tbvEspece)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btnAjoutPoisson = QtWidgets.QPushButton(self.groupBox_4)
        self.btnAjoutPoisson.setMaximumSize(QtCore.QSize(25, 16777215))
        self.btnAjoutPoisson.setObjectName("btnAjoutPoisson")
        self.verticalLayout_11.addWidget(self.btnAjoutPoisson)
        self.btnSuppPoisson = QtWidgets.QPushButton(self.groupBox_4)
        self.btnSuppPoisson.setMaximumSize(QtCore.QSize(25, 16777215))
        self.btnSuppPoisson.setObjectName("btnSuppPoisson")
        self.verticalLayout_11.addWidget(self.btnSuppPoisson)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.btnPrec = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnPrec.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnPrec.setObjectName("btnPrec")
        self.horizontalLayout_39.addWidget(self.btnPrec)
        self.btnPremier = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnPremier.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnPremier.setObjectName("btnPremier")
        self.horizontalLayout_39.addWidget(self.btnPremier)
        self.btnDernier = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnDernier.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnDernier.setObjectName("btnDernier")
        self.horizontalLayout_39.addWidget(self.btnDernier)
        self.btnSuiv = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnSuiv.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSuiv.setObjectName("btnSuiv")
        self.horizontalLayout_39.addWidget(self.btnSuiv)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.btnZoom = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnZoom.setEnabled(True)
        self.btnZoom.setMinimumSize(QtCore.QSize(50, 36))
        self.btnZoom.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnZoom.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnZoom.setIcon(icon)
        self.btnZoom.setObjectName("btnZoom")
        self.horizontalLayout_40.addWidget(self.btnZoom)
        self.btnSelection = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnSelection.setEnabled(True)
        self.btnSelection.setMinimumSize(QtCore.QSize(50, 36))
        self.btnSelection.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnSelection.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelection.setIcon(icon1)
        self.btnSelection.setObjectName("btnSelection")
        self.horizontalLayout_40.addWidget(self.btnSelection)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_40)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_38)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.btnNouveau = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btnNouveau.setFont(font)
        self.btnNouveau.setStyleSheet("color: rgb(0, 170, 0);")
        self.btnNouveau.setObjectName("btnNouveau")
        self.horizontalLayout_37.addWidget(self.btnNouveau)
        self.btnModif = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btnModif.setFont(font)
        self.btnModif.setStyleSheet("color: rgb(85, 0, 255);")
        self.btnModif.setObjectName("btnModif")
        self.horizontalLayout_37.addWidget(self.btnModif)
        self.btnSupprimer = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btnSupprimer.setFont(font)
        self.btnSupprimer.setStyleSheet("color: rgb(231, 0, 0);")
        self.btnSupprimer.setObjectName("btnSupprimer")
        self.horizontalLayout_37.addWidget(self.btnSupprimer)
        self.btnEnregistrer = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnEnregistrer.setObjectName("btnEnregistrer")
        self.horizontalLayout_37.addWidget(self.btnEnregistrer)
        self.btnAnnuler = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.btnAnnuler.setObjectName("btnAnnuler")
        self.horizontalLayout_37.addWidget(self.btnAnnuler)
        self.verticalLayout.addLayout(self.horizontalLayout_37)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_33.addWidget(self.scrollArea)
        dwcPecheMainForm.setWidget(self.dwc_peche_elec_form)

        self.retranslateUi(dwcPecheMainForm)
        QtCore.QMetaObject.connectSlotsByName(dwcPecheMainForm)

    def retranslateUi(self, dwcPecheMainForm):
        _translate = QtCore.QCoreApplication.translate
        dwcPecheMainForm.setWindowTitle(_translate("dwcPecheMainForm", "Gedopi - Pêche électrique"))
        self.btnFiltreCartoManuel.setText(_translate("dwcPecheMainForm", "Filtre carto manuel"))
        self.chkFiltreCartoAuto.setText(_translate("dwcPecheMainForm", "filtre carto automatique"))
        self.btnFiltreAttributaire.setText(_translate("dwcPecheMainForm", "Filtre attributaire"))
        self.btnDeleteFiltrage.setText(_translate("dwcPecheMainForm", "Suppression filtrage"))
        self.chkVerrouAuto.setText(_translate("dwcPecheMainForm", "* Verrouillage des champs automatiques"))
        self.chkVerrouModif.setText(_translate("dwcPecheMainForm", "Verrouillage modification"))
        self.groupBox.setTitle(_translate("dwcPecheMainForm", "Station"))
        self.lbl_commune.setText(_translate("dwcPecheMainForm", "Rivière :"))
        self.btnStation.setText(_translate("dwcPecheMainForm", "Fiche complète"))
        self.lbl_section.setText(_translate("dwcPecheMainForm", "<html><head/><body><p>Station <span style=\" font-size:7pt;\">(ID ; Nom)</span> :</p></body></html>"))
        self.groupBox_3.setTitle(_translate("dwcPecheMainForm", "Information sur la pêche"))
        self.label_8.setText(_translate("dwcPecheMainForm", "Code opération :"))
        self.label_21.setText(_translate("dwcPecheMainForm", "Date :"))
        self.chkComplete.setText(_translate("dwcPecheMainForm", "Pêche complète :"))
        self.label_10.setText(_translate("dwcPecheMainForm", "Nombre d\'anode :"))
        self.label_23.setText(_translate("dwcPecheMainForm", "Condition :"))
        self.label_22.setText(_translate("dwcPecheMainForm", "Motif :"))
        self.label_26.setText(_translate("dwcPecheMainForm", "Opérateur(s) :"))
        self.btnAjoutOperateur.setText(_translate("dwcPecheMainForm", "+"))
        self.btnSuppOperateur.setText(_translate("dwcPecheMainForm", "-"))
        self.label_28.setText(_translate("dwcPecheMainForm", "Maître(s) d\'ouvrage :"))
        self.btnAjoutMoa.setText(_translate("dwcPecheMainForm", "+"))
        self.btnSuppMoa.setText(_translate("dwcPecheMainForm", "-"))
        self.label_13.setText(_translate("dwcPecheMainForm", "Longueur prospectée (m) :"))
        self.label_15.setText(_translate("dwcPecheMainForm", "Largeur moyenne (m) :"))
        self.label_16.setText(_translate("dwcPecheMainForm", "* Surface pêchée (m²) :"))
        self.label_14.setText(_translate("dwcPecheMainForm", "Profondeur moyenne (cm) :"))
        self.label_19.setText(_translate("dwcPecheMainForm", "* Pente (%) :"))
        self.btnPente.setText(_translate("dwcPecheMainForm", "Calcul de la pente (2 clics)"))
        self.label_18.setText(_translate("dwcPecheMainForm", "Observation :"))
        self.btnExcel.setText(_translate("dwcPecheMainForm", "Fiche Externe"))
        self.btnAjoutFiche.setText(_translate("dwcPecheMainForm", "Lier fiche"))
        self.btnRetraitFiche.setText(_translate("dwcPecheMainForm", "Délier fiche"))
        self.groupBox_4.setTitle(_translate("dwcPecheMainForm", "Résultats"))
        self.chkNtt.setText(_translate("dwcPecheMainForm", "NTT réel :"))
        self.label_20.setText(_translate("dwcPecheMainForm", "Valeur NTT :"))
        self.label_27.setText(_translate("dwcPecheMainForm", "Valeur IPR :"))
        self.label_17.setText(_translate("dwcPecheMainForm", "Correspondance IPR :"))
        self.label_9.setText(_translate("dwcPecheMainForm", "Espèce(s) pêchée(s) :"))
        self.btnAjoutPoisson.setText(_translate("dwcPecheMainForm", "+"))
        self.btnSuppPoisson.setText(_translate("dwcPecheMainForm", "-"))
        self.btnPrec.setText(_translate("dwcPecheMainForm", "<"))
        self.btnPremier.setText(_translate("dwcPecheMainForm", "<<"))
        self.btnDernier.setText(_translate("dwcPecheMainForm", ">>"))
        self.btnSuiv.setText(_translate("dwcPecheMainForm", ">"))
        self.btnZoom.setToolTip(_translate("dwcPecheMainForm", "Zoomer sur l\'objet"))
        self.btnSelection.setToolTip(_translate("dwcPecheMainForm", "Sélectionner l\'objet"))
        self.btnNouveau.setText(_translate("dwcPecheMainForm", "Nouveau"))
        self.btnModif.setText(_translate("dwcPecheMainForm", "Enreg. Modif"))
        self.btnSupprimer.setText(_translate("dwcPecheMainForm", "Supprimer"))
        self.btnEnregistrer.setText(_translate("dwcPecheMainForm", "Enregistrer"))
        self.btnAnnuler.setText(_translate("dwcPecheMainForm", "Abandonner"))

import ressourceGedopi_rc
