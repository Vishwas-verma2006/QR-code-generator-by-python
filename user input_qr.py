# progrma to genrat a qr code using PIL 
from PIL import Image
import qrcode

#Step 1: Taking User Input for custom colour 
fill = input("Enter fill colour of QR:- ") 
back = input("Enter baground colour of QR:- ")

# Step 2: Create QR code
data = "https://www.linkedin.com/in/vishwas-verma-a157a8370" 

qr = qrcode.QRCode(
    version=1,
    box_size=8,
    border=6
)
qr.add_data(data)

# Step 3: Generate image
img = qr.make_image(fill_color=fill, back_color=back)

# Step 4: Save the image by save function of qrcode module 
img.save("D:\CODING\python language\qr code\QR Images\my_linkdin.png")
print("Image saved as my_linkdin.png")

# Step 5: Diaplay using PIL by show() function 
img.show()