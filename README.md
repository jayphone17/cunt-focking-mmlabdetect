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

<img src="./figs/result1.jpg" alt="result1" style="zoom:67%;" />

### How to train my own data in MMDetection ??

简单来说就是准备好自己的数据。

转换为COCO或者PASCAL VOC数据集格式。

（1）在线转换：从CustomDataset继承一个新的数据集类，参考CocoDataset和VOCDataset重写load_annotations(self, ann_file)以及get_ann_infi(self,idx)两个方法。

（2）离线转换：直接将标注格式转换成需要的格式，存储为pickle或者JSON文件，然后使用CustomDataset处理数据。

以5个类别为例子：

在mmdet/datasets/my_dataset.py中添加代码：

```python
from .coco import CocoDataset
from .registry import DATASETS

@DATASETS.register_module
class MyDataset(CocoDataset):
    CLASSES = ('1','2','3','4','5')
```

在mmdet/datasets/__init__.py中添加代码：

```python
from .my_dataset import MyDataset
```

