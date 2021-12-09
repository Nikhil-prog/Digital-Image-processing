import cv2
import numpy as np


# img = image and c = interpolation factor or zoom factor of image
def nn_interpolation(img, c):
    # (n, m):size of orignal image  &  (p,q):size of final image
    n, m = img.shape
    p, q = int(n*c), int(m*c)

    final_img = np.ones((p, q))
    for i in range(p):
        for j in range(q):
            x = int(i/c)
            y = int(j/c)
            final_img[i][j] = (int)(img[x][y])

    # converting float matrix to int8 before returning
    return final_img.astype(np.uint8)


# Run the Algorithm
img = cv2.imread("Images/CameraMan.jpg", flags=cv2.IMREAD_GRAYSCALE)
zoom_in_img = nn_interpolation(img, c=2.5)
zoom_out_img = nn_interpolation(img, c=0.5)

# plotting
cv2.imshow("Input Image", img)
cv2.imshow("Zoom in Image", zoom_in_img)
cv2.imshow("Zoom out Image", zoom_out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
