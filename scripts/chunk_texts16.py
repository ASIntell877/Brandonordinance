import os
import json
import re

# === Config ===
RAW_PATH = r"C:\Ordinance\data\raw"
CHUNK_OUTPUT_PATH = r"C:\Ordinance\data\chunks"

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def chunk_ordinance_file(file_path, source_title=None):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Pattern to match section headers:
    # Start of line (^)
    # Section number: 1-3 digits - 1-3 digits - 1-4 digits (to allow longer last group)
    # Followed by optional whitespace and rest of line (possibly title)
    # Then capture everything up to next section header or end of file
    pattern = (
        r"^(?P<section>\d{1,3}-\d{1,3}-\d{1,4})\s*(?P<title_line>[^\n]*)\n"
        r"(?P<body>.*?)(?=^\d{1,3}-\d{1,3}-\d{1,4}\s*[^\n]*\n|\Z)"
    )

    matches = re.finditer(pattern, text, re.DOTALL | re.MULTILINE)

    chunks = []
    for match in matches:
        section = match.group("section")
        title_line = match.group("title_line").strip()
        body = match.group("body").strip()

        # If title_line is empty, try to get title from first non-empty line of body
        if not title_line:
            # Split body into lines and find first non-empty line as title
            body_lines = body.splitlines()
            title = "(No title found)"
            for line in body_lines:
                if line.strip():
                    title = line.strip()
                    # Remove that line from body
                    body = "\n".join(body_lines[1:]).strip()
                    break
        else:
            title = title_line

        chunks.append({
            "section": section,
            "title": title,
            "text": body
        })

    if not chunks:
        print(f"⚠️ No matches found in file: {source_title or os.path.basename(file_path)}")

    return chunks


def process_file(filename, title):
    file_path = os.path.join(RAW_PATH, filename)
    print(f"Processing: {file_path}")

    text = load_text(file_path)

    # Infer chapter from filename like "Chapter_1-1.txt"
    chapter = os.path.basename(filename).split("_")[1].replace(".txt", "").strip()

    chunks = chunk_ordinance_file(file_path)

    output_filename = f"{title.replace(' ', '_').lower()}.json"
    output_path = os.path.join(CHUNK_OUTPUT_PATH, output_filename)

    os.makedirs(CHUNK_OUTPUT_PATH, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(chunks)} chunks to: {output_path}")

# === Process your actual files ===
process_file(r"C:\Ordinance\data\raw\Chapter_16-16.txt", "Chapter 16-16 EASEMENTS")