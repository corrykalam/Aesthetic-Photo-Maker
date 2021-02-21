from PIL import Image, ImageOps, ImageFilter
import random
import os
import sys

path = os.path.join(os.path.dirname(__file__), '../assets/decoration')
sys.path.insert(0, path)


class AestheticMaker:
    def __init__(self, background, photo):
        self.background = Image.open(background)
        self.photo = Image.open(photo)
        if self.photo.size[0] > 600 and self.photo.size[1] > 600:
            self.photo = self.photo.resize((550, 550), Image.ANTIALIAS)
        self.center = int((self.background.size[0]-self.photo.size[0])/2)

    def addBorderPhoto(self, color="yellow"):
        border = self.photo.resize(
            (
                self.photo.size[0]+30,
                self.photo.size[1]+30
            ),
            Image.ANTIALIAS
        )
        alpha = border.getchannel('A')
        fill = Image.new('RGBA', (border.size), color=color)
        fill.putalpha(alpha)
        center = int((fill.size[0]-self.photo.size[0])/2)
        fill.paste(self.photo, (center, center), self.photo)
        return fill

    def addPhoto(self):
        border = self.addBorderPhoto()
        return self.background.paste(
            border,
            (
                self.center,
                self.center
            ),
            border
        )

    def addSunflower(self, fixed_height=420):
        image = Image.open(path+'/sunflower.png')
        height_percent = (fixed_height / float(image.size[1]))
        width_size = int((float(image.size[0]) * float(height_percent)))
        image = image.resize((width_size, fixed_height), Image.NEAREST)
        self.background.paste(image, (0, self.photo.size[1]-100), image)

    def addNoiseImage(self):
        noise = Image.effect_noise(self.background.size, 5)
        self.background.paste(noise, (0, 0), noise)

    def sizeDecoration(self, files, fixed_height=420):
        image = Image.open(files)
        height_percent = (fixed_height / float(image.size[1]))
        width_size = int((float(image.size[0]) * float(height_percent)))
        image = image.resize((width_size, fixed_height), Image.NEAREST)
        return image

    def addDecoration(self):
        acdc = self.sizeDecoration(path+"/acdc.png", 300)
        jejeboy = self.sizeDecoration(path+"/jejeboy.png", 300)
        nirvana = self.sizeDecoration(path+"/nirvana.png", 150)
        trippy = self.sizeDecoration(path+"/trippy.png", 300)
        self.background.paste(
            acdc,
            (124, self.background.size[1]-299),
            acdc
        )
        self.background.paste(
            jejeboy,
            (391, 774),
            jejeboy
        )
        self.background.paste(
            nirvana,
            (500, 0),
            nirvana
        )
        self.background.paste(
            trippy,
            (0, 0),
            trippy
        )

    def create(self, decoration=True):
        if decoration:
            self.addDecoration()
        self.addPhoto()
        self.addSunflower()
        self.addNoiseImage()

    def save(self, filename):
        self.background.save(filename)

    def showImage(self):
        self.background.show()


if __name__ == '__main__':
    aesthestic = AestheticMaker("../background.jpg", "../photo2.png")
    aesthestic.create()
    aesthestic.save("cori.jpg")
