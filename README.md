# cunt-focking-mmlabdetect
### Install

```
conda create -n openmmlab python=3.7 -y
conda activate openmmlab
```

```
conda install pytorch=1.3.1 cudatoolkit=9.2 torchvision=0.4.2 -c pytorch
```

```
pip install openmim
mim install mmdet
```

### Test

```python
python demo/test.py demo/demo.jpg configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
```

### Result

![result](./figs/result.jpg)

