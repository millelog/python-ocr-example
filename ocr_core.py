try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    image = Image.open(filename)
    #image = image.rotate(270, expand=1)
    image.show(command='fim')
    text = pytesseract.image_to_string(image)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text  # Then we will print the text in the image
