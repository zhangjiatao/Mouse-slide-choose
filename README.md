# Mouse-slide-choose
可以通过鼠标滑动来选取token，提升标注效率

## 安装
* mac: pip install PyUserInput
* win: 没有在win上做测试

## 调整
* 用python将脚本跑起来
* 移动点击鼠标鼠标打印的坐标
* 用坐标测量标注页面的一个小个子宽度，修正参数

## 使用
* 用python将脚本跑起来
* 从标注的起点按下鼠标左键，滑动鼠标到结束位置松开鼠标，即可选中中间的token
* (会有部分漏选，还需要手动点击补齐)
