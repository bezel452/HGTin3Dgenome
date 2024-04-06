import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMenu, QFileDialog, qApp, QAction, QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QHBoxLayout,QWidget, QLineEdit, QRadioButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from plt_3D import get_axl, get_HGTaxl

class MplCanvas(FigureCanvas):
    def __init__(self):
        fig = plt.figure(figsize = (60, 36))
    
        plt.rcParams['figure.facecolor'] = 'black'
        plt.rcParams['axes.facecolor'] = 'black'
        plt.rcParams['savefig.facecolor'] = 'black'
        self.axl = fig.add_subplot(111, projection='3d')
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mcool = ""
        self.anno = ""
        self.axlF = ""
        self.res = 1000000
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setGeometry(1000, 300, 800, 1000)
        self.setWindowTitle('PLT3D')
        self.statusBar().showMessage('Ready!')
        
        
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
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAct)

        self.canvas = MplCanvas()
        self.canvas.axl.set_axis_off()

# self.txt.text() is the value in the text table.

        vbox1 = QVBoxLayout()
        
        vbox1.addWidget(btn1)
        vbox1.addWidget(btn2)
        vbox1.addWidget(btn3)
        vbox1.addWidget(check1)
        vbox1.addWidget(check2)
        vbox1.addWidget(btn4)
        vbox1.addWidget(self.canvas)
        central = QWidget()
        central.setLayout(vbox1)
        self.setCentralWidget(central)
        
        

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        exitAct = cmenu.addAction('Exit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == exitAct:
            qApp.quit()

    def select_file1(self):
        self.statusBar().showMessage("Select Cooler Files")
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Cooler File(*.mcool)')
        
        if file:
            print(file)
            self.mcool = file

    def select_file2(self):
        self.statusBar().showMessage("Select Axis Files")
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files(*)')
        
        if file:
            print(file)
            self.axlF = file

    def select_file3(self):
        self.statusBar().showMessage("Select Annotation Files")
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files(*)')
        
        if file:
            print(file)
            self.anno = file
    def checkClick(self):
        if self.sender().text() == '1M':
            self.res = 1000000
            print(self.res)
        else:
            self.res = 500000
            print(self.res)
        
    
    def generate_figure(self):
        self.draw_plot(self.anno, self.mcool, self.axlF, self.res)

    def draw_plot(self, anno, file, axl, res):
        x, y, z, chrom_col, chrom_dic, data = get_axl(file, res, axl)
        H_x, H_y, H_z = get_HGTaxl(res, file, anno, data)
        chl = list(chrom_dic.values())
        chl = chl[:-1]
        tps = []
        for i in range(len(x)):
            t = self.canvas.axl.plot(x[i], y[i], z[i], c=chrom_col[i])
            tps.append(t[0])
        self.canvas.axl.scatter(H_x, H_y, H_z, c="yellow")
        self.canvas.axl.legend(tps, chl, facecolor='white')
        self.canvas.draw()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    sys.exit(app.exec_())