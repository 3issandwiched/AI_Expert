import cv2


image=cv2.imread("ComputerVision\\IntroOpenCV\images.jpg")

cv2.namedWindow('loaded image',cv2.WINDOW_NORMAL)

cv2.resizeWindow('loaded image',600,400)

cv2.imshow('loaded image',image)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(image.shape)