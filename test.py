import copy
import time

import cv2
import numpy as np

import rune
import units
from units import *

# import subprocess
# def test(event) :
#     print(event.Key)
#     if (event.Key == 'T') :
#         mouseMove("2130", "230")
#     if (event.Key == 'Y') :
#         exit()
#     return True
#
# hm = pyHook.HookManager()
# hm.KeyDown = test
# hm.HookKeyboard()
# pythoncom.PumpMessages()
#img = img[300:350,1200:1400]

# img = cv2.imread("testwindow.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret1, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# cv_show(thresh, "22")
# tpl = cv2.imread("icon.jpg")
# res1 = match(tpl, thresh, 0.01)
# print(res1)
# if (res1[0]):
#     x = res1[1][0] - 3
#     y = res1[1][1] + 22
#     img = img[y:y+1080, x:x+1920]
#     cv_show(img, "22")
def checkPointInMap(img, point, lower, upper):
    img = img[0:150, 0:300]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    inRange_hsv = cv2.inRange(hsv, lower, upper)
    thresh = cv2.bitwise_not(inRange_hsv)
    units.cv_show(thresh)
    res = units.match(point, thresh, 0.02)
    return res


point = cv2.imread("me.jpg")
meRes = checkPointInMap(point, np.array([10, 160, 230]), np.array([110, 255, 255]))
img = cv2.imread("ilium/100.jpg")
img = img[1000:, 1350:]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret1, thresh1 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
cv_show(thresh1)
# runePoint = cv2.imread("has_rune.jpg")
# res = checkPointInMap(img, runePoint, np.array([0, 180, 40]), np.array([255, 255, 255]))
# print(res)
# tpl2 = cv2.imread("pathfinder/buff_bottom1.jpg")
# tpl1 = cv2.imread("pathfinder/buff_top1.jpg")
# img = cv2.imread("dawnKnight/snipaste_20220102_212532.jpg")
# img = img[1050:, 920:]
# print(img[0,0] == [102, 97, 99])
# cv_show(img, "22")
# b, g, r = cv2.split(img)
# img = g
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret1, thresh1 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
# res1 = match(tpl2, thresh1, 0.01)
# ret2, thresh2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
# res2 = match(tpl1, thresh2, 0.01)
# print(res1, res2)
# cv_show(thresh1, "22")
# cv_show(tpl2, "22")
# cv_show(thresh2, "22")
# cv_show(tpl1, "22")

# ret1, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

# img = cv2.imread("testatt1.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = img[450:700, 380:450]
# ret1, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
# cv_show(thresh, "22")
# tpl = cv2.imread("luminous/dark.jpg")
# res = units.match(tpl, thresh, 0.005)
# print(res)
# cap = cv2.imread("test2.jpg")
# img = cap[120:300, 600:1360]
# units.cv_show(img, "22")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# out, contours, hi = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for cnt in range(len(contours)):
#     epsilon = 0.035 * cv2.arcLength(contours[cnt], True)
#     approx = cv2.approxPolyDP(contours[cnt], epsilon, True)
#     area = int(cv2.contourArea(contours[cnt]))
#     if (int(area) > 100 and int(area) < 2000):
#         # print(len(approx))
#         for rox in approx:
#             # print(rox[0])
#             cv2.circle(img, (rox[0][0], rox[0][1]), 2, (0, 0, 255), 4)
# units.cv_show(img, "22")
# 102, 115, 45 98, 99, 68 129, 131, 94
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# inrange = cv2.inRange(hsv, np.array([30, 90, 80]), np.array([110, 140, 100]))
# cv_show(inrange, "22")

# box = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# units.cv_show(img, "22")
# ret, thresh = cv2.threshold(box, 80, 255, cv2.THRESH_BINARY)
# units.cv_show(thresh, "22")
# out, contours, hi = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# b, g, r = cv2.split(img)
# # gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
# # cv_show(gray, "22")
# ret1, thresh1 = cv2.threshold(r, 185, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(g, 200, 255, cv2.THRESH_BINARY)
# thresh = cv2.add(thresh1, thresh2)
# thresh = cv2.bitwise_not(thresh)
# cv_show(thresh, "22")

# img = cv2.imread("rune_log/1641044808copy.jpg")
# img = img[155:300, 600:1360]
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# b, g, r = cv2.split(img)
# gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
# cv_show(gray, "22")
# ret1, thresh1 = cv2.threshold(r, 185, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(g, 200, 255, cv2.THRESH_BINARY)
# thresh = cv2.add(thresh1, thresh2)
#
# # 膨胀两次填补缺口
# thresh = cv2.dilate(thresh, np.ones((2, 2), np.uint8))
# thresh = cv2.dilate(thresh, np.ones((2, 2), np.uint8))
#
# thresh = cv2.bitwise_not(thresh)
# tpl = cv2.imread("rune/left.jpg")
# res = match(tpl, thresh, 0.01)
# print(res)
# cv_show(thresh, "22")
# cv2.circle(img, res[1], 2, (0, 0, 255), 4)
# cv_show(img, "22")
# cv_show(img, "33")
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 140, 155, 112
# b, g, r = cv2.split(img)
# cv_show(b, "22")
# cv_show(g, "22")
# cv_show(r, "22")
# inrange = cv2.inRange(r, 1, 254)
# cv_show(inrange, "22")

# img = img[175:300, 600:1360]
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret1, thresh1 = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY_INV)
# cv_show(thresh1, "22")
# tpl = cv2.imread("rune/box_left.jpg")
# res = match(tpl, thresh1, 0.01)
# x = res[1][0]
# y = res[1][1]
# img = img[y:y+82, x:x+400]
# cv_show(img, "33")
# for i in range(250):
#     ret1, thresh1 = cv2.threshold(gray, i, 255, cv2.THRESH_BINARY)
#     cv_show(thresh1, str(i))
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# inrange = cv2.inRange(hsv, np.array([0, 200, 0]), np.array([110, 255, 160]))
# cv_show(inrange, "22")
# r = rune.RuneUse(img)
# res = r.use(1)
# print(res)