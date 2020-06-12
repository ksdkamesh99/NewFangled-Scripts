import qrcode
print("Press 1 for text")
print("Press 2 for storing link\n")
option=int(input("Enter the response\n"))
if option==1:
    qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)
    with open('test.txt','r+') as f:
        text=f.read()
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color='black',back_color='white')
    img.save('qrcode-text.png')
if option==2:
    qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)
    link=input("Enter the link you want to convert to QRCode\n")
    qr.add_data(link)
    qr.make(fit=True)
    img=qr.make_image(fill_color='black',back_color='white')
    img.save('qrcode-link.png')