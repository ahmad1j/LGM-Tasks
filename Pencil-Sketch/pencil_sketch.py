import cv2

# read the image
img = cv2.imread("20190417_143055.jpg")

# resize the image to 500 x 500
img = cv2.resize(img, (500, 500))

# convert BGR to greyscaale image
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# invert the grey image
grey_inv = 255 - grey

# add guassian blur to it
grey_inv_blur = cv2.GaussianBlur(grey_inv, (51, 51), 0)

# invert the blurred image
inv_blur = 255 - grey_inv_blur

# divide grey by inv_blur
sketch = cv2.divide(grey, inv_blur, scale=256.0)





cv2.imshow('image', img)
cv2.imshow('sketch', sketch)

cv2.waitKey(0)