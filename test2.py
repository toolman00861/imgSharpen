import numpy as np
import cv2


def apply_laplacian(img, method='simple'):
    # 定义拉普拉斯算子
    if method == 'simple':
        kernel = np.array([[0, -1, 0],
                           [-1, 4, -1],
                           [0, -1, 0]])
    elif method == 'different':
        kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])
    else:
        raise ValueError("Unknown method: choose 'simple' or 'different'.")

    h, w = img.shape
    new_img = np.zeros_like(img, dtype=np.float32)

    # 手动卷积
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # 提取3x3邻域
            neighborhood = img[i - 1:i + 2, j - 1:j + 2]
            # 应用卷积
            new_value = np.sum(neighborhood * kernel)
            # 更新新图像
            new_img[i, j] = img[i, j] + new_value  # 图像锐化

    # 确保新的图像值在可接受的范围内（0-255）
    new_img = np.clip(new_img, 0, 255)
    return np.uint8(new_img)


# 读取图像
img = cv2.imread('1.tif', cv2.IMREAD_GRAYSCALE)

# 应用拉普拉斯算子
laplacian_img = apply_laplacian(img, method='simple')

# 显示原始图像和拉普拉斯变换后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Laplacian Image', laplacian_img)
cv2.waitKey(0)