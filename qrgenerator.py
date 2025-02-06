import qrcode
img = qrcode.make("localhost:8000")
img.save("business_card_qr.png")