import cv2
from util import *

if __name__ == '__main__':
    img_list = [
        '1.tif',
        '2.tif'
    ]
    for img_name in img_list:
        img = cv2.imread(img_name, cv2.COLOR_BGR2GRAY)
        res = []
        temp = img.copy()
        res.append(Laplacian(temp, alpha=1, method='simple'))
        res.append(Laplacian(temp, alpha=1, method='different'))
        res.append(Laplacian_Of_Gaussian(temp, alpha=1))

        cv2.imwrite('out/' + img_name + '_simple_laplacian' + '.jpg', res[0])
        cv2.imwrite('out/' + img_name + '_different_laplacian' + '.jpg', res[1])
        cv2.imwrite('out/' + img_name + '_Laplacian_Of_Gaussian' + '.jpg', res[2])
