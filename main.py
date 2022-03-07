import cv2
import winsound

# initialize the cam
cap = cv2.VideoCapture(0)
previous = "VU"
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if bbox is not None:
        if data != previous:
            print(data)
            winsound.Beep(440, 500)
            previous = data
    # display the result
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()