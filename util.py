import numpy as np


def Laplacian(img, alpha=1, method='simple'):
    SimpleLaplacian = [
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ]
    DifferentLaplacian = [
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ]
    if method == 'different':
        matrix = DifferentLaplacian
    elif method == 'simple':
        matrix = SimpleLaplacian
    else:
        print('method error')
        return

    h, w = img.shape
    new_img = np.zeros_like(img, dtype=np.float32)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            # 应用拉普拉斯算子
            # 提取3x3邻域
            neighborhood = img[i-1:i+2, j-1:j+2]
            # 应用卷积
            new_img[i, j] += img[i][j] + alpha * np.sum(neighborhood * matrix)

    # 确保新的图像值在可接受的范围内（0-255）
    new_img = np.clip(new_img, 0, 255)
    return new_img.astype(np.uint8)


def Laplacian_Of_Gaussian(img, alpha=1):
    matrix = [
        [0, 0, -1, 0, 0],
        [0, -1, -2, -1, 0],
        [-1, -2, 16, -2, -1],
        [0, -1, -2, -1, 0],
        [0, 0, -1, 0, 0]
    ]

    h, w = img.shape
    new_img = np.zeros_like(img, dtype=np.float32)
    for i in range(2, h - 2):
        for j in range(2, w - 2):
            # 应用算子
            # 提取5x5邻域
            neighborhood = img[i-2:i+3, j-2:j+3]
            # 应用卷积
            new_img[i, j] += img[i][j] + alpha * np.sum(neighborhood * matrix)
    return new_img
