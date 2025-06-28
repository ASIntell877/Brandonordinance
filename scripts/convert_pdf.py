import fitz  # PyMuPDF
import os
import re

PDF_FOLDER = r"C:\Ordinance\data\raw\pdf"
OUTPUT_FOLDER = r"C:\Ordinance\data\raw"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def sanitize_filename(text):
    # Remove illegal filename characters and limit length
    text = re.sub(r'[\\/*?:"<>|]', "", text)
    return text.strip().replace(" ", "_")[:100] + ".txt"

def extract_title_from_first_page(doc):
    # Pull first page and try to extract chapter title
    first_page_text = doc[0].get_text().strip()
    # Look for something like "CHAPTER 5 – PARKING REGULATIONS"
    match = re.search(r'CHAPTER\s+\d+[^:\n]*', first_page_text, re.IGNORECASE)
    if match:
        return sanitize_filename(match.group(0).title())
    else:
        return None

def convert_all_pdfs():
    for filename in os.listdir(PDF_FOLDER):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(PDF_FOLDER, filename)
            try:
                doc = fitz.open(filepath)
                title = extract_title_from_first_page(doc)
                if not title:
                    print(f"⚠️ No title found in {filename}, using fallback name")
                    title = sanitize_filename(filename.replace(".pdf", ""))

                output_path = os.path.join(OUTPUT_FOLDER, title)
                full_text = "\n".join([page.get_text() for page in doc])
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(full_text)

                print(f"✅ Converted: {filename} → {title}")
            except Exception as e:
                print(f"❌ Failed to process {filename}: {e}")

convert_all_pdfs()
