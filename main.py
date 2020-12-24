# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import gui
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import json
import conf
colors = ['#00ff00', '#ff7033', '#ff0000']
limits = [3.287, 3.285]
def jsonRefresh():
    global jdata
    print("works")
    file = open('/home/max/allParams.json', 'r')
    jdata = json.loads(file.read())


class configureWindow(QtWidgets.QMainWindow, conf.Ui_wnd_configure):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.doubleValidator = QtGui.QDoubleValidator(2.222, 3.999, 3)
        # self.btn_warning.clicked.connect(self.buttonPress)
        # set buttons color according user choice  <in global dictionary
        self.buttonGroup.buttonClicked.connect(self.buttonPress)
        x = 2
        for button in self.buttonGroup.buttons():
            button.setStyleSheet("background-color:" + colors[x])
            x -= 1

        self.edt_crytical.setText(str(limits[1]))
        self.edt_warning.setText(str(limits[0]))
        # self.edt_ok.setInputMask("000")
        # lineEdit->setValidator(new QDoubleValidator(-999.0, 999.0, 2, lineEdit));
        self.edt_crytical.setValidator(self.doubleValidator)  # , self.edt_crytical))
        self.edt_warning.setValidator(self.doubleValidator)
        self.edt_crytical.textChanged.connect(self.edt_changed)
        # ob = self.buttonGroup.
        # print(button)
        # QtGui.QColor

    # self.pushButton.clicked.connect(self.buttonPress)

    # QtWidgets.QColorDialog::getColor(blue
    # clWin = QtWidgets.QAction("Quit", self)
    # clWin.triggered.connect(self.closeWin)

    def closeEvent(self, event):
        # print("closing..")
        # Battery.reshowWin(self)
        #save limits value
        limits[0] = float(self.edt_warning.text())
        limits[1] = float(self.edt_crytical.text())
        self.close()
        Battery.reshowWin(self)

    def edt_changed(self):
        print("text changed")

    def buttonPress(self, button):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            # self.btn_warning.setStyleSheet("background-color:" + color.name())
            button.setStyleSheet("background-color:" + color.name())
            # self.buttonGroup
            print(self.buttonGroup.id(button))
            print(color.name())
            # save color
            colors[4 + self.buttonGroup.id(button)] = color.name()
            # Battery.colors[1] = 0
            # print(Battery.colors)




class Battery(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    global jdata
    global CellsImage
    #constant
    global battery
    battery = 'bt1'
    global cellMinValue
    global cellMaxValue
    global cellsCount
    global CellsImage
    cellsCount = 15
    cellMinValue = 3240
    cellMaxValue = 3300
    CellsImage = []



    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.readBattery()
        self.paintCells()
        self.refreshCells()
        self.btn_graphic_sett.clicked.connect(self.settings)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(10)
        #self.tableWidget.


    def reshowWin(self):
        #self.close()
        self.twow = Battery()
        self.twow.show()

    def settings(self):
        self.setVisible(False)
        self.twow = configureWindow()
        self.setFocus(True)
        self.twow.show()
    #def CellsRefresh(self):
    def readBattery(self):
        #battery model
        self.lbl_batModel.setText(jdata['bt1']['80']['Battery ID'])
        #battery charge
        value = int(float(jdata['bt1']['42']['Actual Charge %']) * 10)
        self.progressBar.setValue(value)
    def paintCells(self):
        #self.prBar = QtWidgets.QProgressBar()
        #self.cellsPlace.addWidget()
        cellsCount = 15
        cellWidth = 15
        cellHeight = 100

        lastHPosition = 0
        for i in range(cellsCount):
            CellsImage.append(QtWidgets.QProgressBar(self))
            CellsImage[i].setOrientation(2)
            CellsImage[i].setMaximum(cellMaxValue)
            CellsImage[i].setMinimum(cellMinValue)
            CellsImage[i].setTextVisible(0)
            CellsImage[i].setGeometry(lastHPosition, 0, cellWidth, cellHeight)
            #CellsImage[i].setStyleSheet(#"QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}"
                                       #"QProgressBar::chunk {background:#ff1100}")
            lastHPosition += cellWidth + 2
            CellsImage[i].setValue(50)
            self.cellsPlace.addWidget(CellsImage[i])

    def refreshCells(self):
        keyData = jdata[battery]['42']
        phrase = 'Cell Voltage_0'
        for i in range(cellsCount):
            if i == 9:
                phrase = 'Cell Voltage_'
            str_value = keyData[phrase + str(i + 1)]
            value = float(str_value)
            #define the battery level : ok, alarm or Crytical
            if value <= limits[1]:
                level = 2
            elif value <= limits[0]:
                level = 1
            else:
                level = 0
            CellsImage[i].setValue(int(value * 1000))
            c_color = "QProgressBar::chunk {background:" + colors[level] + "}"
            CellsImage[i].setStyleSheet(c_color)
            #CellsImage[i].setStyleSheet("QProgressBar::chunk {background:#ff1100}")
            #print(int(value * 1000))

        #self.paintCells(self.progress)
        #progress.setGeometry(0, 0, 300, 25)
        #self.progress.setMaximum(100)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app = QtWidgets.QApplication(sys.argv)
    jsonRefresh()
    bat = Battery()
    bat.show()
    #n = nprogressBar()
    #n.show()

    sys.exit(app.exec())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
