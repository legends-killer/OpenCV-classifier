## OpenCV自己训练分类器识别图像
- 反正没啥人看就随便写了
## 食用方法
1. 将正向样本放在positive_images文件夹中，负样本同理
2. 执行posTxtGen，输出得到正样例的路径文件，负样本同理
3. 终端执行```./opencv_creatsamples.exe -info positives.txt -vec pos.vec -num 你的正样本数量 -w 你的正样本宽度 -h 你的正样本高度```得到pos.vec即正样本的向量
4. 终端执行```./opencv_traincascade.exe -data 输出训练结果的文件夹 -vec pos.vec -bg 你的负样本路径文件，如negatives.txt -numPos 正样本数量 -numNeg 负样本数量（可大于你的样本数） -numStages 训练层数 -w 同上 -h 同上 - maxFlaseAlarmRate 一般取0.9-0.995```得到训练的xml文件，即可在test.py中使用