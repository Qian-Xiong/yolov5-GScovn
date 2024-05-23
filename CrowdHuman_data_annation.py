import json
import os
# 假设你有一个名为'annotations.json'的JSON文件
annotations_filename = 'D:\\Rookie\\yolo\\yolov5\\data\\annotation_train.odgt'
# 假设你要将转换后的标注保存到'yolov5_annotations'目录
yolo_annotations_dir = 'D:\Rookie\yolo\yolov5\data\images\yolov5_annotations'

# 创建YOLO格式的标注文件夹
if not os.path.exists(yolo_annotations_dir):
    os.makedirs(yolo_annotations_dir)

# 打开并读取JSON文件
with open(annotations_filename, 'r') as f:
    annotations = json.load(f)

# 遍历JSON文件中的每个图像和标注
for image_name, image_annotations in annotations.items():
    gtboxes = image_annotations['gtboxes']
    image_width = image_annotations['width']  # 假设JSON文件中包含了图像宽度
    image_height = image_annotations['height']  # 假设JSON文件中包含了图像高度

    # 为每个图像创建一个YOLO格式的标注文件
    yolo_filename = os.path.join(yolo_annotations_dir, f"{image_name}.txt")
    with open(yolo_filename, 'w') as yolo_f:
        for obj in gtboxes:
            # 提取边界框坐标和类别标签
            tag = obj['tag']
            hbox = obj['hbox']
            fbox = obj['fbox']
            x, y, w, h = hbox
            x_center = (x + w / 2) / image_width
            y_center = (y + h / 2) / image_height
            width = w / image_width
            height = h / image_height

            # 写入YOLO格式的标注
            yolo_f.write(f"{tag} {x_center} {y_center} {width} {height}\n")
