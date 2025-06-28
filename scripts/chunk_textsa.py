import os
import json
import re

# === Config ===
RAW_PATH = r"C:\Ordinance\data\raw"
CHUNK_OUTPUT_PATH = r"C:\Ordinance\data\chunks"

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def chunk_appendix_a(file_path, source_title=None):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r"""
    (?P<header>
        ^Article\s+[IVXLCDM]+,.*?$         # Match 'Article I,' line
        |
        ^Section\s+[A-Z]\..*?$             # Match 'Section A.,' line
    )
    (?P<body>.*?)
    (?=^Article\s+[IVXLCDM]+,|^Section\s+[A-Z]\.| \Z)
    """

    matches = re.finditer(pattern, text, re.MULTILINE | re.DOTALL | re.VERBOSE)

    chunks = []
    for match in matches:
        header = match.group("header").strip()
        body = match.group("body").strip()
        chunks.append({
            "header": header,
            "text": body
        })

    if not chunks:
        print(f"⚠️ No matches found in Appendix file: {source_title or os.path.basename(file_path)}")

    return chunks



def process_file(filename, title):
    file_path = os.path.join(RAW_PATH, filename)
    print(f"Processing: {file_path}")

    text = load_text(file_path)

    # Infer chapter from filename like "Chapter_1-1.txt"
    chapter = os.path.basename(filename).split("_")[1].replace(".txt", "").strip()

    chunks = chunk_appendix_a(file_path)

    output_filename = f"{title.replace(' ', '_').lower()}.json"
    output_path = os.path.join(CHUNK_OUTPUT_PATH, output_filename)

    os.makedirs(CHUNK_OUTPUT_PATH, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(chunks)} chunks to: {output_path}")

# === Process your actual files ===
process_file(r"C:\Ordinance\data\raw\Flood_Plain_Ordinance_-_Appendix_A.txt", "FLOOD PLAIN ORDINANCE APPENDIX A")
