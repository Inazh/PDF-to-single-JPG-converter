import os
import fitz
from PIL import Image
from tkinter import Tk, filedialog

Tk().withdraw()

pdf_path = filedialog.askopenfilename(
    title="Select PDF file",
    filetypes=[("PDF Files", "*.pdf")]
)

if not pdf_path:
    exit()

base_name = os.path.splitext(os.path.basename(pdf_path))[0]
output_jpg = f"{base_name}_Convertbined.jpg"

app_dir = os.path.dirname(os.path.abspath(__file__))

doc = fitz.open(pdf_path)
images = []

for page in doc:
    pix = page.get_pixmap(dpi=200)
    img = Image.frombytes(
        "RGB",
        (pix.width, pix.height),
        pix.samples
    )
    images.append(img)

doc.close()

width = max(img.width for img in images)
total_height = sum(img.height for img in images)

merged_image = Image.new("RGB", (width, total_height), "white")

y_offset = 0
for img in images:
    merged_image.paste(img, (0, y_offset))
    y_offset += img.height

output_path = os.path.join(app_dir, output_jpg)
merged_image.save(output_path, "JPEG")

print(f"File successfully created:\n{output_path}")
