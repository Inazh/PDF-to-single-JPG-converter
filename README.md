# PDF to Single JPG Converter (PyMuPDF)

This project is a simple Python application that converts a multi-page PDF file into **one single JPG image** by vertically combining all pages.  
It uses **PyMuPDF** for PDF rendering and **Pillow** for image processing.

---

## Features
- Select PDF file using File Explorer
- Convert all PDF pages into a single JPG image

---

## Installation

### 1. Install Python
Make sure Python is installed on your system.

Check version:
```bash
python --version 
```

### 2. Install Requirements
Install the application dependencies.

Make sure `requirements.txt` contains:
```txt
pymupdf
pillow
```

Then install them using:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Run the application with:
```bash
python app.py
```
