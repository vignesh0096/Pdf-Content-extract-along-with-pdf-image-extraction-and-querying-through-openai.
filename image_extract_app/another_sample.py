import openai
import os
import base64
from PIL import Image
import io
import fitz
from paddleocr import PaddleOCR
import numpy as np


openai.api_key = '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'


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


def get_text(path):
    pdf_content = ''
    image_content = ""
    ocr = PaddleOCR(lang='en')
    with open(path,'rb') as file:
        file_bytes = file.read()
        base64_string = base64.b64encode(file_bytes).decode('utf-8')
        bytes_value = base64.b64decode(base64_string)
        pdf_document = fitz.open(stream=bytes_value)
        for i in range(pdf_document.page_count):
            page = pdf_document[i]
            pdf_image = page.get_images(full=True)
            pdf_text = page.get_text()
            pdf_content += pdf_text
            for img_index, img in enumerate(pdf_image):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)

                image_bytes = base_image["image"]
                image_io = Image.open(io.BytesIO(image_bytes))
                image_np = np.array(image_io)
                image_text = ocr.ocr(image_np)
                for line in image_text[0]:
                    image_content += line[1][0]
    prompt = f"""get the name,date of birth and what type of proof as proof from the given text.
    I want the result to be in json format{image_content}{pdf_content}"""
    result = get_completion(prompt)
    print(result)
    return result


# pa = [r"C:\Users\Vrdella\Desktop\Aadhar card.pdf",r"C:\Users\Vrdella\Desktop\Aadhar1 card.pdf"]
# for a in pa:
#     answer = get_text(a)
#     print(answer)
#