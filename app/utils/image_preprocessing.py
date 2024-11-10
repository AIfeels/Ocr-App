from PIL import Image, ImageFilter

def preprocess(image):
    image = Image.open(image)
    image = image.convert("L").resize((800, 800)).filter(ImageFilter.MedianFilter())
    return image
