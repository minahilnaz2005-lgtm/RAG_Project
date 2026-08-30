from pathlib import Path

from pypdf import PdfReader

from config import DOCUMENTS_DIR


def load_documents():
    """
    Documents folder mein maujood PDF files ko read karta hai.
    """

    documents = []

    pdf_files = list(DOCUMENTS_DIR.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in: {DOCUMENTS_DIR}"
        )

    for pdf_path in pdf_files:

        reader = PdfReader(pdf_path)

        for page_number, page in enumerate(reader.pages, start=1):

            text = page.extract_text()

            if text and text.strip():

                documents.append(
                    {
                        "text": text.strip(),
                        "source": pdf_path.name,
                        "page": page_number
                    }
                )

    print(f"Loaded {len(documents)} document pages.")

    return documents