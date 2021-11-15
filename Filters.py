from enum import Enum
import numpy as np
from skimage.filters import gabor, gaussian, hessian, laplace, \
    meijering, farid, prewitt, apply_hysteresis_threshold, \
    frangi, median
from skimage.exposure import rescale_intensity, histogram
from skimage.transform import resize, rotate, swirl
from skimage.morphology import erosion, dilation, closing, opening, white_tophat, black_tophat, \
    square, cube, ball, disk
from skimage import color, img_as_float
from skimage.util import crop


class Shapes(Enum):
    square = 1,
    disk = 2,
    cube = 3,
    ball = 4


class ShapeGen:#TODO DELETE NONE VALUES?
    def __init__(self, shape_type, shape_val):
        self.picked_shape = None
        if shape_type == Shapes.square:
            self.picked_shape = square(shape_val)
        elif shape_type == Shapes.disk:
            self.picked_shape = disk(shape_val)
        elif shape_type == Shapes.cube:
            self.picked_shape = cube(shape_val)
        elif shape_type == Shapes.ball:
            self.picked_shape = ball(shape_val)
        else:
            self.picked_shape = None

    def get_shape(self):
        return self.picked_shape


class Filters:

    #Standart Filters Start
    @staticmethod
    def gabor(img, fr): #Filter 1
        fr, fi = gabor(color.rgb2gray(img), frequency=fr)
        return fr

    @staticmethod
    def gaussian(img, sigma): #Filter 2
        return gaussian(img, sigma=sigma, multichannel=False)

    @staticmethod
    def hessian(img, start, end, step): #Filter 3
        return hessian(img, sigmas=(start, end, step), mode='reflect')

    @staticmethod
    def laplace(img, ksize=3): #Filter 4
        return laplace(img, ksize=ksize)

    @staticmethod
    def meijering(img, low, high, step): #Filter 5
        return meijering(img, sigmas=range(low, high, step))

    @staticmethod
    def farid(img): #Filter 6
        return farid(color.rgb2gray(img))

    @staticmethod
    def prewitt(img): #Filter 7
        return prewitt(img)

    @staticmethod
    def hys_thr(img, low=.6, high=.8): #Filter 8
        return apply_hysteresis_threshold(color.rgb2gray(img), low, high).astype(int)

    @staticmethod
    def frangi(img, low=1, high=10, step=2): #Filter 9
        return frangi(color.rgb2gray(img), sigmas=range(low, high, step))

    @staticmethod
    def median(img): #Filters 10
        return median(img, mode='constant')
    #Filters End

    #Histogram Start ???? TODO fix this
    # @staticmethod
    # def histogram(img):
    #     plt.plot(histogram(img))
    #     plt.show()
    #Histogram End

    #Exposure
    @staticmethod
    def re_intese(img, per):
        p1, p2 = np.percentile(img, (1, per))
        return rescale_intensity(img, in_range=(p1, p2))

    #Transformations Start

    @staticmethod
    def resize(img, out_shape): #Transform 1
        return resize(img, out_shape)

    @staticmethod
    def rotate(img, angle): #Transform 2
        return rotate(img, angle)

    @staticmethod
    def swirl(img, radius, strength): #Transfrom 3
        return swirl(img, radius=radius, strength=strength)

    @staticmethod
    def flip_v(img): #Transform 4.1
        return img[:, ::-1]

    @staticmethod
    def flip_h(img): #Transform 4.2
        return img[::-1, :]

    @staticmethod
    def crop(img): #Transform 5
        return crop(img, ((100, 100), (200, 200), (0, 0)), copy=False)

    #Transformations End

    #Morphology Start
    # TODO ADD SHAPE AND SIZE SELECTION, CHECK FOR IMG SHAPE
    @staticmethod
    def erosion(img): #Morph 1
        return erosion(img, ShapeGen(Shapes.cube, 3).get_shape())

    @staticmethod
    def dilation(img): #Morph 2
        return dilation(img, ShapeGen(Shapes.cube, 3).get_shape())

    @staticmethod
    def closing(img): #Morph 3
        return closing(img, ShapeGen(Shapes.cube, 3).get_shape())

    @staticmethod
    def opening(img): #Morph 4
        return opening(img, ShapeGen(Shapes.cube, 3).get_shape())

    @staticmethod
    def white_tophat(img): #Morph 5
        return white_tophat(img, ShapeGen(Shapes.cube, 3).get_shape())

    @staticmethod
    def black_tophat(img): #Morph 6
        return black_tophat(img, ShapeGen(Shapes.cube, 3).get_shape())

