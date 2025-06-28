import os
import json
import re

# === Config ===
RAW_PATH = r"C:\Ordinance\data\raw"
CHUNK_OUTPUT_PATH = r"C:\Ordinance\data\chunks"

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def split_into_sentences(text):
    # Simple regex to split into sentences. You can swap with nltk.sent_tokenize if you want.
    sentence_endings = re.compile(r'(?<=[.!?]) +')
    return sentence_endings.split(text)

def chunk_by_lines(filepath, source, max_chars=4000):
    chunks = []
    chunk_index = 1
    current_chunk = ""

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()  # This preserves all newlines

    for line in lines:
        if len(current_chunk) + len(line) > max_chars:
            chunks.append({
                'chunk_index': chunk_index,
                'text': current_chunk,  # don't strip
                'source': source
            })
            chunk_index += 1
            current_chunk = line
        else:
            current_chunk += line

    if current_chunk:
        chunks.append({
            'chunk_index': chunk_index,
            'text': current_chunk,
            'source': source
        })

    return chunks

def process_file(filename, title):
    file_path = os.path.join(RAW_PATH, filename)
    print(f"Processing: {file_path}")

    text = load_text(file_path)

    # Infer chapter from filename like "Chapter_1-1.txt"
    chapter = os.path.basename(filename).split("_")[1].replace(".txt", "").strip()

    chunks = chunk_by_lines(file_path, source=title)

    output_filename = f"{title.replace(' ', '_').lower()}.json"
    output_path = os.path.join(CHUNK_OUTPUT_PATH, output_filename)

    os.makedirs(CHUNK_OUTPUT_PATH, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(chunks)} chunks to: {output_path}")

# === Process your actual files ===
process_file(r"C:\Ordinance\data\raw\Chapter__2-4.txt", "Chapter 2-4 PROVISIONS FOR SELLING, DISTRIBUTING AND CONSUMING ALCOHOL")
process_file(r"C:\Ordinance\data\raw\Chapter__6-5.txt", "Chapter  6-5 GARBAGE PROVISIONS")
process_file(r"C:\Ordinance\data\raw\Chapter__6-6.txt", "Chapter  6-6 BICYCLES")
process_file(r"C:\Ordinance\data\raw\Chapter__6-7.txt", "Chapter  6-7 AMBULANCE SERVICES")
process_file(r"C:\Ordinance\data\raw\Chapter_1-1.txt", "Chapter 1-1 NAME, BOUNDARIES, POWER AND GENERAL PROVISIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_1-2.txt", "Chapter 1-2 ELECTIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_1-3.txt", "Chapter 1-3 THE MAYOR, CITY COUNCIL & COMMITTEES")
process_file(r"C:\Ordinance\data\raw\Chapter_1-4.txt", "Chapter 1-4 CITY  APPOINTIVE  OFFICIALS")
process_file(r"C:\Ordinance\data\raw\Chapter_1-5.txt", "Chapter 1-5 DUTIES  AND  COMPENSATION  OF APPOINTIVE  OFFICIALS")
process_file(r"C:\Ordinance\data\raw\Chapter_1-6.txt", "Chapter 1-6 FINANCIAL  REGULATIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_1-7.txt", "Chapter 1-7 CODE  OF  CONDUCT;   FEDERAL  GRANTS")
process_file(r"C:\Ordinance\data\raw\Chapter_1-8.txt", "Chapter 1-8 FINANCE")
process_file(r"C:\Ordinance\data\raw\Chapter_1-9.txt", "Chapter 1-9 RECORDS")
process_file(r"C:\Ordinance\data\raw\Chapter_1-10.txt", "Chapter 1-10 SECTION  IN  GENERAL")
process_file(r"C:\Ordinance\data\raw\Chapter_1-11.txt", "Chapter 1-11 ESTABLISHING  PLANNING  &  ZONING  COMMISSION")
process_file(r"C:\Ordinance\data\raw\Chapter_2-1.txt", "Chapter 2-1 ALCOHOLIC  BEVERAGES")
process_file(r"C:\Ordinance\data\raw\Chapter_2-2.txt", "Chapter 2-2 GENERAL")
process_file(r"C:\Ordinance\data\raw\Chapter_2-3.txt", "Chapter 2-3 LICENSING")
process_file(r"C:\Ordinance\data\raw\Chapter_3-1.txt", "Chapter 3-1 ANIMALS")
process_file(r"C:\Ordinance\data\raw\Chapter_3-2.txt", "Chapter 3-2 ANIMALS")
process_file(r"C:\Ordinance\data\raw\Chapter_3-3.txt", "Chapter 3-3 LIVESTOCK")
process_file(r"C:\Ordinance\data\raw\Chapter_3-4.txt", "Chapter 3-4 FOWL")
process_file(r"C:\Ordinance\data\raw\Chapter_4-1.txt", "Chapter 4-1 ADOPTION OF NATIONAL CODE")
process_file(r"C:\Ordinance\data\raw\Chapter_4-4.txt", "Chapter 4-4 BUILDINGS  TO  BE  MOVED")
process_file(r"C:\Ordinance\data\raw\Chapter_4-5.txt", "Chapter 4-5 BUILDING  PROVISIONS  GENERALLY")
process_file(r"C:\Ordinance\data\raw\Chapter_4-6.txt", "Chapter 4-6 ASSIGNMENT  OF  BUILDING  NUMBERS")
process_file(r"C:\Ordinance\data\raw\Chapter_4-7.txt", "Chapter 4-7 ABATEMENT  OF  DANGEROUS  BUILDINGS")
process_file(r"C:\Ordinance\data\raw\Chapter_4-8.txt", "Chapter 4-8 CERTIFICATE  OF  OCCUPANCY")
process_file(r"C:\Ordinance\data\raw\Chapter_5-1.txt", "Chapter 5-1 RULES  AND  REGULATIONS  OF  THE  STATE FIRE  MARSHALL'S  OFFICE")
process_file(r"C:\Ordinance\data\raw\Chapter_5-2.txt", "Chapter 5-2 FIRE PROTECTION")
process_file(r"C:\Ordinance\data\raw\Chapter_6-1.txt", "Chapter 6-1 GENERAL  PROVISIONS  WITH  REGARD  TO  LICENSES")
process_file(r"C:\Ordinance\data\raw\Chapter_6-2.txt", "Chapter 6-2 CONTRACTOR’S LICENSE PROVISIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_6-3.txt", "Chapter 6-3 PEDDLERS  AND  VENDORS")
process_file(r"C:\Ordinance\data\raw\Chapter_6-4.txt", "Chapter 6-4 LANDSCAPE IRRIGATION CONTRACTORS")
process_file(r"C:\Ordinance\data\raw\Chapter_6-8.txt", "Chapter 6-8 SEWER CLEANING SERVICES")
process_file(r"C:\Ordinance\data\raw\Chapter_6-9.txt", "Chapter 6-9 VIDEO LOTTERY MACHINES")
process_file(r"C:\Ordinance\data\raw\Chapter_6-10.txt", "Chapter 6-10 TREE PESTICIDE APPLICATORS LICENSE")
process_file(r"C:\Ordinance\data\raw\Chapter_7-1.txt", "Chapter 7-1 FIREWORKS")
process_file(r"C:\Ordinance\data\raw\Chapter_7-2.txt", "Chapter 7-2 PUBLIC  NUISANCES")
process_file(r"C:\Ordinance\data\raw\Chapter_7-3.txt", "Chapter 7-3 SPECIFIC  OFFENSES")
process_file(r"C:\Ordinance\data\raw\Chapter_7-4.txt", "Chapter 7-4 PROSTITUTION,  GAMBLING,  AND  INDECENCY")
process_file(r"C:\Ordinance\data\raw\Chapter_7-5.txt", "Chapter 7-5 OFFENSES  AGAINST  THE  PUBLIC  PEACE")
process_file(r"C:\Ordinance\data\raw\Chapter_7-6.txt", "Chapter 7-6 MINORS")
process_file(r"C:\Ordinance\data\raw\Chapter_7-7.txt", "Chapter 7-7 JUNK")
process_file(r"C:\Ordinance\data\raw\Chapter_7-10.txt", "Chapter 7-10 CHAPTER 7-10")
process_file(r"C:\Ordinance\data\raw\Chapter_8-1.txt", "Chapter 8-1 PAWNBROKERS - PURPOSE  &  DEFINITIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_8-2.txt", "Chapter 8-2 PAWNBROKERS - LICENSE")
process_file(r"C:\Ordinance\data\raw\Chapter_8-3.txt", "Chapter 8-3 PAWNBROKERS - RECORDS")
process_file(r"C:\Ordinance\data\raw\Chapter_8-4.txt", "Chapter 8-4 PAWNBROKERS - BOOKKEEPING  REQUIREMENTS")
process_file(r"C:\Ordinance\data\raw\Chapter_8-5.txt", "Chapter 8-5 PAWNBROKERS - GENERAL")
process_file(r"C:\Ordinance\data\raw\Chapter_8-6.txt", "Chapter 8-6 ADULT USE - DEFINITIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_8-7.txt", "Chapter 8-7 ADULT USES - REGULATIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_8-8.txt", "Chapter 8-8 ADULT USES -LICENSING")
process_file(r"C:\Ordinance\data\raw\Chapter_8-9.txt", "Chapter 8-9 ADULT USES - PERFORMER RESTRICTIONS AND REQUIREMENTS")
process_file(r"C:\Ordinance\data\raw\Chapter_10-1.txt", "Chapter 10-1 SIDEWALKS  AND  ALLEYS  -  GENERAL")
process_file(r"C:\Ordinance\data\raw\Chapter_10-2.txt", "Chapter 10-2 SNOW AND ICE REMOVAL")
process_file(r"C:\Ordinance\data\raw\Chapter_10-3.txt", "Chapter 10-3 EXCAVATIONS  IN  PUBLIC  AREAS")
process_file(r"C:\Ordinance\data\raw\Chapter_10-4.txt", "Chapter 10-4 PUBLIC  GROUNDS  IN  GENERAL")
process_file(r"C:\Ordinance\data\raw\Chapter_11-1.txt", "Chapter 11-1 MUNICIPAL  SALES  AND  SERVICE  TAX")
process_file(r"C:\Ordinance\data\raw\Chapter_11-2.txt", "Chapter 11-2 SPECIAL TAX CLASSIFICATION")
process_file(r"C:\Ordinance\data\raw\Chapter_11-3.txt", "Chapter 11-3 COUNTY  TAX  LEVY")
process_file(r"C:\Ordinance\data\raw\Chapter_11-4.txt", "Chapter 11-4 MUNICIPAL SALES AND SERVICE TAX")
process_file(r"C:\Ordinance\data\raw\Chapter_11-6.txt", "Chapter 11-6 SPECIAL ASSESSMENTS")
process_file(r"C:\Ordinance\data\raw\Chapter_12-1.txt", "Chapter 12-1 IN  GENERAL")
process_file(r"C:\Ordinance\data\raw\Chapter_12-2.txt", "Chapter 12-2 ENFORCEMENT  AND  OBEDIENCE")
process_file(r"C:\Ordinance\data\raw\Chapter_12-3.txt", "Chapter 12-3 PROCEDURES  UPON  ARREST")
process_file(r"C:\Ordinance\data\raw\Chapter_12-4.txt", "Chapter 12-4 ACCIDENTS")
process_file(r"C:\Ordinance\data\raw\Chapter_12-5.txt", "Chapter 12-5 OPERATION  OF  VEHICLES  GENERALLY")
process_file(r"C:\Ordinance\data\raw\Chapter_12-6.txt", "Chapter 12-6 RIGHT-OF-WAY  REGULATIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_12-7.txt", "Chapter 12-7 TRAFFIC  CONTROL  SIGNS,  SIGNALS  AND  DEVICES")
process_file(r"C:\Ordinance\data\raw\Chapter_12-8.txt", "Chapter 12-8 SPEED")
process_file(r"C:\Ordinance\data\raw\Chapter_12-9.txt", "Chapter 12-9 ONE-WAY  STREETS  AND  ALLEYS")
process_file(r"C:\Ordinance\data\raw\Chapter_12-10.txt", "Chapter 12-10 TURNS")
process_file(r"C:\Ordinance\data\raw\Chapter_12-11.txt", "Chapter 12-11 TURNING  AND  STOPPING  SIGNALS")
process_file(r"C:\Ordinance\data\raw\Chapter_12-12.txt", "Chapter 12-12 REQUIRED  STOPS  AND  YIELD  INTERSECTIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_12-13.txt", "Chapter 12-13 MISCELLANEOUS  DRIVING  RULES")
process_file(r"C:\Ordinance\data\raw\Chapter_12-14.txt", "Chapter 12-14 STANDING  AND  PARKING")
process_file(r"C:\Ordinance\data\raw\Chapter_12-15.txt", "Chapter 12-15 PEDESTRIANS")
process_file(r"C:\Ordinance\data\raw\Chapter_12-16.txt", "Chapter 12-16 SNOWMOBILES")
process_file(r"C:\Ordinance\data\raw\Chapter_12-17.txt", "Chapter 12-17 TRUCK  ROUTE  SYSTEM")
process_file(r"C:\Ordinance\data\raw\Chapter_12-18.txt", "Chapter 12-18 MOTORCYCLES  AND  MOPEDS")
process_file(r"C:\Ordinance\data\raw\Chapter_12-19.txt", "Chapter 12-19 MOTOR  VEHICLES")
process_file(r"C:\Ordinance\data\raw\Chapter_12-20.txt", "Chapter 12-20 ABANDONED  VEHICLES")
process_file(r"C:\Ordinance\data\raw\Chapter_12-21.txt", "Chapter 12-21 GOLF CART USE IN CITY LIMITS")
process_file(r"C:\Ordinance\data\raw\Chapter_13-1.txt", "Chapter 13-1 TREES AND NOXIOUS VEGETATION")
process_file(r"C:\Ordinance\data\raw\Chapter_13-2.txt", "Chapter 13-2 NOXIOUS  WEEDS")
process_file(r"C:\Ordinance\data\raw\Chapter_14-2.txt", "Chapter 14-2 REGULATION  OF  WATER  USE")
process_file(r"C:\Ordinance\data\raw\Chapter_14-3.txt", "Chapter 14-3 WATER  AND  SEWER  SERVICE  IN  GENERAL")
process_file(r"C:\Ordinance\data\raw\Chapter_14-4.txt", "Chapter 14-4 RATES  AND  CHARGES")
process_file(r"C:\Ordinance\data\raw\Chapter_14-5.txt", "Chapter 14-5 WASTEWATER  SERVICE  CHARGES")
process_file(r"C:\Ordinance\data\raw\Chapter_14-6.txt", "Chapter 14-6 GAS  ENERGY")
process_file(r"C:\Ordinance\data\raw\Chapter_14-7.txt", "Chapter 14-7 CABLE TELEVISION FRANCHISE")
process_file(r"C:\Ordinance\data\raw\Chapter_14-8.txt", "Chapter 14-8 TELEPHONE  FRANCHISE")
process_file(r"C:\Ordinance\data\raw\Chapter_14-9.txt", "Chapter 14-9 ELECTRICITY  FRANCHISE")
process_file(r"C:\Ordinance\data\raw\Chapter_14-10.txt", "Chapter 14-10 STREET LIGHTING SERVICE")
process_file(r"C:\Ordinance\data\raw\Chapter_14-11.txt", "Chapter 14-11 REGULATING SMALL CELL FACILITIES")
process_file(r"C:\Ordinance\data\raw\Chapter_14-12.txt", "Chapter 14-12 STORMWATER UTILITY FEE")
process_file(r"C:\Ordinance\data\raw\Chapter_14-41.txt", "Chapter 14-41 REGULATION OF SEWER USE")
process_file(r"C:\Ordinance\data\raw\Chapter_16-1.txt", "Chapter 16-1 2013 REVISED SUBDIVISION ORDINANCE FOR THE CITY OF BRANDON")
process_file(r"C:\Ordinance\data\raw\Chapter_16-2.txt", "Chapter 16-2 SUBDIVISION PLANS APPROVAL PROCESS")
process_file(r"C:\Ordinance\data\raw\Chapter_16-3.txt", "Chapter 16-3 CONCEPT PLAN")
process_file(r"C:\Ordinance\data\raw\Chapter_16-4.txt", "Chapter 16-4 PRELIMINARY SUBDIVISION PLAN")
process_file(r"C:\Ordinance\data\raw\Chapter_16-5.txt", "Chapter 16-5 DEVELOPMENT ENGINEERING PLANS AND THE PLAT")
process_file(r"C:\Ordinance\data\raw\Chapter_16-6.txt", "Chapter 16-6 PRELIMINARY PLAN CRITERIA")
process_file(r"C:\Ordinance\data\raw\Chapter_16-7.txt", "Chapter 16-7 DEVELOPMENT ENGINEERING PLAN CRITERIA")
process_file(r"C:\Ordinance\data\raw\Chapter_16-8.txt", "Chapter 16-8 UTILITIES AND PUBLIC SPACE")
process_file(r"C:\Ordinance\data\raw\Chapter_16-9.txt", "Chapter 16-9 GRADING AND DRAINAGE")
process_file(r"C:\Ordinance\data\raw\Chapter_16-10.txt", "Chapter 16-10 EROSION CONTROL PLAN")
process_file(r"C:\Ordinance\data\raw\Chapter_16-11.txt", "Chapter 16-11 PRESERVATION OF NATURAL FEATURES AND AMENITIES")
process_file(r"C:\Ordinance\data\raw\Chapter_16-12.txt", "Chapter 16-12 RURAL SUBDIVISIONS")
process_file(r"C:\Ordinance\data\raw\Chapter_16-13.txt", "Chapter 16-13 ASSURANCES FOR THE COMPLETION OF MINIMUM")
process_file(r"C:\Ordinance\data\raw\Chapter_16-14.txt", "Chapter 16-14 CERTIFICATES REQUIRED")
process_file(r"C:\Ordinance\data\raw\Chapter_16-15.txt", "Chapter 16-15 CONSTRUCTION OF IMPROVEMENTS AND ACCEPTANCE")
process_file(r"C:\Ordinance\data\raw\Chapter_16-16.txt", "Chapter 16-16 EASEMENTS")
process_file(r"C:\Ordinance\data\raw\Chapter_17-1.txt", "Chapter 17-1 MEDICAL CANNABIS")
process_file(r"C:\Ordinance\data\raw\Flood_Plain_Ordinance_-_Appendix_A.txt", "FLOOD PLAIN ORDINANCE APPENDIX A")
process_file(r"C:\Ordinance\data\raw\Zoning_Ordinances_-_Effective_05-21-2025.txt", "ZONING ORDINANCES EFFECTIVE MAY 21 2025")