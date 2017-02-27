import cv2

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    cv2.imshow('Press P to save image',frame)
    ch=cv2.waitKey(33)
    if ch==ord('p'):
        cv2.imwrite("Sample1.jpg", frame)
        break
cap.release()
cv2.destroyAllWindows()