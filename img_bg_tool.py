'''
一键转换文件夹下全部PNG图片的背景为透明
authero:zhaocheng
'''

import os
import sys
from PIL import Image

# 模式1:全部白色像素转换成透明 模式2:外围白色像素转换成透明
MODE = 2

# 像素阈值(1 - 255)
THRESHOLD = 220

def convertor_file_1(file):
    print('convertor_file:' + file)
    img = Image.open(file)
    img = img.convert('RGBA')
    width, height = img.size 
    pixel_data = img.load()
    for h in range(height):
        for w in range(width):
            pixel = pixel_data[w, h]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            a = pixel[3]
            if is_white_point(r, g ,b ,a):
                pixel_data[w, h] = (255, 255, 255, 0)
    img.save(os.path.join(os.path.dirname(file), 'alpha_' + os.path.basename(file)))

def convertor_file_2(file):
    print('convertor_file:' + file)
    img = Image.open(file)
    img = img.convert('RGBA')
    width, height = img.size 
    pixel_data = img.load()
    for h in range(height):
        for i in range(0, width):
            index = i
            pixel = pixel_data[index, h]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            a = pixel[3]
            if is_white_point(r, g ,b ,a):
                pixel_data[index, h] = (255, 255, 255, 0)
            else:
                break
        for j in range(0, width):
            index = width - 1 - j
            pixel = pixel_data[index, h]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            a = pixel[3]
            if is_white_point(r, g ,b ,a):
                pixel_data[index, h] = (255, 255, 255, 0)
            else:
                break
    for w in range(width):
            for i in range(0, height):
                index = i
                pixel = pixel_data[w, index]
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                a = pixel[3]
                if is_white_point(r, g ,b ,a):
                    pixel_data[w, index] = (255, 255, 255, 0)
                else:
                    break
            for j in range(0, height):
                index = height - 1 - j
                pixel = pixel_data[w, index]
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                a = pixel[3]
                if is_white_point(r, g ,b ,a):
                    pixel_data[w, index] = (255, 255, 255, 0)
                else:
                    break
    img.save(os.path.join(os.path.dirname(file), 'alpha_' + os.path.basename(file)))

def is_white_point(r, g, b, a):
    if r > THRESHOLD and g > THRESHOLD and b > THRESHOLD:
        return True
    else:
        return False

def convertor_dir(dir):
    if os.path.isdir(dir):
        print('convertor_dir:' + dir)
        files = os.listdir(dir)
        for i in range(0, len(files)):
            file = os.path.join(dir, files[i])
            if os.path.isfile(file):
                if file[-3:] == 'png':
                    if os.path.basename(file).startswith('alpha_'):
                        os.remove(file)
        files = os.listdir(dir)
        for i in range(0, len(files)):
            file = os.path.join(dir, files[i])
            if os.path.isfile(file):
                if file[-3:] == 'png':
                    if MODE == 1:
                        convertor_file_1(file)
                    elif MODE == 2:
                        convertor_file_2(file)
            elif os.path.isdir(file):
                convertor_dir(file)
    else:
        print('wrong:input is not a dir')

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('wrong:params number')
    else:
        if len(sys.argv) > 2:
            MODE = int(sys.argv[2])
        if len(sys.argv) > 3:
            THRESHOLD = int(sys.argv[3])
        convertor_dir(sys.argv[1])