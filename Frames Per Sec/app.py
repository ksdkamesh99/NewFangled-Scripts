import cv2
import datetime

print("Want to frames per sec!")
camera=cv2.VideoCapture(0)
f=0
start_time=datetime.datetime.now()
while True:
    ret,frame=camera.read()
    f=f+1
    time_curr=datetime.datetime.now()
    diff=time_curr-start_time
    diff_sec=diff.seconds
    if diff_sec==0:
        fps=0
    else:
        fps=f/diff_sec
    cv2.putText(frame,"The fps is "+str(fps),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
    cv2.imshow("fps",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()

