import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTextEdit, QMenu, QFileDialog, qApp, QAction, QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QHBoxLayout,QWidget, QLineEdit, QRadioButton, QDockWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from plt_3D import get_axl
from HGTcopy import copy_proc
import numpy as np

class MplCanvas(FigureCanvas):
    def __init__(self):
        fig = plt.figure(figsize = (80, 72))
        plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)
        plt.rcParams['figure.facecolor'] = 'black'
        plt.rcParams['axes.facecolor'] = 'black'
        plt.rcParams['savefig.facecolor'] = 'black'
        self.axl = fig.add_subplot(111, projection='3d')
        self.axl.set_box_aspect([1,1,1])
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mcool = ""
        self.anno = ""
        self.axlF = ""
        self.res = 1000000
        self.cwd = os.getcwd()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setGeometry(1000, 300, 1200, 1300)
        self.setWindowTitle('PLT3D')
        self.statusBar().showMessage('Ready!')

#        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#        self.setWindowOpacity(0.5)
        dock = QDockWidget('Action Bar')
        btn1 = QPushButton('SELECT COOLER FILE', self)
#        self.btn1.setGeometry(160, 50, 150, 30)
        btn1.clicked.connect(self.select_file1)
        btn2 = QPushButton('SELECT AXIS FILE', self)
        btn2.clicked.connect(self.select_file2)
        btn3 = QPushButton('SELECT ANNO FILE', self)
        btn3.clicked.connect(self.select_file3)
        btn4 = QPushButton('GENERATE THE FIGURE', self)
        btn4.clicked.connect(self.generate_figure)

        check1 = QRadioButton('1M')
        check1.setChecked(True)
        check1.toggled.connect(self.checkClick)
        check2 = QRadioButton('500K')
        check2.toggled.connect(self.checkClick)
        
        exitAct = QAction('Quit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit the program')
        exitAct.triggered.connect(qApp.quit)
        saveAct = QAction('Save', self)
        saveAct.triggered.connect(self.saveFigure)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save the figure')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)

        self.canvas = MplCanvas()
        self.canvas.axl.set_axis_off()

# self.txt.text() is the value in the text table.
        dock.setFeatures(QDockWidget.DockWidgetMovable)
        dock2 = QDockWidget('Status')
        dock2.setFeatures(QDockWidget.DockWidgetMovable)
        self.mes = QTextEdit()
        
        vbox1 = QVBoxLayout()
        
        vbox1.addWidget(btn1)
        vbox1.addWidget(btn2)
        vbox1.addWidget(btn3)
        vbox1.addWidget(check1)
        vbox1.addWidget(check2)
        vbox1.addWidget(btn4)
        
        
        central = QWidget()
        central.setLayout(vbox1)
        dock.setWidget(central)
        dock2.setWidget(self.mes)
        '''
        self.setCentralWidget(central)
        '''
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, dock2)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
        self.setCentralWidget(self.canvas)

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        exitAct = cmenu.addAction('Exit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == exitAct:
            qApp.quit()

    def select_file1(self):
        self.statusBar().showMessage("Select Cooler File")
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Cooler File(*.mcool)')
        
        if file:
            print(file)
            self.mcool = file
            self.mess('Cooler File: ' + file)

    def select_file2(self):
        self.statusBar().showMessage("Select Axis File")
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files(*)')
        
        if file:
            print(file)
            self.axlF = file
            self.mess('Axis File: ' + file)

    def select_file3(self):
        self.statusBar().showMessage("Select Annotation File")
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files(*)')
        
        if file:
            print(file)
            self.anno = file
            self.mess('Annotation File: ' + file)

    def mess(self, x):
        self.mes.append(x)

    def checkClick(self):
        if self.sender().text() == '1M':
            self.res = 1000000
            print(self.res)
        else:
            self.res = 500000
            print(self.res)
        
    
    def generate_figure(self):
        if self.anno == "" or self.mcool == "" or self.axlF == "":
            self.mess('Need More Information Files')
        else:
            self.draw_plot(self.anno, self.mcool, self.axlF, self.res)
            self.mess('Generating Completed')

    def getHGT(self, axldata, anno_file, cool_file, resolution):
        HGT, gene = copy_proc(cool_file, anno_file, resolution)
        H_x = list()
        H_y = list()
        H_z = list()
        for idx, _, _, _, cnt in HGT:
            tmp = axldata[idx]
            if np.isnan(tmp[0]):
                continue
            H_x.append(tmp[0])
            H_y.append(tmp[1])
            H_z.append(tmp[2])
        return H_x, H_y, H_z

    def draw_plot(self, anno, file, axl, res):
        x, y, z, chrom_col, chrom_dic, data = get_axl(file, res, axl)
        H_x, H_y, H_z = self.getHGT(data, anno, file, res)
        chl = list(chrom_dic.values())
        chl = chl[:-1]
        tps = []
        for i in range(len(x)):
            t = self.canvas.axl.plot(x[i], y[i], z[i], c=chrom_col[i])
            tps.append(t[0])
        self.canvas.axl.scatter(H_x, H_y, H_z, c="yellow")
        self.canvas.axl.legend(tps, chl, facecolor='white')
        self.canvas.draw()

    def saveFigure(self):
        file, _ = QFileDialog.getSaveFileName(self, 'Save the figure', self.cwd, 'All Files(*);;PDF Files(*.pdf);;PNG Files(*.png)')
        if file:
            self.mess('Save the figure' + file)
            plt.savefig(file)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    sys.exit(app.exec_())