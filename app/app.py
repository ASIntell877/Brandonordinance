import os
import json
import time
import faiss
import numpy as np
import streamlit as st
from openai import OpenAI
from openai.types.chat import ChatCompletion

# === Config ===
INDEX_PATH = r"C:\Ordinance\data\index\ordinance_index.faiss"
METADATA_PATH = r"C:\Ordinance\data\index\metadata.json"
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"  # or "gpt-3.5-turbo" if you prefer cheaper
MAX_CHUNKS = 5

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# === Load FAISS and metadata ===
index = faiss.read_index(INDEX_PATH)
with open(METADATA_PATH, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

# === Helper: Embed a query ===
def get_query_embedding(query):
    response = client.embeddings.create(
        input=[query],
        model=EMBEDDING_MODEL
    )
    return response.data[0].embedding

# === Helper: Search index ===
def search_index(query_embedding, k=MAX_CHUNKS):
    D, I = index.search(np.array([query_embedding]).astype("float32"), k)
    results = []
    for i in I[0]:
        if i < len(metadata):
            results.append(metadata[i])
    return results

# === Helper: Load chunk text from file ===
def get_chunk_text(meta):
    chunk_file = os.path.join(r"C:\Ordinance\data\chunks", meta["filename"])
    with open(chunk_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data[meta["chunk_id"]]["text"]

# === Prompt generation ===
def build_prompt(query, chunk_texts):
    joined_chunks = "\n\n".join(
        f"From *{meta['source']}*:\n\"{text}\"" for meta, text in chunk_texts
    )

    system_prompt = """
	Always answer based on the provided ordinance text. If you are unsure, say so clearly.

	Be polite, professional, and straightforward in tone.

	Use plain language when possible, especially for citizens unfamiliar with legal terms.

	When responding to city officials or during meetings, prioritize accuracy and direct citations (e.g., “Section 14-3-105”).

	If multiple sections may apply, mention them concisely.

	Your users may include:

	City officials needing precise, quick references during public meetings.

	Town residents asking questions about local laws, responsibilities, or procedures.
	"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"{query}\n\nRelevant texts:\n{joined_chunks}"}
    ]
    return messages

# === UI ===
st.set_page_config(page_title="Brandon Ordinance Oracle")
st.title("Brandon Ordinance Oracle")

query = st.text_input("How can I help?:")
submit = st.button("Answer.")

if submit and query:
    with st.spinner("Looking this up."):
        try:
            query_embedding = get_query_embedding(query)
            matches = search_index(query_embedding)
            
            # Check if we got any results from the search
            if not matches:
                st.warning("No relevant ordinance chunks found for your query. Please try rephrasing or ask about something else.")
            else:
                chunk_texts = [(meta, get_chunk_text(meta)) for meta in matches]
                messages = build_prompt(query, chunk_texts)

                response: ChatCompletion = client.chat.completions.create(
                    model=GPT_MODEL,
                    messages=messages,
                    temperature=0.7,
                    max_tokens=700
                )

                # Check if OpenAI returned choices
                if not response.choices or len(response.choices) == 0:
                    st.error("No response received from the language model. Please try again.")
                else:
                    st.markdown(response.choices[0].message.content)

                    st.markdown("""---
### ✨ **Disclaimer:** This chatbot provides information based on city ordinances but is **not a substitute for legal advice**.  
For legal concerns, please consult a qualified attorney or city official.
---""")

                    st.markdown("---")
                    st.markdown("##### 📚 Sources:")
                    for meta in matches:
                        st.markdown(f"- *{meta['source']}*, chunk #{meta['chunk_id']}")

        except Exception as e:
            st.error(f"Error: {e}")