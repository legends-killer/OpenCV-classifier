import os
path = './negative_images'
dir = os.listdir(path) # 自动排序
fopen = open('./negatives.txt', 'w')
for d in dir:
    string = './negative_images/' + d +'\n'
    fopen.write(string)
fopen.close()