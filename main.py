import cv2

video = cv2.VideoCapture(0)#input device
faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")#face setection dataset
smileCascade = cv2.CascadeClassifier("dataset/haarcascade_smile.xml")#smile detection dataset

while True:
    success,img = video.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#converting given image to greyscale
    faces = faceCascade.detectMultiScale(grayImg,1.1,4)
    cnt=500
    keyPressed = cv2.waitKey(1)
    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)
        smiles = smileCascade.detectMultiScale(grayImg,1.8,15)
        for x,y,w,h in smiles:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),5)
            print("Image "+str(cnt)+"Saved")
            path=r'images\img'+str(cnt)+'.jpg'
            cv2.imwrite(path,img)
            cnt +=1
            if(cnt>=503):   
                break
                
    cv2.imshow('live video',img)
    if(keyPressed & 0xFF==ord('q')):
        break

video.release()                                  
cv2.destroyAllWindows() 
