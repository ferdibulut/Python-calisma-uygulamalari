import cv2
import time

video = cv2.VideoCapture(0)

while True:
    ret, img1 = video.read()
    ret, img2 = video.read()
    fark = cv2.absdiff(img1, img2)
    dit = cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    cont , _ =cv2.findContours(dit,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img2,cont,-1,(255,55,255),2)
    for ct in cont:
        (x,y,w,h)=cv2.boundingRect(ct)
        if cv2.contourArea(ct)<1000:
            continue
        print(cv2.contourArea(ct))
        cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),4)
        image = cv2.putText(img1, 'HAREKET ALGILANDI', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("res", img1)
    cv2.imshow("fark", dit)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()