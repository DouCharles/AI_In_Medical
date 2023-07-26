import cv2
import numpy as np
import random

ans = np.zeros((150 * 3 + 20 * 3, 320+305+305+310 + 20 * 4, 3), dtype='uint8')
print(ans.shape)
img = cv2.imread("./EKG/EKG_001-120/1.jpg")
# cv2.imshow('pic', img)
width = 320
height = 150

for j in range(10):
    ran = random.randint(1,120)
    original_pic = "./EKG/EKG_001-120/" + str(ran) + ".jpg"
    img = cv2.imread(original_pic)
    for i in range(3):
        # for j in range(4):
        temp_height = 360 + height * i
            # temp_width = 110 + width * j
            # temp = img[temp_height:temp_height + 140, temp_width:temp_width + 320]
        temp = img[temp_height:temp_height + 150, 110: 110+320]
        ans[height * i + 20 * i: height * i + 150 + 20 * i, 0: 320] = temp.astype(np.uint8)

        temp = img[temp_height:temp_height + 150, 425: 425 + 305]
        ans[height * i + 20 * i: height * i + 150 + 20 * i, 340: 645] = temp

        temp = img[temp_height:temp_height + 150, 730: 730 + 305]
        ans[height * i + 20 * i: height * i + 150 + 20 * i, 665: 970] = temp

        temp = img[temp_height:temp_height + 150, 1035: 1035 + 310]
        ans[height * i + 20 * i: height * i + 150 + 20 * i, 990: 1300] = temp
        # cv2.imshow('ans',ans)
    num = ""
    if ran < 10:
        num += "00"
    elif ran < 100:
        num += "0"
    num += str(ran)
    cv2.imwrite("./answer/EKG_" + num + ".jpg", ans)
# cv2.waitKey(0)
# cv2.destroyAllWindows()