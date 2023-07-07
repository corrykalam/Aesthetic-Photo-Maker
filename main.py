from rembg import remove
from aesthestic.maker import AestheticMaker
from PIL import Image

name_file = "input.jpeg"

img = Image.open(name_file)
out = remove(img)
out.save("output.png")


maker1 = AestheticMaker("background.jpg", "output.png")
maker1.create()
maker1.save("maker1.jpg")
maker1.showImage()

# without decoration
maker2 = AestheticMaker("background.jpg", "output.png")
maker2.create(decoration=False)
maker2.save("maker2.jpg")
