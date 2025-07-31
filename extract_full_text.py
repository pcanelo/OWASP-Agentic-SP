#!/usr/bin/env python3
import PyPDF2
import sys

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                text += f"\n--- PÁGINA {page_num + 1} ---\n"
                text += page_text
                text += "\n"
                
    except Exception as e:
        print(f"Error extrayendo texto: {e}")
        return None
    
    return text

if __name__ == "__main__":
    pdf_path = "/home/ubuntu/upload/OWASPAgentic-AI-Threats-and-Mitigations_v1.0a.pdf"
    output_path = "/home/ubuntu/owasp-agentic-ai-spanish/contenido_completo_original.txt"
    
    print("Extrayendo texto completo del PDF...")
    full_text = extract_text_from_pdf(pdf_path)
    
    if full_text:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"Texto extraído y guardado en: {output_path}")
    else:
        print("Error al extraer el texto del PDF")

