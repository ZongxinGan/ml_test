# -*-coding:utf-8-*-

from PIL import Image
from multiprocessing import Process
import imagesim.histogram as htg
import imagesim.aHash as ah
import imagesim.pHash as ph
import imagesim.dHash as dh

if __name__ == '__main__':

    # read image files
    img1 = Image.open('imges1.png')
    img2 = Image.open('imges2.png')
    # img1.show()
    # img2.show()

    # Histogram Similarity Calculation
    # regularize the images
    img1_htg = htg.regularizeImage(img1)
    img2_htg = htg.regularizeImage(img2)
    
    hg1 = img1_htg.histogram()
    # print(img1.histogram())
    print('img1的样本点有{}个'.format(len(hg1)))
    hg2 = img2_htg.histogram()
    # print(img2.histogram())
    print('img2的样本点有{}个'.format(len(hg2)))

    # draw the histogram in a no-blocking way
    sub_thread = Process(target=htg.drawHistogram, args=(hg1, hg2,))
    sub_thread.start()

    # print the histogram similarity
    print('依据图片直方图距离计算相似度：{}'.format(htg.calMultipleHistogramSimilarity(img1_htg, img2_htg)))

    # aHash Calculation
    print('依据平均哈希算法计算相似度：{}/{}'.format(ah.calaHashSimilarity(img1, img2), 64))

    # pHash Calculation
    print('依据感知哈希算法计算相似度：{}/{}'.format(ph.calpHashSimilarity(img1, img2), 64))

    # dHash Calculation
    print('依据差异哈希算法计算相似度：{}/{}'.format(dh.caldHashSimilarity(img1, img2), 64))
