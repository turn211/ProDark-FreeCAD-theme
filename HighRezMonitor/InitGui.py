from PySide import QtGui
f=QtGui.QApplication.font()
f.pointSize()
f.setPointSize(10) # replace 10 with whatever size you want for 2k to 4k monitors
f=QtGui.QApplication.setFont(f)