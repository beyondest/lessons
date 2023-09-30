import cv2
import numpy as np

img = cv2.imread('D:/tmdvs/pywork/RM/out/fuck.png')  # 输入图像
p_list = []  # 左上，右上，左下，右下顺序点击
dst_point = (1000, 1000)  # 变换目标大小
img2 = img.copy()

def capture_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # create a circle at that position
        # of radius 30 and color greeen
        cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
        cv2.imshow("original_img", img)
        p_list.append([x, y])
        if len(p_list) == 4:
            pts1 = np.float32(p_list)
            pts2 = np.float32(
                [[0, 0], [dst_point[0], 0], [0, dst_point[1]], [dst_point[0], dst_point[1]]])
            dst = cv2.warpPerspective(img2, cv2.getPerspectiveTransform(pts1, pts2), dst_point)
            cv2.namedWindow("result_img", cv2.WINDOW_NORMAL)
            cv2.imshow("result_img", dst)
            cv2.imwrite('2.jpg', dst)  # 输出图像


cv2.namedWindow("original_img", cv2.WINDOW_NORMAL)
cv2.imshow("original_img", img)
cv2.setMouseCallback("original_img", capture_event)
cv2.waitKey(0)
