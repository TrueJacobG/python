import qrcode

img = qrcode.make("https://twitter.com/TrueJacobG")
img.save("myQrCode.png")
