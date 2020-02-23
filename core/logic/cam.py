import cv2

# TODO: Let the user change the camera index
capture = cv2.VideoCapture(-1)

while(True):
    # Capture frame by frame
    success, frame = capture.read()

    if success == False:
        # TODO: Display a message to the user.
        break
    
    img = cv2.imread('../data/frame.jpg')
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

def preview(camIndex):
    capture = cv2.VideoCapture(camIndex)

    while(True):
        # Capture frame by frame
        success, frame = capture.read()

        if success = False:
            # TODO: Display a message to the user.
            break

        return

def capture(frame, i):
    cv2.imwrite('../../data/frame.jpg', frame)
    return 0
