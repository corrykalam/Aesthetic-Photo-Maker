# Aesthetic Photo Maker

Aesthetic Photo Maker is a Python script for edit photo aesthetic.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage

```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.