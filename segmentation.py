# count = 0  # 元素个数
# margin = 5  # 裁剪边距
# draw_rect = image.copy()
# for i, contour in enumerate(cnts):
#     area = cv2.contourArea(contour)  # 计算包围形状的面积
#     if area < 15:  # 过滤面积小于15的形状
#         continue
#     count += 1
#     rect = cv2.minAreaRect(contour)  # 检测轮廓最小外接矩形，得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
#     box = np.int0(cv2.boxPoints(rect))  # 获取最小外接矩形的4个顶点坐标
#     cv2.drawContours(draw_rect, [box], 0, (255, 0, 0), 2)  # 绘制轮廓最小外接矩形
#
#     h, w = image.shape[:2]  # 原图像的高和宽
#     rect_w, rect_h = int(rect[1][0]) + 1, int(rect[1][1]) + 1  # 最小外接矩形的宽和高
#     if rect_w <= rect_h:
#         x, y = int(box[1][0]), int(box[1][1])  # 旋转中心
#         M2 = cv2.getRotationMatrix2D((x, y), rect[2], 1)
#         rotated_image = cv2.warpAffine(image, M2, (w * 2, h * 2))
#         y1, y2 = y - margin if y - margin > 0 else 0, y + rect_h + margin + 1
#         x1, x2 = x - margin if x - margin > 0 else 0, x + rect_w + margin + 1
#         rotated_canvas = rotated_image[y1: y2, x1: x2]
#     else:
#         x, y = int(box[2][0]), int(box[2][1])  # 旋转中心
#         M2 = cv2.getRotationMatrix2D((x, y), rect[2] + 90, 1)
#         rotated_image = cv2.warpAffine(image, M2, (w * 2, h * 2))
#         y1, y2 = y - margin if y - margin > 0 else 0, y + rect_w + margin + 1
#         x1, x2 = x - margin if x - margin > 0 else 0, x + rect_h + margin + 1
#         rotated_canvas = rotated_image[y1: y2, x1: x2]
#     print("dot_th #{}".format(count))
#     # cv2.imshow("rotated_canvas", rotated_canvas)
#     cv2.imwrite("/home/rui/vistr/image_process/rotation-results/{}.jpg".format(count), rotated_canvas)
#     cv2.waitKey(0)
# cv2.imwrite("/home/rui/vistr/image_process/results/rect.jpg", draw_rect)