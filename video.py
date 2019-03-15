import cv2
import os

print(cv2.__version__)

folder_path = "img/"
fileName = "sample.mp4"
# os.makedirs(folder_path)

vc = cv2.VideoCapture(fileName)
c = 0

ret = vc.isOpened()

while ret:
    c += 1
    ret, frame = vc.read()
    if ret:
        cv2.imwrite(folder_path+str(c)+".jpg", frame)
        print(folder_path+str(c)+".jpg")
        cv2.waitKey(1)
    else:
        break

vc.release()
