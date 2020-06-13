from captcha.image import ImageCaptcha
import random as rd

def random_captcha():
    charc="abcdefghijktuvwxyzAIJKLlmnopqrsMNOPQRSTUVBCDEFGHWXYZ1234567890"
    LEN=6
    data=''
    for i in range(6):
        i=rd.randint(0,len(charc)-1)
        data=data+charc[i]
    imc=ImageCaptcha(width=200,height=100)
    imc.write(data,'out.png')
    print("Random Image Captcha generated")
random_captcha()
