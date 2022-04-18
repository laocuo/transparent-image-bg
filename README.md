# transparent-image-bg
select a folder and convert all images background transparent

## usage:
python img_bg_tool.py PATH MODE(1-2) THRESHOLD(1-255)
python img_bg_tool.py XXXX
python img_bg_tool.py XXXX 2
python img_bg_tool.py XXXX 2 220

## mode
模式1:全部白色像素点转换成透明色
模式2:外围白色像素点转换成透明色

## threshold
像素点的RGB值都大于阈值则转成透明点