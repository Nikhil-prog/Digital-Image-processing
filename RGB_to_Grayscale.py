import cv2
import numpy as np

# Grayscale image =  (0.3 * R) + (0.59 * G) + (0.11 * B)
def rgb_to_grayscale(img):
    n, m, k = img.shape
    final_img = np.ones((n, m))
    for i in range(n):
        for j in range(m):
            r = img[i][j][0]
            g = img[i][j][1]
            b = img[i][j][2]
            final_img[i][j] = 0.3*r + 0.59*g + 0.11*b

    # converting float matrix to int8 before returning
    return final_img.astype(np.uint8)


# Run the Algorithm
color_img = cv2.imread("Images/Nature_color_Image.jpeg")
gray_scale_img = rgb_to_grayscale(color_img)

# plotting
cv2.imshow("Input Colour Image", color_img)
cv2.imshow("Gray Scale Image", gray_scale_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
