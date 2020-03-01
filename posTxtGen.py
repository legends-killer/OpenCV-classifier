import os
path = './positive_images'
dir = os.listdir(path) # 自动排序
fopen = open('./positives.txt', 'w')
for d in dir:
    string = './positive_images/' + d + ' 1 0 0 32 32' +'\n'
    fopen.write(string)
fopen.close()