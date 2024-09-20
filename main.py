import cv2
car = cv2.imread("is200 v12.jpg")

text = cv2.putText(car, "HUT", (100, 111), cv2.FONT_ITALIC, 3, (255, 0, 0), 3)
cv2.imshow("screen1", text)
cv2.waitKey(0)