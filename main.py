import cv2
import numpy as np
img = cv2.imread("original.jpg")
layer = img.copy()
gaussian_pyramid_list = [layer]
cv2.imshow("Imagen original", img)

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_list.append(layer)

layer = gaussian_pyramid_list[5]
laplacian_pyramid_list = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)
    laplacian_pyramid_list.append(laplacian)

cv2.imshow("Despues de la compresion",laplacian_pyramid_list[5])

ls_ = laplacian_pyramid_list[0]
for i in range(1,6,1):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_,laplacian_pyramid_list[i])


cv2.imshow("Reconstruccion",ls_)

cv2.waitKey(0)
cv2.destroyAllWindows()