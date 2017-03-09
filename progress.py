#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
#
#@author: pengzx
#@version: 2.0
# Created by: PyQt5 UI code generator 5.5.1
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from datetime import date, datetime
import xml.etree.ElementTree as ET
import os
class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setWindowModality(QtCore.Qt.NonModal)
		MainWindow.resize(1024, 730)
		MainWindow.setWindowTitle("果蝇管理")
		MainWindow.setWindowIcon(QtGui.QIcon('fruitfly.png'))
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		self.gridLayout_all = QtWidgets.QGridLayout(self.centralWidget)
		self.gridLayout_all.setObjectName("gridLayout_all")
		palette1 = QtGui.QPalette()
		palette1.setBrush(self.centralWidget.backgroundRole(),QtGui.QBrush(QtGui.QPixmap("background_02.jpg")))
		self.centralWidget.setPalette(palette1)
		self.centralWidget.setAutoFillBackground(True)
		self.centralWidget.setWindowOpacity(0.2)

		self.formLayout = QtWidgets.QFormLayout()
		self.formLayout.setObjectName("formLayout")
		self.nameLabel = QtWidgets.QLabel(self.centralWidget)
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(11)
		self.nameLabel.setFont(font)
		self.nameLabel.setObjectName("nameLabel")
		self.flyName = QtWidgets.QLineEdit(self.centralWidget)
		self.flyName.setFont(font)
		self.flyName.setObjectName("flyName")
		self.formLayout.addRow(self.nameLabel,self.flyName)
		self.dateEdit = QtWidgets.QDateEdit(self.centralWidget)
		self.dateEdit.setFont(font)
		self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate(),QtCore.QTime(0,0,0)))
		self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
		self.dateEdit.setObjectName("dateEdit")
		self.dateLabel = QtWidgets.QLabel(self.centralWidget)
		self.dateLabel.setFont(font)
		self.dateLabel.setObjectName("dateLabel")
		self.formLayout.addRow(self.dateLabel,self.dateEdit)
		self.numLabel = QtWidgets.QLabel(self.centralWidget)
		self.numLabel.setFont(font)
		self.numLabel.setObjectName("numLabel")
		self.botNum = QtWidgets.QLineEdit(self.centralWidget)
		self.botNum.setFont(font)
		self.botNum.setObjectName("botNum")
		self.formLayout.addRow(self.numLabel,self.botNum)
		self.patternLabel = QtWidgets.QLabel(self.centralWidget)
		self.patternLabel.setFont(font)
		self.patternLabel.setObjectName("patternLabel")
		self.patternT = QtWidgets.QComboBox(self.centralWidget)
		self.patternT.setFont(font)
		self.patternT.setInputMethodHints(QtCore.Qt.ImhNone)
		self.patternT.setEditable(False)
		self.patternT.setObjectName("patternT")
		self.patternT.addItem("")
		self.patternT.addItem("")
		self.patternT.addItem("")
		self.patternT.addItem("")
		self.formLayout.addRow(self.patternLabel,self.patternT)
		self.envT = QtWidgets.QComboBox(self.centralWidget)
		self.envT.setFont(font)
		self.envT.setObjectName("envT")
		self.envT.addItem("")
		self.envT.addItem("")
		self.envT.addItem("")
		self.temTabel = QtWidgets.QLabel(self.centralWidget)
		self.temTabel.setFont(font)
		self.temTabel.setObjectName("temTabel")
		self.formLayout.addRow(self.temTabel,self.envT)
		self.colorTabel = QtWidgets.QLabel(self.centralWidget)
		self.colorTabel.setFont(font)
		self.colorTabel.setObjectName("colorTabel")
		self.colorP = QtWidgets.QComboBox(self.centralWidget)
		self.colorP.setObjectName("colorP")
		pix = QtGui.QPixmap(QtCore.QSize(200,15))
		pix.fill(QtGui.QColor(244,208,0))
		self.colorP.addItem("")
		self.colorP.addItem(QtGui.QIcon(pix),"")
		pix.fill(QtGui.QColor(107,194,53))
		self.colorP.addItem(QtGui.QIcon(pix),"")
		pix.fill(QtGui.QColor(1,165,175))
		self.colorP.addItem(QtGui.QIcon(pix),"")
		self.colorP.setIconSize(QtCore.QSize(200,20))
		self.formLayout.addRow(self.colorTabel,self.colorP)
		self.datePLabel = QtWidgets.QLabel(self.centralWidget)
		self.datePLabel.setObjectName("datePLabel")
		self.datePLabel.setFont(font)
		self.dateP = QtWidgets.QComboBox(self.centralWidget)
		self.dateP.setObjectName("dateP")
		self.dateP.addItem("")
		self.formLayout.addRow(self.datePLabel,self.dateP)
		self.pushButton = QtWidgets.QPushButton(self.centralWidget)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.formLayout.addRow("",self.pushButton)
		self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
		self.gridLayout_all.addLayout(self.formLayout,0,0,1,2)
		
#基因型列表		
		self.gridLayout_2 = QtWidgets.QGridLayout()
		self.gridLayout_2.setObjectName("gridLayout_2")
		spacerItem = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
		self.geneDisLabel = QtWidgets.QLabel(self.centralWidget)
		font = QtGui.QFont()
		font.setFamily("隶书")
		font.setPointSize(20)
		self.geneDisLabel.setFont(font)
		self.geneDisLabel.setObjectName("geneDisLabel")
		self.gridLayout_2.addWidget(self.geneDisLabel, 0, 1, 1, 3)
		self.listP = QtWidgets.QComboBox(self.centralWidget)
		font.setFamily("微软雅黑")
		font.setPointSize(12)
		self.listP.setFont(font)
		self.listP.setObjectName("envT")
		self.listP.addItem("")
		self.listP.addItem("食物模式         ")
		self.listP.addItem("蝇房温度         ")
		self.listP.addItem("颜色             ")
		self.gridLayout_2.addWidget(self.listP, 0, 4, 1, 1)
		self.treeWidget = QtWidgets.QTreeWidget(self.centralWidget)
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(10)
		self.treeWidget.setFont(font)
		self.treeWidget.setObjectName("treeWidget")
		self.treeWidget.setColumnCount(2)
		self.treeWidget.setColumnWidth(0,250)
		self.treeWidget.setColumnWidth(1,50)
		self.treeWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
		self.treeWidget.setMinimumWidth(320)
		self.gridLayout_2.addWidget(self.treeWidget, 1, 0, 1, 5)
		spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 2)
		self.delBtn = QtWidgets.QPushButton(self.centralWidget)
		font = QtGui.QFont()
		font.setFamily("楷体")
		font.setPointSize(16)
		self.delBtn.setFont(font)
		self.delBtn.setObjectName("delBtn")
		self.gridLayout_2.addWidget(self.delBtn, 2, 2, 1, 1)
		spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem3, 2, 3, 1, 2)
		self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
		self.gridLayout_all.addLayout(self.gridLayout_2,1,0,2,2)
		
		self.calendarWidget = QtWidgets.QCalendarWidget(self.centralWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.calendarWidget.setSizePolicy(sizePolicy)
		self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
#		self.calendarWidget.setFixedWidth(420)
		self.calendarWidget.setObjectName("calendarWidget")
		self.gridLayout_all.addWidget(self.calendarWidget,0,3,1,3)

		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.treeWidget_2 = QtWidgets.QTreeWidget(self.centralWidget)
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(10)
		self.treeWidget_2.setFont(font)
		self.treeWidget_2.setObjectName("treeWidget_2")
		self.treeWidget_2.setColumnCount(3)
		self.treeWidget_2.setColumnWidth(0,400)
		self.treeWidget_2.setColumnWidth(1,80)
		self.treeWidget_2.setColumnWidth(2,80)
		self.treeWidget_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)	
		self.treeWidget_2.setMinimumWidth(320)
		self.gridLayout.addWidget(self.treeWidget_2, 0, 0, 1, 5)
		spacerItem7 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem7, 1, 0, 1, 1)
		self.completeBtn = QtWidgets.QPushButton(self.centralWidget)
		font = QtGui.QFont()
		font.setFamily("楷体")
		font.setPointSize(16)
		self.completeBtn.setFont(font)
		self.completeBtn.setObjectName("completeBtn")
		self.gridLayout.addWidget(self.completeBtn, 1, 1, 1, 1)
		spacerItem9 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem9, 1, 2, 1, 1)
		self.createBtn = QtWidgets.QPushButton("批量新建",self.centralWidget)
		self.createBtn.setFont(font)
		self.createBtn.setObjectName("createBtn")
		self.gridLayout.addWidget(self.createBtn, 1, 3, 1, 1)
		spacerItem8 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem8, 1, 4, 1, 1)
		self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
		self.gridLayout_all.addLayout(self.gridLayout,1,3,2,3)

		MainWindow.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 31))
		self.menuBar.setObjectName("menuBar")
		self.menu_F = QtWidgets.QMenu(self.menuBar)
		self.menu_F.setObjectName("menu_F")
		self.menu_S = QtWidgets.QMenu(self.menuBar)
		self.menu_S.setObjectName("menu_S")
		self.menu_H = QtWidgets.QMenu(self.menuBar)
		self.menu_H.setObjectName("menu_H")
		MainWindow.setMenuBar(self.menuBar)
		self.action_N = QtWidgets.QAction(MainWindow)
		self.action_N.setObjectName("action_N")
		self.action_O = QtWidgets.QAction(MainWindow)
		self.action_O.setObjectName("action_O")
		self.action_I = QtWidgets.QAction(MainWindow)
		self.action_I.setObjectName("action_I")
		self.action_X = QtWidgets.QAction(MainWindow)
		self.action_X.setObjectName("action_X")
		self.action_S = QtWidgets.QAction(MainWindow)
		self.action_S.setObjectName("action_S")
		self.action_B = QtWidgets.QAction(MainWindow)
		self.action_B.setObjectName("action_B")
		self.action_A = QtWidgets.QAction(MainWindow)
		self.action_A.setObjectName("action_A")
		self.menu_F.addAction(self.action_N)
		self.menu_F.addAction(self.action_O)
		self.menu_F.addAction(self.action_I)
		self.menu_F.addSeparator()
		self.menu_F.addAction(self.action_X)
		self.menu_S.addAction(self.action_S)
		self.menu_H.addAction(self.action_B)
		self.menu_H.addAction(self.action_A)
		self.menuBar.addAction(self.menu_F.menuAction())
		self.menuBar.addAction(self.menu_S.menuAction())
		self.menuBar.addAction(self.menu_H.menuAction())
#窗口打开默认文件
		self.defaultFile = os.getcwd()+'/default_02.ffsm'
		self.doc = ET.ElementTree()
		self.isFileExist()
		self.curFilename = self.defaultFile
		self.loadFile(self.curFilename)
		self.templateWindow = TemplateSetting()
		self.dateWindow = DateWindow()
		self.datePRefresh()
		self.retranslateUi(MainWindow)

#添加的事件，这些是菜单栏相关
		self.action_N.triggered.connect(self.newFile)
		self.action_O.triggered.connect(self.openFile)
		self.action_I.triggered.connect(self.importOldFile)
		self.action_X.triggered.connect(QtCore.QCoreApplication.instance().quit)
		self.action_S.triggered.connect(self.openTemplate)
		self.action_B.triggered.connect(self.about)
		self.action_A.triggered.connect(self.usageHelp)
#添加的事件，这些是窗口里按钮按下的事件
		self.calendarWidget.clicked.connect(self.otherDayShow)
		self.treeWidget.itemDoubleClicked.connect(self.dateShow)
		self.treeWidget_2.itemChanged.connect(self.itemCheck)
		self.treeWidget.itemChanged.connect(self.itemCheck)
		self.pushButton.clicked.connect(self.addXmlStock)
		self.delBtn.clicked.connect(self.delXmlStock)
		self.completeBtn.clicked.connect(self.delEvent)
		self.createBtn.clicked.connect(self.createNewStocksInBatch)
		self.listP.currentIndexChanged.connect(self.geneListAdjust)

		QtCore.QMetaObject.connectSlotsByName(MainWindow)

#以上是ui设置以及事件响应，以下为相关函数
#使用说明
	def usageHelp(self):
		QMessageBox.information(MainWindow,"使用说明","1.在左上部分输入蝇的相关信息(基因型不能一样）后，点击保存后即可录入\n2.勾选方框后再点击相应按键可删除基因型或者今日已完成事件\n4.点击日历里的其他日期，会显示该日期下要做的事,但今天之前的不会显示。\n5.默认情况下，信息保存在同一文件夹下的default.ffsm里。\n6.当天录入的如果有要当天处理的，默认已处理完毕。\n7")

#关于，即软件说明
	def about(self):
		QMessageBox.information(MainWindow,"关于","该软件用于YiLab同学管理自己的果蝇。\n""----------------------------------------\n""版本：1.0\n开发者：彭怡晴\n联系方式：pyqzzx@163.com\n")
#导入上一版本的文件
	def importOldFile(self):
		fileName, ok = QFileDialog.getOpenFileName(MainWindow,'打开文件','.','Xml Files (*.ffsm);;ALL Files (*)')
		if fileName:
			tree_old = ET.parse(fileName)
			root_old = tree_old.getroot()
			for stock in root_old.iter('stock'):
				p = stock.find('pattern').text 
				if p == '大厚新蝇':
					p_n=0
				elif p =='大厚老蝇':
					p_n=1
				else:
					p_n=2
				e = stock.find('envtem').text
				if e == '23度':
					e_n=0
				else:
					e_n=1
				templateName = self.getTemplateName(p_n,e_n)
				s = {'name':stock.get('name'),'startdate':stock.find('startdate').text,'bottlenum':stock.find('bottlenum').text,'pattern':str(p_n),'envtem':str(e_n),'color':'0'}
				item = self.addStock(s,templateName)
				self.treeWidget.clear()
				if item:
					xmltoday = self.doc.find('today')
					node = ET.SubElement(xmltoday, 'toBeDone')
					node.set('action',item['action'])
					node.set('name',item['name'])
					node.set('bottle',item['bottle'])
					node.set('room',item['room'])
				self.doc.write(self.curFilename,encoding="utf-8",xml_declaration=True,method="xml")
				self.loadFile(self.curFilename)
				if self.string2Date(self.calendarWidget.selectedDate().toString(format=QtCore.Qt.ISODate))==date.today() and item:
					l = [item]
					self.widgetAddEvent(l)

	def geneListAdjust(self, i):
		self.genetypeShow(self.curFilename,i)
	
#打开文件
	def openFile(self):
		fileName, ok = QFileDialog.getOpenFileName(MainWindow,'打开文件','.','Xml Files (*.ffsm);;ALL Files (*)')
		if fileName:
			self.curFilename = fileName
			self.loadFile(self.curFilename)
#载入文件内容
	def loadFile(self,fileName):
			self.doc = ET.parse(fileName)
			self.genetypeShow(fileName,self.listP.currentIndex())
			date = self.string2Date(self.calendarWidget.selectedDate().toString(format=QtCore.Qt.ISODate))
			self.eventShow(fileName,date)

#判断默认文件是否存在，否则新建。
	def isFileExist(self):
		f = QtCore.QFile(self.defaultFile)
		if f.exists():
			if not f.open(QtCore.QFile.ReadOnly):
				QMessageBox.warning(MainWindow, "应用","不能打开文件 %s:\n%s." % (fileName, f.errorString()))
				f.closed()
		else:
			self.saveFile(self.defaultFile)

#保存文件
	def saveFile(self, fileName):
		stocklist = ET.Element('stocklist')
		today = ET.SubElement(stocklist,'today')
		today.set("date",date.today().isoformat())
		tree = ET.ElementTree(stocklist)
		tree.write(fileName,encoding="utf-8",xml_declaration=True,method="xml")
#新建文件
	def newFile(self):
		fileName, ok = QFileDialog.getSaveFileName(MainWindow,'保存文件','.','Xml Files (*.ffsm);;ALL Files (*)')
		if fileName:
			fileName = fileName+'.ffsm'
			self.saveFile(fileName)
			self.curFilename = fileName
			self.doc = ET.parse(fileName)
			self.treeWidget.clear()
			self.treeWidget_2.clear()
			self.flyName.clear()
			self.botNum.clear()
		else:
			QMessageBox.warning(MainWindow, "应用","文件名不能为空！")

#显示已储存基因型
	def genetypeShow(self,fileName,i):
		self.treeWidget.clear()
		self.doc = ET.parse(fileName)
		xmlRoot = self.doc.getroot()
		stocks = xmlRoot.iter('stock')
		if i == 0 :
			for stock in stocks:
				node = QtWidgets.QTreeWidgetItem(self.treeWidget)
				self.widget1addNode(node,stock)
		elif i == 1:
			item_1 = QtWidgets.QTreeWidgetItem(self.treeWidget,['大厚新蝇'])
			self.treeWidget.addTopLevelItem(item_1)
			item_1.setCheckState(0,QtCore.Qt.Unchecked)
			item_2 = QtWidgets.QTreeWidgetItem(self.treeWidget,['大厚老蝇或小厚'])
			self.treeWidget.addTopLevelItem(item_2)
			item_2.setCheckState(0,QtCore.Qt.Unchecked)
			item_3 = QtWidgets.QTreeWidgetItem(self.treeWidget,['大薄或小薄'])
			self.treeWidget.addTopLevelItem(item_3)
			item_3.setCheckState(0,QtCore.Qt.Unchecked)
			item_4 = QtWidgets.QTreeWidgetItem(self.treeWidget,['其他'])
			self.treeWidget.addTopLevelItem(item_4)
			item_4.setCheckState(0,QtCore.Qt.Unchecked)
#			items = [item_1,item_2,item_3,item_4]
			for stock in stocks:
				if stock.find('pattern').text == '0':
					node = QtWidgets.QTreeWidgetItem(item_1)
					self.widget1addNode(node,stock)
				elif stock.find('pattern').text == '1':
					node = QtWidgets.QTreeWidgetItem(item_2)
					self.widget1addNode(node,stock)
				elif stock.find('pattern').text == '2':
					node = QtWidgets.QTreeWidgetItem(item_3)
					self.widget1addNode(node,stock)
				elif stock.find('pattern').text == '3':
					node = QtWidgets.QTreeWidgetItem(item_4)
					self.widget1addNode(node,stock)
		elif i == 2:
			item_1 = QtWidgets.QTreeWidgetItem(self.treeWidget,['23度'])
			self.treeWidget.addTopLevelItem(item_1)
			item_1.setCheckState(0,QtCore.Qt.Unchecked)
			item_2 = QtWidgets.QTreeWidgetItem(self.treeWidget,['18度'])
			self.treeWidget.addTopLevelItem(item_2)
			item_2.setCheckState(0,QtCore.Qt.Unchecked)
			item_3 = QtWidgets.QTreeWidgetItem(self.treeWidget,['其他'])
			self.treeWidget.addTopLevelItem(item_3)
			item_3.setCheckState(0,QtCore.Qt.Unchecked)
			for stock in stocks:
				if stock.find('envtem').text == '0':
					node = QtWidgets.QTreeWidgetItem(item_1)
					self.widget1addNode(node,stock)
				elif stock.find('envtem').text == '1':
					node = QtWidgets.QTreeWidgetItem(item_2)
					self.widget1addNode(node,stock)
				elif stock.find('envtem').text == '2':
					node = QtWidgets.QTreeWidgetItem(item_3)
					self.widget1addNode(node,stock)
		elif i == 3:
			item_1 = QtWidgets.QTreeWidgetItem(self.treeWidget,['无色'])
			self.treeWidget.addTopLevelItem(item_1)
			item_1.setCheckState(0,QtCore.Qt.Unchecked)
			item_2 = QtWidgets.QTreeWidgetItem(self.treeWidget,['黄'])
			self.treeWidget.addTopLevelItem(item_2)
			item_2.setCheckState(0,QtCore.Qt.Unchecked)
			item_3 = QtWidgets.QTreeWidgetItem(self.treeWidget,['绿'])
			self.treeWidget.addTopLevelItem(item_3)
			item_3.setCheckState(0,QtCore.Qt.Unchecked)
			item_4 = QtWidgets.QTreeWidgetItem(self.treeWidget,['蓝'])
			self.treeWidget.addTopLevelItem(item_4)
			item_4.setCheckState(0,QtCore.Qt.Unchecked)
			items = [item_1,item_2,item_3,item_4]
			for stock in stocks:
				c = int(stock.find('color').text)
				node = QtWidgets.QTreeWidgetItem(items[c])
				self.widget1addNode(node,stock)
				
	def widget1addNode(self,node,stock):
		node.setText(0,stock.get('name'))
		node.setCheckState(0,QtCore.Qt.Unchecked)
		node.setText(1,stock.find("targetdate").text)
		c = int(stock.find('color').text)
		if c > 0:
			l = [QtGui.QBrush(QtGui.QColor(244,208,0)),QtGui.QBrush(QtGui.QColor(107,194,53)),QtGui.QBrush(QtGui.QColor(1,165,175))]
			node.setBackground(0,l[c-1])

#字符串转换日期格式
	def string2Date(self,s):
		dTType = datetime.strptime(s,'%Y-%m-%d')
		s = date(dTType.year,dTType.month,dTType.day)
		return s
#显示某日待办事项
	def eventShow(self,fileName,calendarDate):
		self.treeWidget_2.clear()
		xmlRoot = self.doc.getroot()
		today = date.today()
		if calendarDate == today:
			xmlToday = xmlRoot.find('today')
			xmlDate = xmlToday.get('date')
			dateSet = self.string2Date(xmlDate)
			deltaDay = today-dateSet
			if deltaDay.days>0:
				toBeDone = xmlToday.iter('toBeDone')
				if toBeDone:
					for event in toBeDone:
						stocks = xmlRoot.iter('stock')
						for stock in stocks:
							if stock.get("name")==event.get("name"):
								targetDate = stock.find('targetdate')
								newDate = self.string2Date(targetDate.text)
								targetDate.text = (newDate+deltaDay).isoformat()
					xmlToday.clear()
				l = self.dateEventsList(today)
				if l:
					for item in l:
						node = ET.SubElement(xmlToday, 'toBeDone')
						node.set('action',item['action'])
						node.set('name',item['name'])
						node.set('bottle',item['bottle'])
						node.set('room',item['room'])
				xmlToday.set("date",today.isoformat())
			toBeDone = xmlToday.iter('toBeDone')
			l = []
			if toBeDone:
				for item in toBeDone:
					l = l+[{'action':item.get('action'),'name':item.get('name'),'bottle':item.get('bottle'),'room':item.get('room')}]
				self.widgetAddEvent(l)
			self.doc.write(fileName,encoding="utf-8",xml_declaration=True,method="xml")
		elif calendarDate<today:
			self.treeWidget_2.clear()
			QMessageBox.warning(MainWindow, "选的日期是过去的！", "过去的记录不保留!")
		else:
			self.treeWidget_2.clear()
			l = self.dateEventsList(calendarDate)
			self.widgetAddEvent(l)

	def otherDayShow(self):
		date =  self.string2Date(self.calendarWidget.selectedDate().toString(format=QtCore.Qt.ISODate))
		self.eventShow(self.curFilename,date)

	def dateEventsList(self,dateNeed):
		xmlRoot = self.doc.getroot()
		stocks = xmlRoot.iter('stock')
		l =[]
		for stock in stocks:
			item = self.getEvent(stock,dateNeed)
			if item:
				l = l+[item]
		return l

	def widgetAddEvent(self,l):
		if l:
			for event in l:
				addOrNo = 0
				TLICount = self.treeWidget_2.topLevelItemCount()
				if TLICount>0:
					for n in range(TLICount):
						if event['action'] == self.treeWidget_2.topLevelItem(n).text(0):
							item_c = QtWidgets.QTreeWidgetItem(self.treeWidget_2.topLevelItem(n),[event['name'],event['bottle'],event['room']])
							item_c.setCheckState(0,QtCore.Qt.Unchecked)
							addOrNo = 1
							break
				if addOrNo==0:
					item_t = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
					self.treeWidget_2.addTopLevelItem(item_t)
					item_t.setCheckState(0,QtCore.Qt.Unchecked)
					item_t.setText(0,event['action'])
					item_c = QtWidgets.QTreeWidgetItem(item_t,[event['name'],event['bottle'],event['room']])
					item_c.setCheckState(0,QtCore.Qt.Unchecked)
	def itemCheck(self,item):
		if item.parent() == None:
			if item.checkState(0) == QtCore.Qt.Checked:
				count = item.childCount()
				for c in range(count):
					item.child(c).setCheckState(0,QtCore.Qt.Checked)
			elif item.checkState(0) == QtCore.Qt.Unchecked:
				count = item.childCount()
				for c in range(count):
					item.child(c).setCheckState(0,QtCore.Qt.Unchecked)
	def createNewStocksInBatch(self):
		pList = ['传大厚或小厚第二批','传大厚或小厚第三批','收大薄或小薄第一批','收大薄或小薄第二批']
		p,ok = QInputDialog.getItem(MainWindow,'已勾选果蝇批量创建','注意：该功能将默认所勾选工作已完成\n请选择要创建的果蝇类型：',pList,0,False)
		if ok:
			i = 1 
			for item in pList:
				if p==item:
					self.delEvent(i)
					break
				i = i+1
#按下后将左上的五种input里的值保存入xml文件，如有基因型有重复，则默认为修改
	def addXmlStock(self):
		if self.flyName.text() and self.botNum.text():
			if self.nameRepeat(self.flyName.text()):
				QMessageBox.information(MainWindow,"注意","名字不能重复!!")
			else:
				if self.dateP.currentIndex()==0:
					templateName = self.getTemplateName(self.patternT.currentIndex(),self.envT.currentIndex())
				else:
					templateName = self.dateP.currentText()
				s = {'name':self.flyName.text(),'startdate':self.dateEdit.date().toString(format=QtCore.Qt.ISODate),'bottlenum':self.botNum.text(),'pattern':str(self.patternT.currentIndex()),'envtem':str(self.envT.currentIndex()),'color':str(self.colorP.currentIndex())}
				item = self.addStock(s,templateName)
				self.treeWidget.clear()
				if item:
					xmltoday = self.doc.find('today')
					node = ET.SubElement(xmltoday, 'toBeDone')
					node.set('action',item['action'])
					node.set('name',item['name'])
					node.set('bottle',item['bottle'])
					node.set('room',item['room'])
				self.doc.write(self.curFilename,encoding="utf-8",xml_declaration=True,method="xml")
				self.loadFile(self.curFilename)
		else:
			QMessageBox.information(MainWindow,"注意","名称和瓶数为必填项！")
	def getTemplateName(self, p_n, e_n):
		templateName = ''
		if e_n==0:
			if p_n==0 or p_n==3:
				templateName = '23度大厚新蝇'
			elif p_n==1:
				templateName = '23度大厚老蝇'
			elif p_n==2:
				templateName = '23度大薄'
		elif e_n == 1:	
			if p_n==0 or p_n==3:
				templateName = '18度大厚新蝇'
			elif p_n==1:
				templateName = '18度大厚老蝇'
			elif p_n==2:
				templateName = '18度大薄'
		elif e_n == 2:
			templateName='23度大厚新蝇'
		return templateName

#向xml树里加入stock信息功能函数：	
	def addStock(self,newstock,templateName):
		root = self.doc.getroot()
		stock = ET.SubElement(root, 'stock')
		stock.set('name',newstock['name'])

		startdate = ET.SubElement(stock, 'startdate')
		startdate.text = newstock['startdate']

		bottlenum = ET.SubElement(stock, 'bottlenum')
		bottlenum.text = newstock['bottlenum']

		pattern = ET.SubElement(stock, 'pattern')
		pattern.text = newstock['pattern']

		envtem = ET.SubElement(stock, 'envtem')
		envtem.text = newstock['envtem']

		targetdate = ET.SubElement(stock, 'targetdate')
		targetdate.text = newstock['startdate']

		color = ET.SubElement(stock,'color')
		color.text = newstock['color']

		for template in self.templateWindow.root.iter('template'):
			if template.get('name')==templateName:
				period = template.find('period')
				stock.append(period)
		item = self.getEvent(stock,date.today())
		return item

	def getEvent(self,stock,dateNeed):
		differ = dateNeed-self.string2Date(stock.find('targetdate').text)
		x = differ.days%int(stock.find('period').get('days'))
		episodes = stock.iter('episode')
		item = {}
		temperature={'0':'23度','1':'18度','2':'其他'}
		if x==0:
			item = {'action':stock.find('period').get('action'),'name':stock.get('name'),'bottle':stock.find('bottlenum').text,'room':temperature[stock.find('envtem').text]}
			if  dateNeed==date.today():
				stock.find('targetdate').text = date.today().isoformat()
				self.doc.write(self.curFilename,encoding="utf-8",xml_declaration=True,method="xml")
		elif episodes:
			for episode in episodes:
				if x==int(episode.text):
					item={'action':episode.get('action'),'name':stock.get('name'),'bottle':stock.find('bottlenum').text,'room':temperature[stock.find('envtem').text]}
		return item
#判断果蝇名是否重复
	def nameRepeat(self, name):
		root = self.doc.getroot()
		stocks = root.iter('stock')
		for stock in stocks:
			if name == stock.get('name'):
				return True
		return False
#按下后将treeWidget里选中的基因型删掉，同时删掉xml文件里的相关
	def delXmlStock(self):
		xmlRoot = self.doc.getroot()
		item = QtWidgets.QTreeWidgetItemIterator(self.treeWidget)
		while item.value():
			stocks = xmlRoot.iter('stock')
			if item.value().checkState(0) == QtCore.Qt.Checked:
				for stock in stocks:
					if stock.get('name')==item.value().text(0):
						stock.clear()
						xmlRoot.remove(stock)
				self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(item.value()))
			else:
				item = item.__iadd__(1)
		self.doc.write(self.curFilename,encoding="utf-8",xml_declaration=True,method="xml")
#按下后，treeWidget_2里选中的事件删除，同时对xml里today下的子项进行修改（不用传到下一天）
	def delEvent(self,i=0):
		if self.string2Date(self.calendarWidget.selectedDate().toString(format=QtCore.Qt.ISODate))==date.today():
			xmlRoot = self.doc.getroot()
			item = QtWidgets.QTreeWidgetItemIterator(self.treeWidget_2)
			l1 = []
			xmlToday = xmlRoot.find('today')
			while item.value():
				if item.value().parent() and item.value().checkState(0) == QtCore.Qt.Checked:
					l1 = l1+[[item.value().parent().text(0),item.value().text(0)]]
					item.value().parent().removeChild(item.value())
				else:
					item = item.__iadd__(1)
			if l1:
				for data in l1:
					for node in xmlToday.iter("toBeDone"):
						if node.get('action')==data[0] and node.get('name') == data[1]:
							xmlToday.remove(node)
					if i>0:
						nametail = ['_2','_3','_薄','_2薄']
						for stock in xmlRoot.iter('stock'):
							if data[1] == stock.get('name'):
								s = {'name':stock.get('name')+nametail[i-1],'startdate':date.today().isoformat(),'bottlenum':stock.find('bottlenum').text,'pattern':str(int((i+1)/2)),'envtem':stock.find('envtem').text,'color':stock.find('color').text}
								templateName = self.getTemplateName(int((i+1)/2),int(stock.find('envtem').text))
								item = self.addStock(s,templateName)
								self.treeWidget.clear()
			self.doc.write(self.curFilename,encoding="utf-8",xml_declaration=True,method="xml")
			self.loadFile(self.curFilename)
#打开模板窗口	
	def openTemplate(self):
		self.templateWindow.show()
		self.templateWindow.templateListShow()
		self.templateWindow.listWidget.setCurrentRow(0)
		self.templateWindow.tableWidget.clearContents()
		self.templateWindow.templateContent()
		self.templateWindow.button_save.clicked.connect(self.saveTemplate)
		self.templateWindow.button_delete.clicked.connect(self.deleteTemplate)
#根据模板安装其他模式的item
	def datePRefresh(self):
		self.dateP.clear()
		self.dateP.addItem("")
		root_t = self.templateWindow.root
		a = 0
		for template in root_t.iter('template'):
			if a>5:
				self.dateP.addItem(template.get('name'))
			a = a+1
	def saveTemplate(self):
		self.templateWindow.listWidget.closePersistentEditor(self.templateWindow.listWidget.currentItem())
		if self.templateWindow.listWidget.currentItem().text() and self.templateWindow.tableWidget.item(0,0) and self.templateWindow.tableWidget.item(0,1):
			if self.templateWindow.listWidget.count() == self.templateWindow.tCount:
				templates = self.templateWindow.root.iter('template')
				i=0
				j = self.templateWindow.listWidget.currentRow()
				for template in templates:
					if i == j:
						self.templateWindow.template2xml(template)
						break
					else:
						i = i+1
			elif self.templateWindow.listWidget.count() >self.templateWindow.tCount:
				template = ET.SubElement(self.templateWindow.root,'template')
				self.templateWindow.template2xml(template)
			self.templateWindow.tree.write("template.xml",encoding="utf-8",xml_declaration=True,method="xml")
			self.datePRefresh()
			self.templateWindow.templateListShow()
			self.templateWindow.listWidget.setCurrentRow(0)
			self.templateWindow.templateContent()
		else:
			QMessageBox.information(MainWindow,"注意","模板名称和周期信息为必填项！")
#删除模板后更新‘其他模式’的item
	def deleteTemplate(self):
		templates = self.templateWindow.root.iter('template')
		deleteItem = self.templateWindow.listWidget.currentItem()
		for template in templates:
			if template.get('name') == deleteItem.text():
				self.templateWindow.root.remove(template)
				self.templateWindow.tree.write("template.xml",encoding="utf-8",xml_declaration=True,method="xml")
				break
		self.templateWindow.listWidget.takeItem(self.templateWindow.listWidget.currentRow())
		self.datePRefresh()
		self.templateWindow.templateListShow()
		self.templateWindow.listWidget.setCurrentRow(0)
		self.templateWindow.templateContent()
#双击list里的果蝇名称后弹出data窗口
	def dateShow(self):
		text = self.treeWidget.currentItem().text(0)
		if text:
			l = []
			l.append(text)
			stocks = self.doc.getroot().iter('stock')
			for stock in stocks:
				if text == stock.get('name'):
					l.append(stock.find('startdate').text)
					l.append(stock.find('targetdate').text)
					l.append(stock.find('bottlenum').text)
					l.append(stock.find('pattern').text)
					l.append(stock.find('envtem').text)
					l.append(stock.find('color').text)
					period = stock.find('period')
					l.append(period.get('action'))
					l.append(period.get('days'))
					episodes = period.iter('episode')
					if episodes:
						for episode in episodes:
							l.append(episode.get('action'))
							l.append(episode.text)
			self.dateWindow.setContent(l)
			self.dateWindow.pushButton_d.clicked.connect(self.dateChange)
			self.dateWindow.show()
	def dateChange(self):
		name = self.dateWindow.flyName_d.text()
		if name and self.dateWindow.botNum_d.text() and self.dateWindow.tableWidget_d.item(0,0) and self.dateWindow.tableWidget_d.item(0,1):
			root = self.doc.getroot()
			stocks = root.iter('stock')
			for stock in stocks:
				if name == stock.get('name'):
					stock.find('targetdate').text = self.dateWindow.dateEdit_d.date().toString(format=QtCore.Qt.ISODate)
					stock.find('bottlenum').text = self.dateWindow.botNum_d.text()
					stock.find('pattern').text = str(self.dateWindow.patternT_d.currentIndex())
					stock.find('envtem').text = str(self.dateWindow.envT_d.currentIndex())
					stock.find('color').text = str(self.dateWindow.colorP_d.currentIndex())
					period = stock.find('period')
					period.clear()
					period.set('action',self.dateWindow.tableWidget_d.item(0,0).text())
					period.set('days',self.dateWindow.tableWidget_d.item(0,1).text())
					row = 1
					while self.dateWindow.tableWidget_d.item(row,0) and self.dateWindow.tableWidget_d.item(row,1) and (row<4):
						episode = ET.SubElement(period,'episode')
						episode.set('action',self.dateWindow.tableWidget_d.item(row,0).text())
						episode.text = self.dateWindow.tableWidget_d.item(row,1).text()
						row = row+1
					self.doc.write(self.curFilename,encoding="utf-8",xml_declaration=True,method="xml")
					break
			self.genetypeShow(self.curFilename,self.listP.currentIndex())
			date = self.string2Date(self.calendarWidget.selectedDate().toString(format=QtCore.Qt.ISODate))
			self.eventShow(self.curFilename,date)
		else:
			QMessageBox.information(MainWindow,"注意","瓶数、周期及操作为必填项！")
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		self.geneDisLabel.setText(_translate("MainWindow", "已添加基因型"))
		self.treeWidget.headerItem().setText(0, _translate("MainWindow", "名称"))
		self.treeWidget.headerItem().setText(1, _translate("MainWindow", "本周期开始日期"))
		self.delBtn.setText(_translate("MainWindow", "删除"))
		self.nameLabel.setText(_translate("MainWindow", "果蝇名"))
		self.datePLabel.setText(_translate("MainWindow", "其他模式"))
		self.envT.setItemText(0, _translate("MainWindow", "23度"))
		self.envT.setItemText(1, _translate("MainWindow", "18度"))
		self.envT.setItemText(2, _translate("MainWindow", "其他"))
		self.pushButton.setText(_translate("MainWindow", "保存"))
		self.numLabel.setText(_translate("MainWindow", "瓶数"))
		self.patternLabel.setText(_translate("MainWindow", "食物模式"))
		self.patternT.setCurrentText(_translate("MainWindow", "大厚新蝇"))
		self.patternT.setItemText(0, _translate("MainWindow", "大厚新蝇"))
		self.patternT.setItemText(1, _translate("MainWindow", "大厚老蝇或小厚"))
		self.patternT.setItemText(2, _translate("MainWindow", "大薄或小薄"))
		self.patternT.setItemText(3, _translate("MainWindow", "其他"))
		self.temTabel.setText(_translate("MainWindow", "蝇房"))
		self.colorTabel.setText(_translate("MainWindow", "颜色标签"))
		self.dateLabel.setText(_translate("MainWindow", "开始时间"))
		self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "名称"))
		self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "瓶数"))
		self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "蝇房"))
		__sortingEnabled = self.treeWidget_2.isSortingEnabled()
		self.treeWidget_2.setSortingEnabled(False)
		self.treeWidget_2.setSortingEnabled(__sortingEnabled)
		self.completeBtn.setText(_translate("MainWindow", "已完成"))
		self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
		self.menu_S.setTitle(_translate("MainWindow", "设置(&C)"))
		self.menu_H.setTitle(_translate("MainWindow", "帮助(&H)"))
		self.action_N.setText(_translate("MainWindow", "新建(&N)"))
		self.action_O.setText(_translate("MainWindow", "打开(&O)"))
		self.action_I.setText(_translate("MainWindow", "导入(&I)"))
		self.action_X.setText(_translate("MainWindow", "退出(&X)"))
		self.action_S.setText(_translate("MainWindow", "模板设置(&S)"))
		self.action_B.setText(_translate("MainWindow", "关于(&B)"))
		self.action_A.setText(_translate("MainWindow", "使用说明(&A)"))

class DateWindow(QWidget):
	def __init__(self,parent=None):
		super(DateWindow,self).__init__(parent)
		self.resize(300,500)
		self.formLayout_d = QtWidgets.QFormLayout(self)
		self.formLayout_d.setObjectName("formLayout_d")
		self.nameLabel_d = QtWidgets.QLabel("果蝇名称",self)
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(12)
		self.nameLabel_d.setFont(font)
		self.nameLabel_d.setObjectName("nameLabel_d")
		self.flyName_d = QtWidgets.QLineEdit(self)
		self.flyName_d.setFont(font)
		self.flyName_d.setObjectName("flyName_d")
		self.flyName_d.setReadOnly(True)
		self.formLayout_d.addRow(self.nameLabel_d,self.flyName_d)
		self.sdLabel_d = QtWidgets.QLabel("起始日期",self)
		self.sdLabel_d.setFont(font)
		self.sdLabel_d.setObjectName("sdLabel_d")
		self.startdate_d = QtWidgets.QLineEdit(self)
		self.startdate_d.setFont(font)
		self.startdate_d.setObjectName("startdate_d")
		self.startdate_d.setReadOnly(True)
		self.formLayout_d.addRow(self.sdLabel_d,self.startdate_d)
		self.dateEdit_d = QtWidgets.QDateEdit(self)
		self.dateEdit_d.setFont(font)
		self.dateEdit_d.setObjectName("dateEdit_d")
		self.dateLabel_d = QtWidgets.QLabel("周期起始",self)
		self.dateLabel_d.setFont(font)
		self.dateLabel_d.setObjectName("dateLabel_d")
		self.formLayout_d.addRow(self.dateLabel_d,self.dateEdit_d)
		self.numLabel_d = QtWidgets.QLabel("瓶数",self)
		self.numLabel_d.setFont(font)
		self.numLabel_d.setObjectName("numLabel_d")
		self.botNum_d = QtWidgets.QLineEdit(self)
		self.botNum_d.setFont(font)
		self.botNum_d.setObjectName("botNum_d")
		self.formLayout_d.addRow(self.numLabel_d,self.botNum_d)
		self.patternLabel_d = QtWidgets.QLabel("模式",self)
		self.patternLabel_d.setFont(font)
		self.patternLabel_d.setObjectName("patternLabel_d")
		self.patternT_d = QtWidgets.QComboBox(self)
		self.patternT_d.setFont(font)
		self.patternT_d.setEditable(False)
		self.patternT_d.setObjectName("patternT_d")
		self.patternT_d.addItem("大厚新蝇")
		self.patternT_d.addItem("大厚老蝇或小厚")
		self.patternT_d.addItem("大薄或小薄")
		self.patternT_d.addItem("其他")
		self.formLayout_d.addRow(self.patternLabel_d,self.patternT_d)
		self.envT_d = QtWidgets.QComboBox(self,)
		self.envT_d.setFont(font)
		self.envT_d.setObjectName("envT")
		self.envT_d.addItem("23度")
		self.envT_d.addItem("18度")
		self.envT_d.addItem("其他")
		self.temTabel_d = QtWidgets.QLabel("蝇房温度",self)
		self.temTabel_d.setFont(font)
		self.temTabel_d.setObjectName("temTabel")
		self.formLayout_d.addRow(self.temTabel_d,self.envT_d)
		self.colorTabel_d = QtWidgets.QLabel("颜色标签",self)
		self.colorTabel_d.setFont(font)
		self.colorTabel_d.setObjectName("colorTabel_d")
		self.colorP_d = QtWidgets.QComboBox(self)
		self.colorP_d.setObjectName("colorP_d")
		pix = QtGui.QPixmap(QtCore.QSize(200,20))
		pix.fill(QtGui.QColor(244,208,0))
		self.colorP_d.addItem("")
		self.colorP_d.addItem(QtGui.QIcon(pix),"")
		pix.fill(QtGui.QColor(107,194,53))
		self.colorP_d.addItem(QtGui.QIcon(pix),"")
		pix.fill(QtGui.QColor(1,165,175))
		self.colorP_d.addItem(QtGui.QIcon(pix),"")
		self.colorP_d.setIconSize(QtCore.QSize(200,20))
		self.formLayout_d.addRow(self.colorTabel_d,self.colorP_d)
		self.tableWidget_d = QtWidgets.QTableWidget(self)
		self.tableWidget_d.setFont(font)
		self.tableWidget_d.setObjectName("tableWidget_d")
		self.tableWidget_d.setRowCount(4)
		self.tableWidget_d.setColumnCount(2)
		self.tableWidget_d.setHorizontalHeaderLabels(['操作','天数'])
		self.tableWidget_d.setVerticalHeaderLabels(['周期','周期内操作','周期内操作','周期内操作'])
		self.formLayout_d.addRow(self.tableWidget_d)
		self.pushButton_d = QtWidgets.QPushButton("保存",self)
		self.pushButton_d.setFont(font)
		self.pushButton_d.setObjectName("pushButton")
		self.formLayout_d.addRow("",self.pushButton_d)
	def setContent(self, l):
		self.flyName_d.setText(l[0])
		self.startdate_d.setText(l[1])
		self.dateEdit_d.setDate(self.string2Date(l[2]))
		self.botNum_d.setText(l[3])
		self.patternT_d.setCurrentIndex(int(l[4]))
		self.envT_d.setCurrentIndex(int(l[5]))
		self.colorP_d.setCurrentIndex(int(l[6]))
		length = int((len(l)-7)/2)
		for i in range(length):
			newItem = QtWidgets.QTableWidgetItem(l[2*i+7])
			self.tableWidget_d.setItem(i,0,newItem)
			newItem = QtWidgets.QTableWidgetItem(l[2*i+8])
			self.tableWidget_d.setItem(i,1,newItem)
	def string2Date(self,s):
		dTType = datetime.strptime(s,'%Y-%m-%d')
		s = date(dTType.year,dTType.month,dTType.day)
		return s
		
class TemplateSetting(QWidget):
	def __init__(self,parent=None):
		super(TemplateSetting,self).__init__(parent)
		self.resize(800,600)
		self.setWindowTitle("模板设置")
		grid = QGridLayout()
		font = QtGui.QFont()
		font.setFamily("微软雅黑")
		font.setPointSize(14)
		self.label_1 = QtWidgets.QLabel("模板列表",self)
		self.label_1.setObjectName("label_1")
		self.label_1.setFont(font)
		grid.addWidget(self.label_1,0,0,1,2)
		self.label_2 = QtWidgets.QLabel("模板详情",self)
		self.label_2.setObjectName("label_2")
		self.label_2.setFont(font)
		grid.addWidget(self.label_2,0,2,1,2)
		self.listWidget = QtWidgets.QListWidget(self)
		self.listWidget.setFont(font)
		self.listWidget.setObjectName("listWidget")
		grid.addWidget(self.listWidget,1, 0, 1, 2)
		self.tableWidget = QtWidgets.QTableWidget(self)
		self.tableWidget.setFont(font)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setRowCount(4)
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setHorizontalHeaderLabels(['操作','天数'])
		self.tableWidget.setVerticalHeaderLabels(['周期','周期内操作','周期内操作','周期内操作'])
		grid.addWidget(self.tableWidget,1, 2, 1, 2)
		self.button_new = QtWidgets.QPushButton("新建模板",self)
		self.button_new.setFont(font)
		self.button_new.setObjectName("button_new")
		grid.addWidget(self.button_new, 2, 0)
		self.button_save = QtWidgets.QPushButton("保存模板",self)
		self.button_save.setFont(font)
		self.button_save.setObjectName("button_save")
		grid.addWidget(self.button_save, 2, 1)
		self.button_delete = QtWidgets.QPushButton("删除模板",self)
		self.button_delete.setFont(font)
		self.button_delete.setObjectName("button_delete")
		grid.addWidget(self.button_delete, 2, 2)
		self.button_exit = QtWidgets.QPushButton("退出",self)
		self.button_exit.setFont(font)
		self.button_exit.setObjectName("button_exit")
		grid.addWidget(self.button_exit, 2, 3)
		self.setLayout(grid)
		self.templateFile = os.getcwd()+'/template.xml'
		self.tree = ET.parse(self.templateFile)
		self.root = self.tree.getroot()
		self.tCount = 0

		self.listWidget.itemDoubleClicked.connect(self.editName)
		self.listWidget.itemClicked.connect(self.templateContent)
		self.button_new.clicked.connect(self.newTemplate)
		self.button_exit.clicked.connect(self.close)
	def editName(self,item):
		i = self.listWidget.row(item)
		if i>5:
			self.listWidget.openPersistentEditor(item)
		else:
			QMessageBox.information(MainWindow,"注意","固有模板只能修改参数，不可改名！")

	def templateListShow(self):
		self.listWidget.clear()
		templates = self.root.iter('template')
		self.tCount = 0
		for template in templates:
			self.tCount = self.tCount + 1
			self.listWidget.addItem(template.get("name"))

	def templateContent(self):
		self.tableWidget.clearContents()
		item_text = self.listWidget.currentItem().text()
		templates = self.root.iter('template')
		for template in templates:
			if template.get("name") == item_text:
				period = template.find('period')
				newItem = QtWidgets.QTableWidgetItem(period.get('action'))
				self.tableWidget.setItem(0,0,newItem)
				newItem = QtWidgets.QTableWidgetItem(period.get('days'))
				self.tableWidget.setItem(0,1,newItem)
				i = 1
				for episode in template.iter('episode'):
					newItem = QtWidgets.QTableWidgetItem(episode.get('action'))
					self.tableWidget.setItem(i,0,newItem)
					newItem = QtWidgets.QTableWidgetItem(episode.text)
					self.tableWidget.setItem(i,1,newItem)
					i = i+1

	def newTemplate(self):
		self.listWidget.addItem("新建模板(双击改名)")
		self.tableWidget.clearContents()

	def template2xml(self, template):
		template.set("name",self.listWidget.currentItem().text())
		if template.find('period'):
			template.remove(template.find('period'))
		period = ET.SubElement(template,'period')
		period.set('action',self.tableWidget.item(0,0).text())
		period.set('days',self.tableWidget.item(0,1).text())
		i = 1
		while self.tableWidget.item(i,0) and self.tableWidget.item(i,1) and (i<4):
			episode = ET.SubElement(period,'episode')
			episode.set('action',self.tableWidget.item(i,0).text())
			episode.text = self.tableWidget.item(i,1).text()
			i = i+1



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
