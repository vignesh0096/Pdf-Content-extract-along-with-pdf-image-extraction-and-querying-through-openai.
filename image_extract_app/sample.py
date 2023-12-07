import fitz
from paddleocr import PaddleOCR
import io
from PIL import Image
import numpy as np


def pdf_text_extract(path, i):
    ocr = PaddleOCR(lang='en')
    doc = fitz.open(f"{path}")

    file = open(f'output_file{i}.txt', 'w', encoding='utf-8')
    for i in range(doc.page_count):
        page = doc[i]
        pdf_text = page.get_text()
        if pdf_text:
            file.write('\n' + 'PDF Text' + '\n')
            file.write(pdf_text + '\n')
        img_list = page.get_images(full=True)

        for img_index, img in enumerate(img_list):
            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            image_io = Image.open(io.BytesIO(image_bytes))
            image_np = np.array(image_io)
            image_text = ocr.ocr(image_np)
            file.write('\n' + 'Image Text' + '\n')
            for line in image_text[0]:
                file.write(line[1][0] + '\n')

    doc.close()
    file.close()

