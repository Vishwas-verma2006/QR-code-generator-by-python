# progrma to genrat a qr code using PIL 
from PIL import Image
import qrcode

# Step 1: Create QR code
data = "https://github.com/Vishwas-verma2006"
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(data)

# Step 2: Generate image
img = qr.make_image(fill_color="white", back_color="black")

# Step 3: Save the image by save function of qrcode module 
img.save("D:\CODING\python language\qr code\qr.png")
print("Image saved as qr.png")

# Step 4: Diaplay using PIL by show() function 
img.show()