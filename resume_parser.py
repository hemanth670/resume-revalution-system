# ------------------------------------------------------------
# © 2025 Sarthak Raut
# Resume Relevance Check System
# All rights reserved. Unauthorized copying, modification,
# or distribution of this file is prohibited.
# ------------------------------------------------------------

import fitz  # PyMuPDF
import pdfplumber
import docx2txt

def extract_text_pymupdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_pdfplumber(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def parse_resume(resume_path):
    if resume_path.endswith(".pdf"):
        # Try PyMuPDF first, fallback to pdfplumber
        text = extract_text_pymupdf(resume_path)
        if not text.strip():
            text = extract_text_pdfplumber(resume_path)
        return text
    elif resume_path.endswith(".docx"):
        return docx2txt.process(resume_path)
    else:
        return ""

def parse_jd(jd_path):
    if jd_path.endswith(".pdf"):
        text = extract_text_pymupdf(jd_path)
        if not text.strip():
            text = extract_text_pdfplumber(jd_path)
        return text
    elif jd_path.endswith(".docx"):
        return docx2txt.process(jd_path)
    else:
        return ""