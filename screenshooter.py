import sys
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *


class Screen(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        # Uygulamanın durumunu kontrol etmek
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def wait_load(self,delay=0):
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self,result):
        self._loaded = True

    def get_image(self,url):
        self.load(QUrl(url))
        self.wait_load()

        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())

        image = QImage(self.page().viewportSize(),QImage.Format_ARGB32)
        # QPainter. Get_image işlevi tek bir parametre alır: hedefimiz
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        return image



