import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Funcion
def detectfaces(gray,frame):
    faces = face_cascade.detectMultiScale(gray,1.2,3)
    for (x,y,w,h) in faces:
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(120,0,0))
    return frame

video_capture = cv2.VideoCapture('output.mp4')

while True:
        _, frame = video_capture.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        canvas = detectfaces(gray,frame)
        cv2.imshow('Video', canvas)
        #break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #restart video if ends
        lastframe = video_capture.get(cv2.CAP_PROP_FRAME_COUNT) -1
        thisframe = video_capture.get(cv2.CAP_PROP_POS_FRAMES) -1
        if lastframe == thisframe:
            video_capture.set(cv2.CAP_PROP_POS_FRAMES,0)
video_capture.release()
cv2.destroyAllWindows()