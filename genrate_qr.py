# QR code program by qrcode module 
import qrcode 

# Data to encode
data = "https://github.com/Vishwas-verma2006"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data
qr.add_data(data)

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="red")

# Save the image
img.save("D:\CODING\python language\qr code\QR Images\custom_qr2.png")

# This message will appear on the terminal ! 
print("File save successfullly as custom_qr2.png at D drive on the folder the script !")