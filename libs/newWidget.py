#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    # needed for py3+qt4
    # Ref:
    # http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html
    # http://stackoverflow.com/questions/21217399/pyqt4-qtcore-qvariant-object-instead-of-a-string
    if sys.version_info.major >= 3:
        import sip
        sip.setapi('QVariant', 2)
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *



class NewWidget(QDockWidget):
    newSignal = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super(NewWidget, self).__init__(*args, **kwargs)
        self.items = []
        self.fileListWidget = QListWidget()
        self.fileListWidget.itemDoubleClicked.connect(self.itemDoubleClicked)
        filelistLayout = QVBoxLayout()
        filelistLayout.setContentsMargins(0, 0, 0, 0)
        filelistLayout.addWidget(self.fileListWidget)
        fileListContainer = QWidget()
        fileListContainer.setLayout(filelistLayout)
        self.filedock = QDockWidget('NewWidget', self)
        self.filedock.setObjectName('NewWidget')
        self.filedock.setWidget(fileListContainer)

    def itemDoubleClicked(self):
        print('click')
        self.newSignal.emit('emit')
