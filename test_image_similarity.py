# -*-coding:utf-8-*-

import PIL
from PIL import Image

class Geetest(object):
    def __init__(self):
        pass

    def find_diffrectange_of_two_image(self, img_src1, img_src2):
        try:
            image1 = Image.open(img_src1)
            image2 = Image.open(img_src2)

            width1, height1 = image1.size
            width2, height2 = image2.size

            if width1 != width2 or height1 != height2:
                return []

            left = 0
            pixel_list = []
            for i in range(width1):
                for j in range(height1):
                    pixel_list.append(self.is_pixel_not_equal(image1, image2, i, j))
            return pixel_list
        except Exception as e:
            print(str(e))
            return []

    def is_pixel_not_equal(self, image1, image2, i, j):
        pixel1 = image1.getpixel((i,j))
        pixel2 = image2.getpixel((i,j))

        for i in range(3):
            if abs(pixel1[i] - pixel2[i]) > 100:
                return 0
        return 1

if __name__ == '__main__':
    pixel_list = Geetest().find_diffrectange_of_two_image('imges1.png', 'imges2.png')
    print(pixel_list.count(1)*1.0/len(pixel_list))
    
    