import cv2

class Camera():
    def __init__(self, cam_index, data_format):
        self.cam_index = cam_index
        self.data_format = data_format
        
    def preview(self):
        capture = cv2.VideoCapture(self.cam_index)

        while(True):
            # Capture frame by frame
            success, frame = capture.read()

            if success == False:
                # TODO: Display an error  message to the user.
                print("Error")
                break
            else:
                return frame

        capture.release()
        
    def capture(self):
        if (self.data_format == "photos"):
            capture_photo()
    
    def capture_photo(self):
        capture = cv2.VideoCapture(self.cam_index)
        success, frame = capture.read()
        if (success == False):
            # return failed message
            print("Error: Failed to read the image.")
        else:
            capture.release()
            #cv2.imwrite('../../data/frame.jpg', frame)
            return frame
            
    #def capture_video(self):
    

# Test
#cam = camera(-1, "photos")
#cam.preview()
#cam.capture_photo()
