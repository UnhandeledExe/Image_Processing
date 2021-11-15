from skimage import data, io
from skimage.filters import apply_hysteresis_threshold


class ImgFileProcessing:

    def __init__(self, *args):
        self.img_stack = []
        if len(args) > 0:
            self.img_stack.append(io.imread(args[0]))

        else:
            self.img_stack.append(data.astronaut())

    def show_image(self):
        io.imshow(self.img_stack[-1])
        io.show()

    def save_image(self, name):
        io.imsave(name, self.img_stack[-1])

    def get_image(self):
        return self.img_stack[-1]

    def undo_changes(self):
        self.img_stack.pop()

    def apply_effect(self, effect, *args):
        self.img_stack.append(effect(self.img_stack[-1], *[i for i in args]))
