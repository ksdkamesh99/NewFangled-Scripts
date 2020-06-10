import os
print("If you want to shutdown your computer press 1\n")
print("If you want to restart your computer press 2\n")
print("If you want to log out your computer press 3\n")
s=int(input("Enter your Response\n"))
if s==1:
    os.system('shutdown /s /t 1')
elif s==2:
    os.system('shutdown /r /t 1')
elif s==3:
    os.system('shutdown /l')
else:
    print("You have entered the wrong response! Please run the script again")