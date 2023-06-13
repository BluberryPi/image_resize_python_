import glob
from PIL import Image
import os

###
# 파일을 저장할 파일 안에 넣고 실행!!!
###

name = input('name: ') #파일 이름 입력
input_path = "파일위치/*.jpg" #변환할 이미지 파일 위치
file_list = [file for file in glob.glob(input_path)]
num = 1


img_resize_list = []
for f in file_list:
    img = Image.open(f)
    img_resize = img.resize((48, 48))
    img_resize_list.append(img_resize.size)
    #title, ext = os.path.splitext(f)
    #img_resize = img_resize.convert('RGB')
    img_resize.save(f'{name}_{num}_resize.jpg', 'png')
    num += 1

print(img_resize_list)
