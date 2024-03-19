import qrcode                  #"pip install pyqrcode" to install 'qrcode' for importation in Python
from PIL import Image          #"pip install pillow" to open created QR Code
value=str(input("Enter String or Link: "))
qrImg=qrcode.make(value)       #Generates a QR Code
qrImg.save("qr-img.jpg")       #Saving Image File
print("QR Code saved as 'qr-img.jpg'")
img=Image.open("qr-img.jpg")   #Creating an Object of Image
img.show()                     #Display the QR Code