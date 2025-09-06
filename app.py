# PDF → Text Extractor using Docling
# Author: Bathini Rohini

from docling.document_converter import DocumentConverter

def extract_text(pdf_file, output_file="output.txt"):
    converter = DocumentConverter()
    doc = converter.convert(pdf_file)
    text = doc.export_to_text()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Extracted text saved to {output_file}")

if __name__ == "__main__":
    # Change 'sample.pdf' to your PDF filename
    extract_text("sample.pdf")
