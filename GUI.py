from tkinter import *
from PIL import ImageTk, Image
from Filters import Filters as fl


class GUI:
    def __init__(self, ifp):
        self.img = ifp
        self.root = Tk()

        # Image
        self.imtemp = ImageTk.PhotoImage(Image.fromarray(self.img.get_image()))
        self.img_loc = Label(self.root, image=self.imtemp)

        # Frames
        self.filter_frame = LabelFrame(self.root, text='Filters', padx=5, pady=5)  # Filter Frames
        self.transformation_frame = LabelFrame(self.root, text='Transformation', padx=5, pady=5)  # Transformation Frame
        self.morphology_frame = LabelFrame(self.root, text='Morphology', padx=5, pady=5)  # Morphology Frame
        self.exposure_frame = LabelFrame(self.root, text='Exposure', padx=5, pady=5)  # Exposure Frame
        self.histogram_frame = LabelFrame(self.root,  text='Histogram',  padx=5, pady=5)  # Histogram Frame
        self.video_frame = LabelFrame(self.root,  text='Video?',  padx=5, pady=5)  # Video Frame

        # Buttons Filters
        self.fl1 = Button(self.filter_frame, text='Gabor', command=lambda: self.filter_button(fl.gabor, 30))
        self.fl2 = Button(self.filter_frame, text='Gaussian', command=lambda: self.filter_button(fl.gaussian, .1))
        self.fl3 = Button(self.filter_frame, text='Hessian', command=lambda: self.filter_button(fl.hessian, 1, 10, 2))
        self.fl4 = Button(self.filter_frame, text='Laplace', command=lambda: self.filter_button(fl.laplace, 3))
        self.fl5 = Button(self.filter_frame, text='Meijering', command=lambda: self.filter_button(fl.meijering, 1, 10, 2))
        self.fl6 = Button(self.filter_frame, text='Farid', command=lambda: self.filter_button(fl.farid))
        self.fl7 = Button(self.filter_frame, text='Prewitt', command=lambda: self.filter_button(fl.prewitt))
        self.fl8 = Button(self.filter_frame, text='Hys_Thr', command=lambda: self.filter_button(fl.hys_thr))
        self.fl9 = Button(self.filter_frame, text='Frangi', command=lambda: self.filter_button(fl.frangi))
        self.fl10 = Button(self.filter_frame, text='Median', command=lambda: self.filter_button(fl.median))

        # Transformation Layout Start -----------------------------------------------------------
        # Buttons
        self.tr1 = Button(self.transformation_frame, text='Resize', command=lambda: self.transformation_button())
        self.tr2 = Button(self.transformation_frame, text='Rotate', command=lambda: self.transformation_button())
        self.tr3 = Button(self.transformation_frame, text='Swirl', command=lambda: self.transformation_button())
        self.tr41 = Button(self.transformation_frame, text='Vertical Flip', command=lambda: self.transformation_button())
        self.tr42 = Button(self.transformation_frame, text='Horizontal Flip', command=lambda: self.transformation_button())
        self.tr5 = Button(self.transformation_frame, text='Crop', command=lambda: self.transformation_button())

        # Entries
        self.te11 = Entry(self.transformation_frame)
        self.te12 = Entry(self.transformation_frame)

        self.te2 = Scale(self.transformation_frame, from_=-180, to=180, orient=HORIZONTAL)

        self.te31 = Entry(self.transformation_frame)
        self.te32 = Entry(self.transformation_frame)

        # Labels
        self.tl11 = Label(self.transformation_frame, text='X : ')
        self.tl12 = Label(self.transformation_frame, text='Y : ')

        self.tl2 = Label(self.transformation_frame, text='Angle: ')

        self.tl31 = Label(self.transformation_frame, text='Radius : ')
        self.tl32 = Label(self.transformation_frame, text='Strength : ')
        # Transformation Layout End ------------------------------------------------------------

        # Morphology Layout Start -----------------------------------------------------------
        self.mf_var = IntVar()
        self.ms_var = IntVar()

        self.mf_var.set(1)
        self.ms_var.set(1)
        # Buttons
        self.morph = Button(self.morphology_frame, text='Morph', command=lambda: self.morphology_button())

        # Entries
        self.mrb1 = Radiobutton(self.morphology_frame, text='Morph1', variable=self.mf_var, value=1)
        self.mrb2 = Radiobutton(self.morphology_frame, text='Morph2', variable=self.mf_var, value=2)
        self.mrb3 = Radiobutton(self.morphology_frame, text='Morph3', variable=self.mf_var, value=3)
        self.mrb4 = Radiobutton(self.morphology_frame, text='Morph4', variable=self.mf_var, value=4)
        self.mrb5 = Radiobutton(self.morphology_frame, text='Morph5', variable=self.mf_var, value=5)
        self.mrb6 = Radiobutton(self.morphology_frame, text='Morph6', variable=self.mf_var, value=6)
        self.mrb7 = Radiobutton(self.morphology_frame, text='Morph7', variable=self.mf_var, value=7)
        self.mrb8 = Radiobutton(self.morphology_frame, text='Morph8', variable=self.mf_var, value=8)
        self.mrb9 = Radiobutton(self.morphology_frame, text='Morph9', variable=self.mf_var, value=9)
        self.mrb10 = Radiobutton(self.morphology_frame, text='Morph10', variable=self.mf_var, value=10)

        self.ms1 = Radiobutton(self.morphology_frame, text='Shape1', variable=self.ms_var, value=1)
        self.ms2 = Radiobutton(self.morphology_frame, text='Shape2', variable=self.ms_var, value=2)

        self.m_size = Entry(self.morphology_frame, width=10)

        # Labels
        self.ml1 = Label(self.morphology_frame, text='Methods')
        self.ml2 = Label(self.morphology_frame, text='Shapes')
        self.ml3 = Label(self.morphology_frame, text='Size')
        # Morphology Layout End---------------------------------------------------------------------------------

        # Exposure Start ---------------------------------------------------------------------------------
        self.es = Scale(self.exposure_frame, from_=1, to=100, orient=HORIZONTAL)
        self.eb = Button(self.exposure_frame, text='Apply', command=lambda: self.exposure_button())
        self.el = Label(self.exposure_frame, text='%')
        # Exposure End ---------------------------------------------------------------------------------

        # Histogram Start -----------------------------------------------------------------------
        self.his = Button(self.histogram_frame, text='Show Histogram', command=lambda: self.histogram_button())
        # Histogram End -------------------------------------------------------------------

        # Video Start ---------------------------------------
        self.vibut = Button(self.video_frame, text='VideoSomething', command=lambda: self.video_button())
        # Video End ------------------------------------------

        self.undob = Button(self.root, text='Undo', command=self.undo_button, state=DISABLED)

        # Grids ------------------------------------------------------------
        # Grid Image
        self.img_loc.grid(row=0, column=4, rowspan=3)

        # Grid Frames
        self.filter_frame.grid(row=0, column=0, columnspan=2, sticky='nw', padx=5, pady=5)
        self.transformation_frame.grid(row=1, column=0, columnspan=2, sticky='nw', padx=5, pady=5)
        self.morphology_frame.grid(row=2, column=0, rowspan=2, sticky='nw', padx=5, pady=5)
        self.exposure_frame.grid(row=2, column=1, padx=5, pady=5, sticky='nw')

        # Frame Grid Buttons Filters
        self.fl1.grid(row=0, column=0, sticky='nw')
        self.fl2.grid(row=0, column=1, sticky='nw')
        self.fl3.grid(row=0, column=2, sticky='nw')
        self.fl4.grid(row=0, column=3, sticky='nw')
        self.fl5.grid(row=1, column=0, sticky='nw')
        self.fl6.grid(row=1, column=1, sticky='nw')
        self.fl7.grid(row=1, column=2, sticky='nw')
        self.fl8.grid(row=1, column=3, sticky='nw')
        self.fl9.grid(row=2, column=0, sticky='nw')
        self.fl10.grid(row=2, column=0, sticky='nw')

        # Frame Grid Buttons Transformation
        self.tr1.grid(row=0, column=4, sticky='nw')
        self.tr2.grid(row=1, column=4)
        self.tr3.grid(row=2, column=4)
        self.tr41.grid(row=3, column=0)
        self.tr42.grid(row=3, column=1)

        # Frame Grid Entry Transformation
        self.te11.grid(row=0, column=1, sticky='nw', padx=2)
        self.te12.grid(row=0, column=3, sticky='nw', padx=2)

        self.te2.grid(row=1, column=1, sticky='w')

        self.te31.grid(row=2, column=1)
        self.te32.grid(row=2, column=3)

        # Frame Grid Label Transformation
        self.tl11.grid(row=0, column=0, stick='n')
        self.tl12.grid(row=0, column=2, stick='n')

        self.tl2.grid(row=1, column=0, sticky='w')

        self.tl31.grid(row=2, column=0)
        self.tl32.grid(row=2, column=2)

        # Frame Grid Button Morph
        self.morph.grid(row=10, column=2, sticky='s')

        # Frame Grid Entry Morph
        self.mrb1.grid(row=1, column=0, sticky='w')
        self.mrb2.grid(row=2, column=0, sticky='w')
        self.mrb3.grid(row=3, column=0, sticky='w')
        self.mrb4.grid(row=4, column=0, sticky='w')
        self.mrb5.grid(row=5, column=0, sticky='w')
        self.mrb6.grid(row=6, column=0, sticky='w')
        self.mrb7.grid(row=7, column=0, sticky='w')
        self.mrb8.grid(row=8, column=0, sticky='w')
        self.mrb9.grid(row=9, column=0, sticky='w')
        self.mrb10.grid(row=10, column=0, sticky='w')

        self.ms1.grid(row=1, column=1, sticky='w')
        self.ms2.grid(row=2, column=1, sticky='w')

        self.m_size.grid(row=4, column=1)

        # Frame Grid Label Morph
        self.ml1.grid(row=0, column=0, stick='w')
        self.ml2.grid(row=0, column=1, stick='w')
        self.ml3.grid(row=3, column=1, stick='w')

        # Frame Grid Exposure
        self.el.grid(row=0, column=0)
        self.eb.grid(row=0, column=2)
        self.es.grid(row=0, column=1)

        self.undob.grid(row=10, column=0)

        self.root.mainloop()

    def filter_button(self, filter, *args):
        self.activate_undo_button()
        self.img_loc.grid_forget()
        self.img.apply_effect(filter, *[i for i in args])
        self.imtemp = ImageTk.PhotoImage(Image.fromarray(self.img.get_image()))
        self.img_loc = Label(self.root, image=self.imtemp)
        self.img_loc.grid(row=0, column=4, rowspan=3)

    def transformation_button(self, *args):
        pass

    def morphology_button(self, *args):
        pass

    def exposure_button(self):
        self.activate_undo_button()
        self.img_loc.grid_forget()
        self.img.apply_effect(fl.re_intese, self.es.get())
        self.imtemp = ImageTk.PhotoImage(Image.fromarray(self.img.get_image()))
        self.img_loc = Label(self.root, image=self.imtemp)
        self.img_loc.grid(row=0, column=4, rowspan=3)

    def histogram_button(self):
        pass

    def video_button(self):
        pass

    def undo_button(self):
        self.img_loc.grid_forget()
        self.img.undo_changes()
        self.imtemp = ImageTk.PhotoImage(Image.fromarray(self.img.get_image()))
        self.img_loc = Label(self.root, image=self.imtemp)
        self.img_loc.grid(row=0, column=4, rowspan=3)
        if len(self.img.img_stack) == 1:
            self.undob = Button(self.root, text='Undo', command=self.undo_button, state=DISABLED)
            self.undob.grid(row=10, column=0)

    def activate_undo_button(self):
        self.undob = Button(self.root, text='Undo', command=self.undo_button, state=ACTIVE)
        self.undob.grid(row=10, column=0)
