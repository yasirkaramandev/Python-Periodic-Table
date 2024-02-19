# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard
import json
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-image: url(Assets/Frame 1 jpg.jpg);\n"
"")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.widget.setStyleSheet("QWidget{\n"
"    background-image: url();\n"
"}")
        self.widget.setObjectName("widget")
        self.H = QtWidgets.QPushButton(self.widget)
        self.H.setGeometry(QtCore.QRect(342, 30, 66, 67))
        self.H.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.H.setText("")
        self.H.setObjectName("H")
        self.H.clicked.connect(lambda x: self.dataAnalyze("H"))
        self.Li = QtWidgets.QPushButton(self.widget)
        self.Li.setGeometry(QtCore.QRect(342, 103, 66, 67))
        self.Li.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Li.setText("")
        self.Li.setObjectName("Li")
        self.Li.clicked.connect(lambda x: self.dataAnalyze("Li"))
        self.Na = QtWidgets.QPushButton(self.widget)
        self.Na.setGeometry(QtCore.QRect(342, 176, 66, 67))
        self.Na.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Na.setText("")
        self.Na.setObjectName("Na")
        self.Na.clicked.connect(lambda x: self.dataAnalyze("Na"))
        self.K = QtWidgets.QPushButton(self.widget)
        self.K.setGeometry(QtCore.QRect(342, 249, 66, 67))
        self.K.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.K.setText("")
        self.K.setObjectName("K")
        self.K.clicked.connect(lambda x: self.dataAnalyze("K"))
        self.Rb = QtWidgets.QPushButton(self.widget)
        self.Rb.setGeometry(QtCore.QRect(342, 322, 66, 67))
        self.Rb.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Rb.setText("")
        self.Rb.setObjectName("Rb")
        self.Rb.clicked.connect(lambda x: self.dataAnalyze("Rb"))
        self.Cs = QtWidgets.QPushButton(self.widget)
        self.Cs.setGeometry(QtCore.QRect(342, 395, 66, 67))
        self.Cs.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Cs.setText("")
        self.Cs.setObjectName("Cs")
        self.Cs.clicked.connect(lambda x: self.dataAnalyze("Cs"))
        self.Be = QtWidgets.QPushButton(self.widget)
        self.Be.setGeometry(QtCore.QRect(415, 103, 66, 67))
        self.Be.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Be.setText("")
        self.Be.setObjectName("Be")
        self.Be.clicked.connect(lambda x: self.dataAnalyze("Be"))
        self.Mg = QtWidgets.QPushButton(self.widget)
        self.Mg.setGeometry(QtCore.QRect(415, 176, 66, 67))
        self.Mg.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Mg.setText("")
        self.Mg.setObjectName("Mg")
        self.Mg.clicked.connect(lambda x: self.dataAnalyze("Mg"))
        self.Ca = QtWidgets.QPushButton(self.widget)
        self.Ca.setGeometry(QtCore.QRect(415, 249, 66, 67))
        self.Ca.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ca.setText("")
        self.Ca.setObjectName("Ca")
        self.Ca.clicked.connect(lambda x: self.dataAnalyze("Ca"))
        self.Sr = QtWidgets.QPushButton(self.widget)
        self.Sr.setGeometry(QtCore.QRect(415, 322, 66, 67))
        self.Sr.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Sr.setText("")
        self.Sr.setObjectName("Sr")
        self.Sr.clicked.connect(lambda x: self.dataAnalyze("Sr"))
        self.Ba = QtWidgets.QPushButton(self.widget)
        self.Ba.setGeometry(QtCore.QRect(415, 395, 66, 67))
        self.Ba.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ba.setText("")
        self.Ba.setObjectName("Ba")
        self.Ba.clicked.connect(lambda x: self.dataAnalyze("Ba"))
        self.Sc = QtWidgets.QPushButton(self.widget)
        self.Sc.setGeometry(QtCore.QRect(489, 249, 66, 67))
        self.Sc.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Sc.setText("")
        self.Sc.setObjectName("Sc")
        self.Sc.clicked.connect(lambda x: self.dataAnalyze("Sc"))
        self.Ti = QtWidgets.QPushButton(self.widget)
        self.Ti.setGeometry(QtCore.QRect(562, 249, 66, 67))
        self.Ti.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ti.setText("")
        self.Ti.setObjectName("Ti")
        self.Ti.clicked.connect(lambda x: self.dataAnalyze("Ti"))
        self.V = QtWidgets.QPushButton(self.widget)
        self.V.setGeometry(QtCore.QRect(635, 249, 66, 67))
        self.V.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.V.setText("")
        self.V.setObjectName("V")
        self.V.clicked.connect(lambda x: self.dataAnalyze("V"))
        self.Cr = QtWidgets.QPushButton(self.widget)
        self.Cr.setGeometry(QtCore.QRect(708, 249, 66, 67))
        self.Cr.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Cr.setText("")
        self.Cr.setObjectName("Cr")
        self.Cr.clicked.connect(lambda x: self.dataAnalyze("Cr"))
        self.Mn = QtWidgets.QPushButton(self.widget)
        self.Mn.setGeometry(QtCore.QRect(781, 249, 66, 67))
        self.Mn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Mn.setText("")
        self.Mn.setObjectName("Mn")
        self.Mn.clicked.connect(lambda x: self.dataAnalyze("Mn"))
        self.Fe = QtWidgets.QPushButton(self.widget)
        self.Fe.setGeometry(QtCore.QRect(854, 249, 66, 67))
        self.Fe.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Fe.setText("")
        self.Fe.setObjectName("Fe")
        self.Fe.clicked.connect(lambda x: self.dataAnalyze("Fe"))
        self.Co = QtWidgets.QPushButton(self.widget)
        self.Co.setGeometry(QtCore.QRect(926, 249, 66, 67))
        self.Co.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Co.setText("")
        self.Co.setObjectName("Co")
        self.Co.clicked.connect(lambda x: self.dataAnalyze("Co"))
        self.Ni = QtWidgets.QPushButton(self.widget)
        self.Ni.setGeometry(QtCore.QRect(1000, 249, 66, 67))
        self.Ni.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ni.setText("")
        self.Ni.setObjectName("Ni")
        self.Ni.clicked.connect(lambda x: self.dataAnalyze("Ni"))
        self.Cu = QtWidgets.QPushButton(self.widget)
        self.Cu.setGeometry(QtCore.QRect(1073, 249, 66, 67))
        self.Cu.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Cu.setText("")
        self.Cu.setObjectName("Cu")
        self.Cu.clicked.connect(lambda x: self.dataAnalyze("Cu"))
        self.Zn = QtWidgets.QPushButton(self.widget)
        self.Zn.setGeometry(QtCore.QRect(1146, 249, 66, 67))
        self.Zn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Zn.setText("")
        self.Zn.setObjectName("Zn")
        self.Zn.clicked.connect(lambda x: self.dataAnalyze("Zn"))
        self.Ga = QtWidgets.QPushButton(self.widget)
        self.Ga.setGeometry(QtCore.QRect(1219, 249, 66, 67))
        self.Ga.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ga.setText("")
        self.Ga.setObjectName("Ga")
        self.Ga.clicked.connect(lambda x: self.dataAnalyze("Ga"))
        self.Ge = QtWidgets.QPushButton(self.widget)
        self.Ge.setGeometry(QtCore.QRect(1291, 249, 66, 67))
        self.Ge.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ge.setText("")
        self.Ge.setObjectName("Ge")
        self.Ge.clicked.connect(lambda x: self.dataAnalyze("Ge"))
        self.As = QtWidgets.QPushButton(self.widget)
        self.As.setGeometry(QtCore.QRect(1365, 249, 66, 67))
        self.As.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.As.setText("")
        self.As.setObjectName("As")
        self.As.clicked.connect(lambda x: self.dataAnalyze("As"))
        self.Se = QtWidgets.QPushButton(self.widget)
        self.Se.setGeometry(QtCore.QRect(1438, 249, 66, 67))
        self.Se.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Se.setText("")
        self.Se.setObjectName("Se")
        self.Se.clicked.connect(lambda x: self.dataAnalyze("Se"))
        self.Br = QtWidgets.QPushButton(self.widget)
        self.Br.setGeometry(QtCore.QRect(1510, 249, 66, 67))
        self.Br.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Br.setText("")
        self.Br.setObjectName("Br")
        self.Br.clicked.connect(lambda x: self.dataAnalyze("Br"))
        self.Kr = QtWidgets.QPushButton(self.widget)
        self.Kr.setGeometry(QtCore.QRect(1584, 249, 66, 67))
        self.Kr.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Kr.setText("")
        self.Kr.setObjectName("Kr")
        self.Kr.clicked.connect(lambda x: self.dataAnalyze("Kr"))
        self.Ar = QtWidgets.QPushButton(self.widget)
        self.Ar.setGeometry(QtCore.QRect(1585, 176, 66, 67))
        self.Ar.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ar.setText("")
        self.Ar.setObjectName("Ar")
        self.Ar.clicked.connect(lambda x: self.dataAnalyze("Ar"))
        self.S = QtWidgets.QPushButton(self.widget)
        self.S.setGeometry(QtCore.QRect(1438, 176, 66, 67))
        self.S.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.S.setText("")
        self.S.setObjectName("S")
        self.S.clicked.connect(lambda x: self.dataAnalyze("S"))
        self.P = QtWidgets.QPushButton(self.widget)
        self.P.setGeometry(QtCore.QRect(1365, 176, 66, 67))
        self.P.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.P.setText("")
        self.P.setObjectName("P")
        self.P.clicked.connect(lambda x: self.dataAnalyze("P"))
        self.Si = QtWidgets.QPushButton(self.widget)
        self.Si.setGeometry(QtCore.QRect(1290, 176, 66, 67))
        self.Si.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Si.setText("")
        self.Si.setObjectName("Si")
        self.Si.clicked.connect(lambda x: self.dataAnalyze("Si"))
        self.Cl = QtWidgets.QPushButton(self.widget)
        self.Cl.setGeometry(QtCore.QRect(1510, 176, 66, 67))
        self.Cl.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Cl.setText("")
        self.Cl.setObjectName("Cl")
        self.Cl.clicked.connect(lambda x: self.dataAnalyze("Cl"))
        self.Al = QtWidgets.QPushButton(self.widget)
        self.Al.setGeometry(QtCore.QRect(1218, 176, 66, 67))
        self.Al.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Al.setText("")
        self.Al.setObjectName("Al")
        self.Al.clicked.connect(lambda x: self.dataAnalyze("Al"))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1220, 100, 433, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.B = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.B.setMinimumSize(QtCore.QSize(66, 67))
        self.B.setMaximumSize(QtCore.QSize(66, 67))
        self.B.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.B.setText("")
        self.B.setObjectName("B")
        self.B.clicked.connect(lambda x: self.dataAnalyze("B"))
        self.horizontalLayout.addWidget(self.B)
        self.C = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.C.setMinimumSize(QtCore.QSize(66, 67))
        self.C.setMaximumSize(QtCore.QSize(66, 67))
        self.C.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.C.setText("")
        self.C.setObjectName("C")
        self.C.clicked.connect(lambda x: self.dataAnalyze("C"))
        self.horizontalLayout.addWidget(self.C)
        self.N = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.N.setMinimumSize(QtCore.QSize(66, 67))
        self.N.setMaximumSize(QtCore.QSize(66, 67))
        self.N.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.N.setText("")
        self.N.setObjectName("N")
        self.N.clicked.connect(lambda x: self.dataAnalyze("N"))
        self.horizontalLayout.addWidget(self.N)
        self.O = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.O.setMinimumSize(QtCore.QSize(66, 67))
        self.O.setMaximumSize(QtCore.QSize(66, 67))
        self.O.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.O.setText("")
        self.O.setObjectName("O")
        self.O.clicked.connect(lambda x: self.dataAnalyze("O"))
        self.horizontalLayout.addWidget(self.O)
        self.F = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.F.setMinimumSize(QtCore.QSize(66, 67))
        self.F.setMaximumSize(QtCore.QSize(66, 67))
        self.F.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.F.setText("")
        self.F.setObjectName("F")
        self.F.clicked.connect(lambda x: self.dataAnalyze("F"))
        self.horizontalLayout.addWidget(self.F)
        self.Ne = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Ne.setMinimumSize(QtCore.QSize(66, 67))
        self.Ne.setMaximumSize(QtCore.QSize(66, 67))
        self.Ne.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ne.setText("")
        self.Ne.setObjectName("Ne")
        self.Ne.clicked.connect(lambda x: self.dataAnalyze("Ne"))
        self.horizontalLayout.addWidget(self.Ne)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(490, 320, 287, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Y = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Y.setMinimumSize(QtCore.QSize(66, 67))
        self.Y.setMaximumSize(QtCore.QSize(66, 67))
        self.Y.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Y.setText("")
        self.Y.setObjectName("Y")
        self.Y.clicked.connect(lambda x: self.dataAnalyze("Y"))
        self.horizontalLayout_2.addWidget(self.Y)
        self.Zr = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Zr.setMinimumSize(QtCore.QSize(66, 67))
        self.Zr.setMaximumSize(QtCore.QSize(66, 67))
        self.Zr.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Zr.setText("")
        self.Zr.setObjectName("Zr")
        self.Zr.clicked.connect(lambda x: self.dataAnalyze("Zr"))
        self.horizontalLayout_2.addWidget(self.Zr)
        self.Nb = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Nb.setMinimumSize(QtCore.QSize(66, 67))
        self.Nb.setMaximumSize(QtCore.QSize(66, 67))
        self.Nb.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Nb.setText("")
        self.Nb.setObjectName("Nb")
        self.Nb.clicked.connect(lambda x: self.dataAnalyze("Nb"))
        self.horizontalLayout_2.addWidget(self.Nb)
        self.Mo = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Mo.setMinimumSize(QtCore.QSize(66, 67))
        self.Mo.setMaximumSize(QtCore.QSize(66, 67))
        self.Mo.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Mo.setText("")
        self.Mo.setObjectName("Mo")
        self.Mo.clicked.connect(lambda x: self.dataAnalyze("Mo"))
        self.horizontalLayout_2.addWidget(self.Mo)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(850, 320, 811, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Ru = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Ru.setMinimumSize(QtCore.QSize(66, 67))
        self.Ru.setMaximumSize(QtCore.QSize(66, 67))
        self.Ru.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ru.setText("")
        self.Ru.setObjectName("Ru")
        self.Ru.clicked.connect(lambda x: self.dataAnalyze("Ru"))
        self.horizontalLayout_3.addWidget(self.Ru)
        self.Rh = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Rh.setMinimumSize(QtCore.QSize(66, 67))
        self.Rh.setMaximumSize(QtCore.QSize(66, 67))
        self.Rh.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Rh.setText("")
        self.Rh.setObjectName("Rh")
        self.Rh.clicked.connect(lambda x: self.dataAnalyze("Rh"))
        self.horizontalLayout_3.addWidget(self.Rh)
        self.Pd = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Pd.setMinimumSize(QtCore.QSize(66, 67))
        self.Pd.setMaximumSize(QtCore.QSize(66, 67))
        self.Pd.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Pd.setText("")
        self.Pd.setObjectName("Pd")
        self.Pd.clicked.connect(lambda x: self.dataAnalyze("Pd"))
        self.horizontalLayout_3.addWidget(self.Pd)
        self.Ag = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Ag.setMinimumSize(QtCore.QSize(66, 67))
        self.Ag.setMaximumSize(QtCore.QSize(66, 67))
        self.Ag.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ag.setText("")
        self.Ag.setObjectName("Ag")
        self.Ag.clicked.connect(lambda x: self.dataAnalyze("Ag"))
        self.horizontalLayout_3.addWidget(self.Ag)
        self.Cd = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Cd.setMinimumSize(QtCore.QSize(66, 67))
        self.Cd.setMaximumSize(QtCore.QSize(66, 67))
        self.Cd.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Cd.setText("")
        self.Cd.setObjectName("Cd")
        self.Cd.clicked.connect(lambda x: self.dataAnalyze("Cd"))
        self.horizontalLayout_3.addWidget(self.Cd)
        self.In = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.In.setMinimumSize(QtCore.QSize(66, 67))
        self.In.setMaximumSize(QtCore.QSize(66, 67))
        self.In.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.In.setText("")
        self.In.setObjectName("In")
        self.In.clicked.connect(lambda x: self.dataAnalyze("In"))
        self.horizontalLayout_3.addWidget(self.In)
        self.Sn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Sn.setMinimumSize(QtCore.QSize(66, 67))
        self.Sn.setMaximumSize(QtCore.QSize(66, 67))
        self.Sn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Sn.setText("")
        self.Sn.setObjectName("Sn")
        self.Sn.clicked.connect(lambda x: self.dataAnalyze("Sn"))
        self.horizontalLayout_3.addWidget(self.Sn)
        self.Sb = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Sb.setMinimumSize(QtCore.QSize(66, 67))
        self.Sb.setMaximumSize(QtCore.QSize(66, 67))
        self.Sb.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Sb.setText("")
        self.Sb.setObjectName("Sb")
        self.Sb.clicked.connect(lambda x: self.dataAnalyze("Sb"))
        self.horizontalLayout_3.addWidget(self.Sb)
        self.Te = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Te.setMinimumSize(QtCore.QSize(66, 67))
        self.Te.setMaximumSize(QtCore.QSize(66, 67))
        self.Te.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Te.setText("")
        self.Te.setObjectName("Te")
        self.Te.clicked.connect(lambda x: self.dataAnalyze("Te"))
        self.horizontalLayout_3.addWidget(self.Te)
        self.I = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.I.setMinimumSize(QtCore.QSize(66, 67))
        self.I.setMaximumSize(QtCore.QSize(66, 67))
        self.I.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.I.setText("")
        self.I.setObjectName("I")
        self.I.clicked.connect(lambda x: self.dataAnalyze("I"))
        self.horizontalLayout_3.addWidget(self.I)
        self.Xe = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.Xe.setMinimumSize(QtCore.QSize(66, 67))
        self.Xe.setMaximumSize(QtCore.QSize(66, 67))
        self.Xe.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Xe.setText("")
        self.Xe.setObjectName("Xe")
        self.Xe.clicked.connect(lambda x: self.dataAnalyze("Xe"))
        self.horizontalLayout_3.addWidget(self.Xe)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(560, 390, 881, 81))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Hf = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Hf.setMinimumSize(QtCore.QSize(66, 67))
        self.Hf.setMaximumSize(QtCore.QSize(66, 67))
        self.Hf.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Hf.setText("")
        self.Hf.setObjectName("Hf")
        self.Hf.clicked.connect(lambda x: self.dataAnalyze("Hf"))
        self.horizontalLayout_4.addWidget(self.Hf)
        self.Ta = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Ta.setMinimumSize(QtCore.QSize(66, 67))
        self.Ta.setMaximumSize(QtCore.QSize(66, 67))
        self.Ta.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ta.setText("")
        self.Ta.setObjectName("Ta")
        self.Ta.clicked.connect(lambda x: self.dataAnalyze("Ta"))
        self.horizontalLayout_4.addWidget(self.Ta)
        self.W = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.W.setMinimumSize(QtCore.QSize(66, 67))
        self.W.setMaximumSize(QtCore.QSize(66, 67))
        self.W.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.W.setText("")
        self.W.setObjectName("W")
        self.W.clicked.connect(lambda x: self.dataAnalyze("W"))
        self.horizontalLayout_4.addWidget(self.W)
        self.Re = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Re.setMinimumSize(QtCore.QSize(66, 67))
        self.Re.setMaximumSize(QtCore.QSize(66, 67))
        self.Re.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Re.setText("")
        self.Re.setObjectName("Re")
        self.Re.clicked.connect(lambda x: self.dataAnalyze("Re"))
        self.horizontalLayout_4.addWidget(self.Re)
        self.Os = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Os.setMinimumSize(QtCore.QSize(66, 67))
        self.Os.setMaximumSize(QtCore.QSize(66, 67))
        self.Os.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Os.setText("")
        self.Os.setObjectName("Os")
        self.Os.clicked.connect(lambda x: self.dataAnalyze("Os"))
        self.horizontalLayout_4.addWidget(self.Os)
        self.Ir = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Ir.setMinimumSize(QtCore.QSize(66, 67))
        self.Ir.setMaximumSize(QtCore.QSize(66, 67))
        self.Ir.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ir.setText("")
        self.Ir.setObjectName("Ir")
        self.Ir.clicked.connect(lambda x: self.dataAnalyze("Ir"))
        self.horizontalLayout_4.addWidget(self.Ir)
        self.Pt = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Pt.setMinimumSize(QtCore.QSize(66, 67))
        self.Pt.setMaximumSize(QtCore.QSize(66, 67))
        self.Pt.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Pt.setText("")
        self.Pt.setObjectName("Pt")
        self.Pt.clicked.connect(lambda x: self.dataAnalyze("Pt"))
        self.horizontalLayout_4.addWidget(self.Pt)
        self.Au = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Au.setMinimumSize(QtCore.QSize(66, 67))
        self.Au.setMaximumSize(QtCore.QSize(66, 67))
        self.Au.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Au.setText("")
        self.Au.setObjectName("Au")
        self.Au.clicked.connect(lambda x: self.dataAnalyze("Au"))
        self.horizontalLayout_4.addWidget(self.Au)
        self.Hg = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Hg.setMinimumSize(QtCore.QSize(66, 67))
        self.Hg.setMaximumSize(QtCore.QSize(66, 67))
        self.Hg.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Hg.setText("")
        self.Hg.setObjectName("Hg")
        self.Hg.clicked.connect(lambda x: self.dataAnalyze("Hg"))
        self.horizontalLayout_4.addWidget(self.Hg)
        self.Tl = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Tl.setMinimumSize(QtCore.QSize(66, 67))
        self.Tl.setMaximumSize(QtCore.QSize(66, 67))
        self.Tl.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Tl.setText("")
        self.Tl.setObjectName("Tl")
        self.Tl.clicked.connect(lambda x: self.dataAnalyze("Tl"))
        self.horizontalLayout_4.addWidget(self.Tl)
        self.Pb = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Pb.setMinimumSize(QtCore.QSize(66, 67))
        self.Pb.setMaximumSize(QtCore.QSize(66, 67))
        self.Pb.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Pb.setText("")
        self.Pb.setObjectName("Pb")
        self.Pb.clicked.connect(lambda x: self.dataAnalyze("Pb"))
        self.horizontalLayout_4.addWidget(self.Pb)
        self.Bi = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.Bi.setMinimumSize(QtCore.QSize(66, 67))
        self.Bi.setMaximumSize(QtCore.QSize(66, 67))
        self.Bi.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Bi.setText("")
        self.Bi.setObjectName("Bi")
        self.Bi.clicked.connect(lambda x: self.dataAnalyze("Bi"))
        self.horizontalLayout_4.addWidget(self.Bi)
        self.He = QtWidgets.QPushButton(self.widget)
        self.He.setGeometry(QtCore.QRect(1584, 30, 66, 67))
        self.He.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.He.setText("")
        self.He.setObjectName("He")
        self.He.clicked.connect(lambda x: self.dataAnalyze("He"))
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(560, 460, 1091, 81))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.RF = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.RF.setMinimumSize(QtCore.QSize(66, 67))
        self.RF.setMaximumSize(QtCore.QSize(66, 67))
        self.RF.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.RF.setText("")
        self.RF.setObjectName("RF")
        self.RF.clicked.connect(lambda x: self.dataAnalyze("Rf"))
        self.horizontalLayout_5.addWidget(self.RF)
        self.Db = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Db.setMinimumSize(QtCore.QSize(66, 67))
        self.Db.setMaximumSize(QtCore.QSize(66, 67))
        self.Db.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Db.setText("")
        self.Db.setObjectName("Db")
        self.Db.clicked.connect(lambda x: self.dataAnalyze("Db"))
        self.horizontalLayout_5.addWidget(self.Db)
        self.Sg = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Sg.setMinimumSize(QtCore.QSize(66, 67))
        self.Sg.setMaximumSize(QtCore.QSize(66, 67))
        self.Sg.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Sg.setText("")
        self.Sg.setObjectName("Sg")
        self.Sg.clicked.connect(lambda x: self.dataAnalyze("Sg"))
        self.horizontalLayout_5.addWidget(self.Sg)
        self.Bh = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Bh.setMinimumSize(QtCore.QSize(66, 67))
        self.Bh.setMaximumSize(QtCore.QSize(66, 67))
        self.Bh.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Bh.setText("")
        self.Bh.setObjectName("Bh")
        self.Bh.clicked.connect(lambda x: self.dataAnalyze("Bh"))
        self.horizontalLayout_5.addWidget(self.Bh)
        self.Hs = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Hs.setMinimumSize(QtCore.QSize(66, 67))
        self.Hs.setMaximumSize(QtCore.QSize(66, 67))
        self.Hs.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Hs.setText("")
        self.Hs.setObjectName("Hs")
        self.Hs.clicked.connect(lambda x: self.dataAnalyze("Hs"))
        self.horizontalLayout_5.addWidget(self.Hs)
        self.Mt = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Mt.setMinimumSize(QtCore.QSize(66, 67))
        self.Mt.setMaximumSize(QtCore.QSize(66, 67))
        self.Mt.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Mt.setText("")
        self.Mt.setObjectName("Mt")
        self.Mt.clicked.connect(lambda x: self.dataAnalyze("Mt"))
        self.horizontalLayout_5.addWidget(self.Mt)
        self.Ds = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Ds.setMinimumSize(QtCore.QSize(66, 67))
        self.Ds.setMaximumSize(QtCore.QSize(66, 67))
        self.Ds.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ds.setText("")
        self.Ds.setObjectName("Ds")
        self.Ds.clicked.connect(lambda x: self.dataAnalyze("Ds"))
        self.horizontalLayout_5.addWidget(self.Ds)
        self.Rg = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Rg.setMinimumSize(QtCore.QSize(66, 67))
        self.Rg.setMaximumSize(QtCore.QSize(66, 67))
        self.Rg.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Rg.setText("")
        self.Rg.setObjectName("Rg")
        self.Rg.clicked.connect(lambda x: self.dataAnalyze("Rg"))
        self.horizontalLayout_5.addWidget(self.Rg)
        self.Cn = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Cn.setMinimumSize(QtCore.QSize(66, 67))
        self.Cn.setMaximumSize(QtCore.QSize(66, 67))
        self.Cn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Cn.setText("")
        self.Cn.setObjectName("Cn")
        self.Cn.clicked.connect(lambda x: self.dataAnalyze("Cn"))
        self.horizontalLayout_5.addWidget(self.Cn)
        self.Nh = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Nh.setMinimumSize(QtCore.QSize(66, 67))
        self.Nh.setMaximumSize(QtCore.QSize(66, 67))
        self.Nh.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Nh.setText("")
        self.Nh.setObjectName("Nh")
        self.Nh.clicked.connect(lambda x: self.dataAnalyze("Nh"))
        self.horizontalLayout_5.addWidget(self.Nh)
        self.Fl = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Fl.setMinimumSize(QtCore.QSize(66, 67))
        self.Fl.setMaximumSize(QtCore.QSize(66, 67))
        self.Fl.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Fl.setText("")
        self.Fl.setObjectName("Fl")
        self.Fl.clicked.connect(lambda x: self.dataAnalyze("Fl"))
        self.horizontalLayout_5.addWidget(self.Fl)
        self.Mc = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Mc.setMinimumSize(QtCore.QSize(66, 67))
        self.Mc.setMaximumSize(QtCore.QSize(66, 67))
        self.Mc.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Mc.setText("")
        self.Mc.setObjectName("Mc")
        self.Mc.clicked.connect(lambda x: self.dataAnalyze("Mc"))
        self.horizontalLayout_5.addWidget(self.Mc)
        self.Lv = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Lv.setMinimumSize(QtCore.QSize(66, 67))
        self.Lv.setMaximumSize(QtCore.QSize(66, 67))
        self.Lv.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Lv.setText("")
        self.Lv.setObjectName("Lv")
        self.Lv.clicked.connect(lambda x: self.dataAnalyze("Lv"))
        self.horizontalLayout_5.addWidget(self.Lv)
        self.Ts = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Ts.setMinimumSize(QtCore.QSize(66, 67))
        self.Ts.setMaximumSize(QtCore.QSize(66, 67))
        self.Ts.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ts.setText("")
        self.Ts.setObjectName("Ts")
        self.Ts.clicked.connect(lambda x: self.dataAnalyze("Ts"))
        self.horizontalLayout_5.addWidget(self.Ts)
        self.Og = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.Og.setMinimumSize(QtCore.QSize(66, 67))
        self.Og.setMaximumSize(QtCore.QSize(66, 67))
        self.Og.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Og.setText("")
        self.Og.setObjectName("Og")
        self.Og.clicked.connect(lambda x: self.dataAnalyze("Og"))
        self.horizontalLayout_5.addWidget(self.Og)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(340, 560, 299, 81))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.La = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.La.setMinimumSize(QtCore.QSize(66, 67))
        self.La.setMaximumSize(QtCore.QSize(66, 67))
        self.La.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.La.setText("")
        self.La.setObjectName("La")
        self.La.clicked.connect(lambda x: self.dataAnalyze("La"))
        self.horizontalLayout_6.addWidget(self.La)
        self.Ce = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.Ce.setMinimumSize(QtCore.QSize(66, 67))
        self.Ce.setMaximumSize(QtCore.QSize(66, 67))
        self.Ce.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ce.setText("")
        self.Ce.setObjectName("Ce")
        self.Ce.clicked.connect(lambda x: self.dataAnalyze("Ce"))
        self.horizontalLayout_6.addWidget(self.Ce)
        self.Pr = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.Pr.setMinimumSize(QtCore.QSize(66, 67))
        self.Pr.setMaximumSize(QtCore.QSize(66, 67))
        self.Pr.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Pr.setText("")
        self.Pr.setObjectName("Pr")
        self.Pr.clicked.connect(lambda x: self.dataAnalyze("Pr"))
        self.horizontalLayout_6.addWidget(self.Pr)
        self.Nd = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.Nd.setMinimumSize(QtCore.QSize(66, 67))
        self.Nd.setMaximumSize(QtCore.QSize(66, 67))
        self.Nd.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Nd.setText("")
        self.Nd.setObjectName("Nd")
        self.Nd.clicked.connect(lambda x: self.dataAnalyze("Nd"))
        self.horizontalLayout_6.addWidget(self.Nd)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(710, 558, 721, 81))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Sm = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Sm.setMinimumSize(QtCore.QSize(66, 67))
        self.Sm.setMaximumSize(QtCore.QSize(66, 67))
        self.Sm.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Sm.setText("")
        self.Sm.setObjectName("Sm")
        self.Sm.clicked.connect(lambda x: self.dataAnalyze("Sm"))
        self.horizontalLayout_7.addWidget(self.Sm)
        self.Eu = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Eu.setMinimumSize(QtCore.QSize(66, 67))
        self.Eu.setMaximumSize(QtCore.QSize(66, 67))
        self.Eu.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Eu.setText("")
        self.Eu.setObjectName("Eu")
        self.Eu.clicked.connect(lambda x: self.dataAnalyze("Eu"))
        self.horizontalLayout_7.addWidget(self.Eu)
        self.Gd = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Gd.setMinimumSize(QtCore.QSize(66, 67))
        self.Gd.setMaximumSize(QtCore.QSize(66, 67))
        self.Gd.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Gd.setText("")
        self.Gd.setObjectName("Gd")
        self.Gd.clicked.connect(lambda x: self.dataAnalyze("Gd"))
        self.horizontalLayout_7.addWidget(self.Gd)
        self.Tb = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Tb.setMinimumSize(QtCore.QSize(66, 67))
        self.Tb.setMaximumSize(QtCore.QSize(66, 67))
        self.Tb.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Tb.setText("")
        self.Tb.setObjectName("Tb")
        self.Tb.clicked.connect(lambda x: self.dataAnalyze("Tb"))
        self.horizontalLayout_7.addWidget(self.Tb)
        self.Dy = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Dy.setMinimumSize(QtCore.QSize(66, 67))
        self.Dy.setMaximumSize(QtCore.QSize(66, 67))
        self.Dy.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Dy.setText("")
        self.Dy.setObjectName("Dy")
        self.Dy.clicked.connect(lambda x: self.dataAnalyze("Dy"))
        self.horizontalLayout_7.addWidget(self.Dy)
        self.Ho = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Ho.setMinimumSize(QtCore.QSize(66, 67))
        self.Ho.setMaximumSize(QtCore.QSize(66, 67))
        self.Ho.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ho.setText("")
        self.Ho.setObjectName("Ho")
        self.Ho.clicked.connect(lambda x: self.dataAnalyze("Ho"))
        self.horizontalLayout_7.addWidget(self.Ho)
        self.Er = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Er.setMinimumSize(QtCore.QSize(66, 67))
        self.Er.setMaximumSize(QtCore.QSize(66, 67))
        self.Er.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Er.setText("")
        self.Er.setObjectName("Er")
        self.Er.clicked.connect(lambda x: self.dataAnalyze("Er"))
        self.horizontalLayout_7.addWidget(self.Er)
        self.Tm = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Tm.setMinimumSize(QtCore.QSize(66, 67))
        self.Tm.setMaximumSize(QtCore.QSize(66, 67))
        self.Tm.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Tm.setText("")
        self.Tm.setObjectName("Tm")
        self.Tm.clicked.connect(lambda x: self.dataAnalyze("Tm"))
        self.horizontalLayout_7.addWidget(self.Tm)
        self.Yb = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Yb.setMinimumSize(QtCore.QSize(66, 67))
        self.Yb.setMaximumSize(QtCore.QSize(66, 67))
        self.Yb.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Yb.setText("")
        self.Yb.setObjectName("Yb")
        self.Yb.clicked.connect(lambda x: self.dataAnalyze("Yb"))
        self.horizontalLayout_7.addWidget(self.Yb)
        self.Lu = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.Lu.setMinimumSize(QtCore.QSize(66, 67))
        self.Lu.setMaximumSize(QtCore.QSize(66, 67))
        self.Lu.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Lu.setText("")
        self.Lu.setObjectName("Lu")
        self.Lu.clicked.connect(lambda x: self.dataAnalyze("Lu"))
        self.horizontalLayout_7.addWidget(self.Lu)
        self.Th = QtWidgets.QPushButton(self.widget)
        self.Th.setGeometry(QtCore.QRect(414, 638, 66, 67))
        self.Th.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Th.setText("")
        self.Th.setObjectName("Th")
        self.Th.clicked.connect(lambda x: self.dataAnalyze("Th"))
        self.U = QtWidgets.QPushButton(self.widget)
        self.U.setGeometry(QtCore.QRect(561, 639, 66, 67))
        self.U.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 31px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.U.setText("")
        self.U.setObjectName("U")
        self.U.clicked.connect(lambda x: self.dataAnalyze("U"))
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(780, 640, 652, 69))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Am = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.Am.setMinimumSize(QtCore.QSize(66, 67))
        self.Am.setMaximumSize(QtCore.QSize(66, 67))
        self.Am.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Am.setText("")
        self.Am.setObjectName("Am")
        self.Am.clicked.connect(lambda x: self.dataAnalyze("Am"))
        self.horizontalLayout_8.addWidget(self.Am)
        self.Cm = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.Cm.setMinimumSize(QtCore.QSize(66, 67))
        self.Cm.setMaximumSize(QtCore.QSize(66, 67))
        self.Cm.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Cm.setText("")
        self.Cm.setObjectName("Cm")
        self.Cm.clicked.connect(lambda x: self.dataAnalyze("Cm"))
        self.horizontalLayout_8.addWidget(self.Cm)
        self.Bk = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.Bk.setMinimumSize(QtCore.QSize(66, 67))
        self.Bk.setMaximumSize(QtCore.QSize(66, 67))
        self.Bk.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Bk.setText("")
        self.Bk.setObjectName("Bk")
        self.Bk.clicked.connect(lambda x: self.dataAnalyze("Bk"))
        self.horizontalLayout_8.addWidget(self.Bk)
        self.Cf = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.Cf.setMinimumSize(QtCore.QSize(66, 67))
        self.Cf.setMaximumSize(QtCore.QSize(66, 67))
        self.Cf.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Cf.setText("")
        self.Cf.setObjectName("Cf")
        self.Cf.clicked.connect(lambda x: self.dataAnalyze("Cf"))
        self.horizontalLayout_8.addWidget(self.Cf)
        self.Es = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.Es.setMinimumSize(QtCore.QSize(66, 67))
        self.Es.setMaximumSize(QtCore.QSize(66, 67))
        self.Es.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Es.setText("")
        self.Es.setObjectName("Es")
        self.Es.clicked.connect(lambda x: self.dataAnalyze("Es"))
        self.horizontalLayout_8.addWidget(self.Es)
        self.Fm = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.Fm.setMinimumSize(QtCore.QSize(66, 67))
        self.Fm.setMaximumSize(QtCore.QSize(66, 67))
        self.Fm.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Fm.setText("")
        self.Fm.setObjectName("Fm")
        self.Fm.clicked.connect(lambda x: self.dataAnalyze("Fm"))
        self.horizontalLayout_8.addWidget(self.Fm)
        self.Md = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.Md.setMinimumSize(QtCore.QSize(66, 67))
        self.Md.setMaximumSize(QtCore.QSize(66, 67))
        self.Md.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Md.setText("")
        self.Md.setObjectName("Md")
        self.Md.clicked.connect(lambda x: self.dataAnalyze("Md"))
        self.horizontalLayout_8.addWidget(self.Md)
        self.No = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.No.setMinimumSize(QtCore.QSize(66, 67))
        self.No.setMaximumSize(QtCore.QSize(66, 67))
        self.No.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.No.setText("")
        self.No.setObjectName("No")
        self.No.clicked.connect(lambda x: self.dataAnalyze("No"))
        self.horizontalLayout_8.addWidget(self.No)
        self.Lr = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.Lr.setMinimumSize(QtCore.QSize(66, 67))
        self.Lr.setMaximumSize(QtCore.QSize(66, 67))
        self.Lr.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Lr.setText("")
        self.Lr.setObjectName("Lr")
        self.Lr.clicked.connect(lambda x: self.dataAnalyze("Lr"))
        self.horizontalLayout_8.addWidget(self.Lr)
        self.Ac = QtWidgets.QPushButton(self.widget)
        self.Ac.setGeometry(QtCore.QRect(342, 637, 68, 69))
        self.Ac.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ac.setText("")
        self.Ac.setObjectName("Ac")
        self.Ac.clicked.connect(lambda x: self.dataAnalyze("Ac"))
        self.Pa = QtWidgets.QPushButton(self.widget)
        self.Pa.setGeometry(QtCore.QRect(488, 638, 68, 69))
        self.Pa.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Pa.setText("")
        self.Pa.setObjectName("Pa")
        self.Pa.clicked.connect(lambda x: self.dataAnalyze("Pa"))
        self.Np = QtWidgets.QPushButton(self.widget)
        self.Np.setGeometry(QtCore.QRect(634, 638, 68, 69))
        self.Np.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Np.setText("")
        self.Np.setObjectName("Np")
        self.Np.clicked.connect(lambda x: self.dataAnalyze("Np"))
        self.Pu = QtWidgets.QPushButton(self.widget)
        self.Pu.setGeometry(QtCore.QRect(707, 637, 68, 69))
        self.Pu.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Pu.setText("")
        self.Pu.setObjectName("Pu")
        self.Pu.clicked.connect(lambda x: self.dataAnalyze("Pu"))
        self.Pm = QtWidgets.QPushButton(self.widget)
        self.Pm.setGeometry(QtCore.QRect(634, 564, 68, 69))
        self.Pm.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Pm.setText("")
        self.Pm.setObjectName("Pm")
        self.Pm.clicked.connect(lambda x: self.dataAnalyze("Pm"))
        self.Ra = QtWidgets.QPushButton(self.widget)
        self.Ra.setGeometry(QtCore.QRect(414, 468, 68, 69))
        self.Ra.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Ra.setText("")
        self.Ra.setObjectName("Ra")
        self.Ra.clicked.connect(lambda x: self.dataAnalyze("Ra"))
        self.Fr = QtWidgets.QPushButton(self.widget)
        self.Fr.setGeometry(QtCore.QRect(341, 467, 68, 69))
        self.Fr.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Fr.setText("")
        self.Fr.setObjectName("Fr")
        self.Fr.clicked.connect(lambda x: self.dataAnalyze("Fr"))
        self.Tc = QtWidgets.QPushButton(self.widget)
        self.Tc.setGeometry(QtCore.QRect(780, 322, 68, 69))
        self.Tc.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Tc.setText("")
        self.Tc.setObjectName("Tc")
        self.Tc.clicked.connect(lambda x: self.dataAnalyze("Tc"))
        self.Rn = QtWidgets.QPushButton(self.widget)
        self.Rn.setGeometry(QtCore.QRect(1583, 394, 68, 69))
        self.Rn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Rn.setText("")
        self.Rn.setObjectName("Rn")
        self.Rn.clicked.connect(lambda x: self.dataAnalyze("Rn"))
        self.At = QtWidgets.QPushButton(self.widget)
        self.At.setGeometry(QtCore.QRect(1509, 394, 68, 69))
        self.At.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.At.setText("")
        self.At.setObjectName("At")
        self.At.clicked.connect(lambda x: self.dataAnalyze("At"))
        self.Po = QtWidgets.QPushButton(self.widget)
        self.Po.setGeometry(QtCore.QRect(1436, 394, 68, 69))
        self.Po.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom-right-radius : 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255,20);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255,60);\n"
"}")
        self.Po.setText("")
        self.Po.setObjectName("Po")
        self.Po.clicked.connect(lambda x: self.dataAnalyze("Po"))
        self.sembol_label = QtWidgets.QLabel(self.widget)
        self.sembol_label.setGeometry(QtCore.QRect(310, 730, 121, 81))
        self.sembol_label.setStyleSheet("QLabel{\n"
"\n"
"color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 64px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"}")
        self.sembol_label.setObjectName("sembol_label")
        self.renk_label = QtWidgets.QLabel(self.widget)
        self.renk_label.setGeometry(QtCore.QRect(310, 730, 611, 81))
        self.renk_label.setText("")
        self.renk_label.setObjectName("renk_label")
        self.isim_label = QtWidgets.QLabel(self.widget)
        self.isim_label.setGeometry(QtCore.QRect(450, 730, 471, 81))
        self.isim_label.setStyleSheet("QLabel{\n"
"\n"
"color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 55px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"}")
        self.isim_label.setText("")
        self.isim_label.setTextFormat(QtCore.Qt.AutoText)
        self.isim_label.setScaledContents(False)
        self.isim_label.setWordWrap(True)
        self.isim_label.setOpenExternalLinks(False)
        self.isim_label.setObjectName("isim_label")
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setGeometry(QtCore.QRect(310, 830, 161, 31))
        self.label_1.setStyleSheet("color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.label_1.setObjectName("label_1")
        self.atom_kutlesi_label = QtWidgets.QLabel(self.widget)
        self.atom_kutlesi_label.setGeometry(QtCore.QRect(468, 830, 161, 31))
        self.atom_kutlesi_label.setStyleSheet("color: #B3B3B3;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.atom_kutlesi_label.setObjectName("atom_kutlesi_label")
        self.kaynama_nok_label = QtWidgets.QLabel(self.widget)
        self.kaynama_nok_label.setGeometry(QtCore.QRect(513, 870, 161, 31))
        self.kaynama_nok_label.setStyleSheet("color: #B3B3B3;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.kaynama_nok_label.setObjectName("kaynama_nok_label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(310, 870, 211, 31))
        self.label_2.setStyleSheet("color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.label_2.setObjectName("label_2")
        self.elektron_dizilimi_label = QtWidgets.QLabel(self.widget)
        self.elektron_dizilimi_label.setGeometry(QtCore.QRect(507, 910, 1500, 31))
        self.elektron_dizilimi_label.setStyleSheet("color: #B3B3B3;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.elektron_dizilimi_label.setObjectName("elektron_dizilimi_label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(310, 910, 211, 31))
        self.label_3.setStyleSheet("color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.label_3.setObjectName("label_3")
        self.Konum_label = QtWidgets.QLabel(self.widget)
        self.Konum_label.setGeometry(QtCore.QRect(423, 950, 381, 31))
        self.Konum_label.setStyleSheet("color: #B3B3B3;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.Konum_label.setObjectName("Konum_label")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(310, 950, 111, 31))
        self.label_4.setStyleSheet("color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.label_4.setObjectName("label_4")
        self.bulankisi_label = QtWidgets.QLabel(self.widget)
        self.bulankisi_label.setGeometry(QtCore.QRect(480, 990, 381, 31))
        self.bulankisi_label.setStyleSheet("color: #B3B3B3;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.bulankisi_label.setObjectName("bulankisi_label")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(310, 990, 171, 31))
        self.label_5.setStyleSheet("color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.label_5.setObjectName("label_5")
        self.aciklama_label = QtWidgets.QLabel(self.widget)
        self.aciklama_label.setGeometry(QtCore.QRect(1160, 770, 731, 271))
        self.aciklama_label.setStyleSheet("color: #FFF;\n"
"font-family: Inter;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;")
        self.aciklama_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.aciklama_label.setWordWrap(True)
        self.aciklama_label.setObjectName("aciklama_label")
        self.renk_label.raise_()
        self.H.raise_()
        self.Li.raise_()
        self.Na.raise_()
        self.K.raise_()
        self.Rb.raise_()
        self.Cs.raise_()
        self.Be.raise_()
        self.Mg.raise_()
        self.Ca.raise_()
        self.Sr.raise_()
        self.Ba.raise_()
        self.Sc.raise_()
        self.Ti.raise_()
        self.V.raise_()
        self.Cr.raise_()
        self.Mn.raise_()
        self.Fe.raise_()
        self.Co.raise_()
        self.Ni.raise_()
        self.Cu.raise_()
        self.Zn.raise_()
        self.Ga.raise_()
        self.Ge.raise_()
        self.As.raise_()
        self.Se.raise_()
        self.Br.raise_()
        self.Kr.raise_()
        self.Ar.raise_()
        self.S.raise_()
        self.P.raise_()
        self.Si.raise_()
        self.Cl.raise_()
        self.Al.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.He.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.horizontalLayoutWidget_6.raise_()
        self.horizontalLayoutWidget_7.raise_()
        self.Th.raise_()
        self.U.raise_()
        self.horizontalLayoutWidget_8.raise_()
        self.Ac.raise_()
        self.Pa.raise_()
        self.Np.raise_()
        self.Pu.raise_()
        self.Pm.raise_()
        self.Ra.raise_()
        self.Fr.raise_()
        self.Tc.raise_()
        self.Rn.raise_()
        self.At.raise_()
        self.Po.raise_()
        self.sembol_label.raise_()
        self.isim_label.raise_()
        self.label_1.raise_()
        self.atom_kutlesi_label.raise_()
        self.kaynama_nok_label.raise_()
        self.label_2.raise_()
        self.elektron_dizilimi_label.raise_()
        self.label_3.raise_()
        self.Konum_label.raise_()
        self.label_4.raise_()
        self.bulankisi_label.raise_()
        self.label_5.raise_()
        self.aciklama_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sembol_label.setText(_translate("MainWindow", ""))
        self.label_1.setText(_translate("MainWindow", "• Atom Kütlesi: "))
        self.atom_kutlesi_label.setText(_translate("MainWindow", " "))
        self.kaynama_nok_label.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "• Kaynama Noktası:"))
        self.elektron_dizilimi_label.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "• Elektron Dizilimi:"))
        self.Konum_label.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "• Konumu:"))
        self.bulankisi_label.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "• Keşfeden(ler):"))
        self.aciklama_label.setText(_translate("MainWindow", ""))
    def close(self):
        MainWindow.close()

    def dataAnalyze(self,idx):


        _translate = QtCore.QCoreApplication.translate
        with open("data\PeriodicTableJSON.json", "r", encoding="utf-8") as file:
    
                veri = json.load(file)
        
        for w in veri["elements"]:
            if w["symbol"] == idx:
                if w["name"] != None:
                        name = w["name"]
                if w["symbol"] != None:
                        symbol = w["symbol"]
                if w["atomic_mass"] != None:
                        atom_kutlesi = w["atomic_mass"]
                else: atom_kutlesi = "Bilinmiyor"
                if w["discovered_by"] != None:
                        kesfeden_kisi = w["discovered_by"]
                else: kesfeden_kisi = "Bilinmiyor"
                if w["period"] != None:
                        period = w["period"]
                if w["group"] != None:
                        grup = w["group"]
                if w["block"] != None:
                      blok = w["block"]
                      blok = blok.upper()
                else:blok = "Bilinmiyor"
                konumu = f"{period}. Periyot {grup}. Grup {blok} Bloğu "
                if w["summary"] != None:
                        aciklama = w["summary"]
                else: aciklama = "Bilinmiyor"
                if w["boil"] != None:
                        boil =round(w["boil"],2)
                else: boil = "Bilinmiyor"
                if boil == "Bilinmiyor":
                      kaynama = f"{boil}"
                else:
                        kaynama = f"{boil}K"
                e_config = w["electron_configuration_semantic"]
                 
        self.sembol_label.setText(_translate("MainWindow", f"{symbol}"))
        self.isim_label.setText(_translate("MainWindow", f"{name}"))
        self.atom_kutlesi_label.setText(_translate("MainWindow", f"{atom_kutlesi}u"))
        self.kaynama_nok_label.setText(_translate("MainWindow", f"{kaynama}"))
        self.elektron_dizilimi_label.setText(_translate("MainWindow", f"{e_config}"))
        self.Konum_label.setText(_translate("MainWindow", f"{konumu}"))
        self.bulankisi_label.setText(_translate("MainWindow", f"{kesfeden_kisi}"))
        self.aciklama_label.setText(_translate("MainWindow", f"{aciklama}"))
    def elektronik_yapi(self,atom_num):
            elektron = atom_num

            alt_seviyeler = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
            max_elektron = {"s": 2, "p": 6, "d": 10, "f": 14}

            yapi = {}
            elementler = {
                2: ("Helyum", "He"),
                10: ("Neon", "Ne"),
                18: ("Argon", "Ar"),
                36: ("Kripton", "Kr")
            }
            toplam_elektron = 0
            while elektron > 0:
                for alt_seviye in alt_seviyeler:
                    max_e = max_elektron[alt_seviye[-1]]
                    if elektron >= max_e:
                        elektron -= max_e
                        yapi[alt_seviye] = max_e
                        toplam_elektron += max_e
                    elif elektron < max_e:
                        yapi[alt_seviye] = elektron
                        toplam_elektron += elektron
                        elektron = 0
                    if elektron == 0:
                        break

            metin = ""
            if toplam_elektron in elementler:
                sembol = elementler[toplam_elektron][1]
                metin += f"{sembol}{''.join(['⁰¹²³⁴⁵⁶⁷⁸⁹'[int(digit)] for digit in str(toplam_elektron)])} "
                for alt_seviye in alt_seviyeler:
                    if int(alt_seviye[0]) <= toplam_elektron:
                        yapi.pop(alt_seviye, None)
           
            for anahtar, deger in yapi.items():
                metin += f"{anahtar}{''.join(['⁰¹²³⁴⁵⁶⁷⁸⁹'[int(digit)] for digit in str(deger)])} "

            
            return metin.strip()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    keyboard.add_hotkey('esc',ui.close)
    sys.exit(app.exec_())
