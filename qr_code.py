import qrcode

text = input("input text or link then enter : ")
name = input("name QRcode picture then enter : ")
img = ".png"
img = name + img

save = qrcode.make(text)
save.save(img)

print(f"QR {img} saved")
