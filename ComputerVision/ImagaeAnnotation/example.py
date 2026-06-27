import cv2
import matplotlib.pyplot as plt
# 1. Load the image
image = cv2.imread('ComputerVision\\IntroOpenCV\images.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()


start_point = (100, 150)
end_point = (404, 421)


thickness = 4
image_annotated = cv2.rectangle(image_rgb, start_point, end_point,(0,255,0), thickness)

cv2.arrowedLine(image_annotated,(0,0),(500,500),(0,0,255),thickness)

cv2.line(image_annotated,(500,500),(500,0),(0,0,255),thickness)


label = "Object"
text_org = (100, 140) # Bottom-left corner of the text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color_white = (255, 255, 255)

cv2.putText(image_annotated, label, text_org, font, font_scale, color_white, 2, cv2.LINE_AA)

plt.imshow(image_annotated)
plt.title("Image")
plt.show()

