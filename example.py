from aesthestic.maker import AestheticMaker

# with decoration
maker1 = AestheticMaker("background.jpg", "ploy.png")
maker1.create()
maker1.save("maker1.jpg")
maker1.showImage()

# without decoration
maker2 = AestheticMaker("background.jpg", "ploy.png")
maker2.create(decoration=False)
maker2.save("maker2.jpg")
