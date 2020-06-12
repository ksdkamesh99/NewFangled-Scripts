from textblob import TextBlob
with open('test.txt','r+') as f:
    text=f.read()
b=TextBlob(text)
corrected=str(b.correct())
with open("correct.txt",'w+') as f:
    f.write(corrected)