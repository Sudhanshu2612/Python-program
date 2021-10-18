from PySide6.QtWidgets import QApplication, QMainWindow , QLabel
from PySide6.QtGui import QIcon , QPixmap ,QImage
import sys
import requests


url = 'https://www.nasa.gov/sites/default/files/styles/full_width/public/thumbnails/image/stsci-01fhref5sgr4pfn9cytcvkt8gq.jpg?itok=iy0fNinG'
app  =  QApplication([])

image  = QImage()
image.loadFromData(requests.get(url).content)

image_label = QLabel()
image_label.setPixmap(QPixmap(image))
image_label.show()

app.exec_()