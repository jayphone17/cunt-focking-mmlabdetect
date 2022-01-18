from turtle import color
from mmdet.apis import init_detector, inference_detector
import mmcv
import cv2

threshold = 0.8
config_file = 'configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

model = init_detector(config_file, checkpoint_file,device = 'cuda:0')

img = 'demo/1.jpg'
result = inference_detector(model, img)

img = cv2.imread('demo/1.jpg')
scores = result[0][:,-1]

ind = scores > threshold
bboxes = result[0][ind,:-1]
for bbox in bboxes :
      left_top = (bbox[0], bbox[1])
      right_bottom = (bbox[2], bbox[3])
      cv2.rectangle(img, left_top, right_bottom, color = (0, 255, 0))
cv2.imwrite('demo/1_result.jpg',img)