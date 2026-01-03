import qrcode
data =input("enter the url or text for QR:")
qr=qrcode.make(data)
qr.save("myqr.png")
print("QR code genrated successfully")