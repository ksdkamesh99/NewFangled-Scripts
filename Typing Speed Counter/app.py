import datetime
import random

def typespeed(words,diff):
    sec=diff.seconds
    if sec==0:
        return 0
    wps=words/sec
    return wps*60

def random_scripts():
    scripts=["Paid was hill sir high. For him precaution any advantages dissimilar comparison few terminated projecting. Prevailed discovery immediate objection of ye at. Repair summer one winter living feebly pretty his. In so sense am known these since. Shortly respect ask cousins brought add tedious nay. Expect relied do we genius is. On as around spirit of hearts genius. Is raptures daughter branched laughter peculiar in settling.",
    "An an valley indeed so no wonder future nature vanity. Debating all she mistaken indulged believed provided declared. He many kept on draw lain song as same. Whether at dearest certain spirits is entered in to. Rich fine bred real use too many good. She compliment unaffected expression favourable any. Unknown chiefly showing to conduct no. Hung as love evil able to post at as.",
"Not far stuff she think the jokes. Going as by do known noise he wrote round leave. Warmly put branch people narrow see. Winding its waiting yet parlors married own feeling. Marry fruit do spite jokes an times. Whether at it unknown warrant herself winding if. Him same none name sake had post love. An busy feel form hand am up help. Parties it brother amongst an fortune of. Twenty behind wicket why age now itself ten.",
"Over fact all son tell this any his. No insisted confined of weddings to returned to debating rendered. Keeps order fully so do party means young. Table nay him jokes quick. In felicity up to graceful mistaken horrible consider. Abode never think to at. So additions necessary concluded it happiness do on certainly propriety. On in green taken do offer witty of." ]
    r=random.randint(0,3)
    return scripts[r]


print("Welcome To Typing Speed Test")

while(True):
    print("If you want to start the test press Y and not interested press N ")
    res=input()
    if(res=='Y' or res=='y'):
        print("Please enter the following text below and press enter")
        script=random_scripts().lower()
        print(script)
        print("Your Time Starts Now! Clock is running ")
        start=datetime.datetime.now()
        text=input().lower()
        end=datetime.datetime.now()

        script_words=script.split(' ')
        
        text_word=text.split(' ')
        if(text_word[0]==' '):
            print(typespeed(0,end-start))
        else:
            if(text==script):
                print(typespeed(len(text_word),end-start))
            else:
                print("Please enter correct text and try again")

    elif(res=='N' or res=='n'):
        break 
    else:
        print("Enter Correct Key")
    



