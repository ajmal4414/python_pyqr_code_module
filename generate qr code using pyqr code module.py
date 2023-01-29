#import QRcode from  pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
#string which represent QRcode
str="helloworld"

#url
url= pyqrcode.create(str)

#create and save the svg file naming "myqr.svg"

url.svg("myqr.svg",scale= 8)

#create and save png file naming "myqr.png"
url.png("myqr.png", scale= 6)