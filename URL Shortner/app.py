import pyshorteners as pys
shortner=pys.Shortener()
link=input("Enter the link you want to shorten")
print("Enter the following options for shorteners\n")
print("1. TinyUrl")
print("2. Clck.ru")
print("3. Da.gd")
print("4. Is.gd")
print("5. Os.db")
print("6. Ow.ly")
print("7. Create Your Own URL")
option=int(input())
if option==1:
    shortlink=shortner.tinyurl.short(link)
    print(shortlink)
if option==2:
    shortlink=shortner.clckru.short(link)
    print(shortlink)
if option==3:
    shortlink=shortner.dagd.short(link)
    print(shortlink)
if option==4:
    shortlink=shortner.isgd.short(link)
    print(shortlink)
if option==5:
    shortlink=shortner.osdb.short(link)
    print(shortlink)
if option==6:
    shortlink=shortner.owly.short(link)
    print(shortlink)
if option==7:
    domain=input("Enter the domain you want to create with it")
    shortner=pys.Shortener(domain=domain)
    shortlink=shortner.nullpointer.short(link)
    print(shortlink)





