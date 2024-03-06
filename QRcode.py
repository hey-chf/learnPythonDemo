import pyqrcode

text = input('请输入要生成的QR码的文本：')

qr_code = pyqrcode.create(text)
qr_code.svg('qr_code.svg', scale=8)
