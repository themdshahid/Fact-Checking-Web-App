from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    text = ""

    reader = PdfReader(pdf_file)

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text