import cv2 as cv

# reading pics

img = cv.imread('Resources\Photos\cat.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

# reading videos

# capture = cv.VideoCapture('Resources\Videos\dog.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()


