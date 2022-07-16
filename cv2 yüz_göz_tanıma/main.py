import cv2

video=cv2.VideoCapture(0)
surat_yuz=cv2.CascadeClassifier("haarcascade_eye.xml")
ka=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
        ret,res=video.read()
        siyah=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
        kafa = ka.detectMultiScale(siyah, 1.1, 3)
        yuzler=surat_yuz.detectMultiScale(siyah,1.1,5,minSize=(50,50))
        for (x,y,w,h) in yuzler:
            cv2.rectangle(res,(x,y),(x+w,y+h),(255,0,0),4)
        for (x,y,w,h) in kafa:
            cv2.rectangle(res,(x,y),(x+w,y+h),(255,0,0),4)

        cv2.imshow("r",res)
        if cv2.waitKey(1)==ord('q'):
            break
cv2.destroyAllWindows()