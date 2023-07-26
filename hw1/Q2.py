import cv2
from scipy.signal import find_peaks
import numpy as np
import os
import csv
import statistics

every_N_pixel = 4

directory = [f for f in os.listdir("./EKG") if os.path.isdir(os.path.join("./EKG/", f))]
ans = []
all_file_name = []
heartbeatCSV = open('heartbeat.csv', 'w', newline='')
for k in  range(len(directory)):
    dirname = "./EKG/" + directory[k]
    all_files = os.listdir("./EKG/" + directory[k])
    all_files.sort(key = lambda x:int(x[:-4]))
    for l in range(len(all_files)):
        filename = "./EKG/" + directory[k] + "/" + all_files[l]
        # filename = "./EKG/EKG_481-600/598.jpg"

        # all_file_name.append(os.listdir(ts))
        pic = cv2.imread(filename)

        # pic = cv2.imread("./EKG/EKG_001-120/20.jpg")
        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("original", pic)
        ret, th1 = cv2.threshold(pic, 127, 255, cv2.THRESH_BINARY)
        # cv2.imshow("th1", th1)

        # total 120~1350

        y1 = 243
        y2 = 1350
        ans = th1[820:900, y1:y2]
        have_num = 0
        tmp_num = 0
        t = np.zeros(int((y2-y1) / every_N_pixel), dtype='uint8')
        for i in range(0, y2-y1):
            for j in range(900-820):
                if ans[j][i] == 0 and have_num < every_N_pixel - 1:
                    tmp_num += 80 - j
                    have_num += 1
                    break
                elif ans[j][i] == 0 and have_num == every_N_pixel - 1:
                    t[int(i / every_N_pixel)] = int((80 - j + tmp_num) / every_N_pixel)
                    have_num = 0
                    tmp_num = 0
                    # print(t[int(i / every_N_pixel)], end=' ')
                    break

        sort_t = sorted(t)
        # mode = statistics.mode(t)
        average_t = sum(t) / len(t)

        if (sort_t[-5] - average_t) < 5:
            division = 10
        # elif (sort_t[-4] - average_t) < 30:
        #     division = 8
        # elif (sort_t[-4] - average_t) < 35:
        #     division = 8
        # elif (sort_t[-4] - average_t) < 40:
        #     division = 7.5
        else:
            division = 2

        prominence = (sort_t[-5] - average_t)/division  # (max(t) - mode)/4

        peaks, _ = find_peaks(t, width=[1, 3], height=average_t , prominence= (sort_t[-5]-average_t)/division)#, threshold=(sort_t[-4] - average_t) / division) #  threshold=(sort_t[-4] - average_t) / division,

        if len(all_files[l]) == 6:
            pic_name = "EKG_0" + all_files[l][0:2]
        elif len(all_files[l]) == 5:
            pic_name = "EKG_00" + all_files[l][0]
        else:
            pic_name = "EKG_" + all_files[l][0:3]
        #  modify 2 to the corresponding number of picture

        # print("------------------")
        # print("threshold = ", (sort_t[-4] - average_t) / division)
        # print("division = ", division, "max - average = ", sort_t[-5]-average_t, sort_t[-5])
        # print("prominence = ", prominence)
        print(pic_name, len(peaks) / 9 * 60)
        # print("=====================")
        heart_rate = round(len(peaks) / 9 * 60)

        data = [pic_name, heart_rate]
        writer = csv.writer(heartbeatCSV)
        writer.writerow(data)

#         # draw the detected peak
#         radius = 10  # Radius of circle
#         color = (0, 0, 255)  # Red color in BGR
#         thickness = 2  # Line thickness of -1 px
#         image = ans
#         for i in range(len(peaks)):
#             image = cv2.circle(ans, (peaks[i] * every_N_pixel, 30), radius, color, thickness)
#
#         name = "image" + pic_name
#         cv2.imshow(name, image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

