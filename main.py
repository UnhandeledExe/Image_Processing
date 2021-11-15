from GUI import GUI
from ImgFileProcessing import ImgFileProcessing
from Filters import Filters as fl

import numpy as np
from skimage import data, io
from skimage.exposure import rescale_intensity
from skimage import color
from skimage.transform import swirl
from skimage.morphology import square, closing, ball, cube

def main():
    IMAGE = ImgFileProcessing("images/cat.jpg")
    GUI(IMAGE)

    # IMAGE.show_image()

    # io.imshow(IMAGE.get_image())
    # io.show()

    # IMAGE.apply_effect(fl.gaussian, 10)
    # print(color.rgb2gray(IMAGE.get_image()))
    # IMAGE.show_image()

    #IMAGE.show_image()
    #IMAGE.undo_changes()
    #IMAGE.show_image()
    #test(1, 2, 3, 5, "bla")

    # print(IMAGE.get_image())
    # print(np.amax(IMAGE.get_image()))
    # print(np.amin(IMAGE.get_image()))
    # p1, p2 = np.percentile(IMAGE.get_image(), (2, 98))
    # print(p1)
    # print(p2)



if __name__ == '__main__':
    main()

