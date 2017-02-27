import cv2

def imgcap():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Raw_Video", frame)
        ch = cv2.waitKey(33)
        if ch== ord('p'):
            cv2.destroyAllWindows()
            cap.release()
            return frame
        if ch == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()