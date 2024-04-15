import cv2
import albumentations as A
import argparse
from draw_box import draw_boxes
# construct the argument parser
parser = argparse.ArgumentParser()
parser.add_argument(
    '-f', '--format', help='bbox transform type', 
    default='yolo', choices=['coco', 'voc', 'yolo']
)
parser.add_argument(
    '-ma', '--min-area', dest='min_area', 
    help='provide value > 0 if wanting to ignore bbox after \
        augmentation under a certain threshold', 
    default=0, type=int
)
args = vars(parser.parse_args())

# read image and convert to RGB format
image = cv2.imread('images/dog.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# bbox in COCO format
bboxes_coco = [
    # xmin, ymin, width, height
    [193, 108, 208, 272]
]
# bbox in Pascal VOC format
bboxes_voc = [
    # xmin, ymin, xmax, ymax
    [193, 108, 401, 380]
]
# bbox in YOLO format
bboxes_yolo = [
    # normalized[x_center, y_center, width, height]
    [0.464105, 0.573096, 0.324689, 0.640049]
]
# class labels list containing all the class names
class_labels = ['dog']

# apply the transforms according to the bbox data format
if args['format'] == 'yolo':
    transform = A.Compose([
        A.RandomCrop(width=250, height=250, p=1), 
    ], bbox_params=A.BboxParams(
        format='yolo', label_fields=['class_labels'],
        min_area=args['min_area']
    ))
    transformed_instance = transform(
        image=image, bboxes=bboxes_yolo, class_labels=class_labels
    )
    transformed_image = transformed_instance['image']
    transformed_bboxes = transformed_instance['bboxes']
# draw the bounding boxes on the tranformed/augmented image
annot_image, box_areas = draw_boxes(
    transformed_image, transformed_bboxes, args['format']
)
print(f"Area bboxes: {box_areas}")
#cv2.imshow('Image', annot_image)
import matplotlib.pyplot as plt
plt.imshow(cv2.cvtColor(annot_image, cv2.COLOR_BGR2RGB))
plt.show()
cv2.waitKey(0)