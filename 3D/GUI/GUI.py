import sys
from PyQt5.QtWidgets import QMenu, QFileDialog, qApp, QAction, QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QHBoxLayout,QWidget, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from plt_3D import get_axl, get_HGTaxl

class MplCanvas(FigureCanvas):
    def __init__(self):
        fig = plt.figure(figsize = (15, 9))
    
        plt.rcParams['figure.facecolor'] = 'black'
        plt.rcParams['axes.facecolor'] = 'black'
        plt.rcParams['savefig.facecolor'] = 'black'
        self.axl = fig.add_subplot(111, projection='3d')
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('PLT3D')
        self.statusBar().showMessage('Ready!')
        self.txt = QLineEdit("Input Resolution", self)
        
        self.btn1 = QPushButton('SELECT FILES', self)
#        self.btn1.setGeometry(160, 50, 150, 30)
        self.btn1.clicked.connect(self.select_file)
        exitAct = QAction('Quit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit the program')
        exitAct.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAct)
        self.txt.selectAll()
        self.txt.setFocus()
#        self.txt.setGeometry(10, 50, 150, 30)
        self.canvas = MplCanvas()
        self.canvas.axl.set_axis_off()
#        self.setCentralWidget(self.canvas)
# self.txt.text() is the value in the text table.
        '''
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.txt)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        '''
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.txt)
        vbox1.addWidget(self.btn1)
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
    def select_file(self):
        self.statusBar().showMessage("Select multiple Files")
        files, _ = QFileDialog.getOpenFileNames(self, 'Open Files', '', 'All Files(*)')
        
        if files:
            print(self.txt.text())
            print(files)
            self.draw_plot(files[0], files[1], files[2], self.txt.text())


    def draw_plot(self, anno, file, axl, res):
        x, y, z, chrom_col, chrom_dic, data = get_axl(file, res, axl)
        H_x, H_y, H_z = get_HGTaxl(res, file, anno, data)
        chl = list(chrom_dic.values())
        chl = chl[:-1]
 #       tps = []
        for i in range(len(x)):
            t = self.canvas.axl.plot(x[i], y[i], z[i], c=chrom_col[i])
#            tps.append(t)
        self.canvas.axl.scatter(H_x, H_y, H_z, c="yellow")
        
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    sys.exit(app.exec_())