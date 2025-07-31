#!/usr/bin/env python3
from pdf2image import convert_from_path
import os

# Páginas que contienen diagramas importantes
pages_with_diagrams = [7, 9, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44]

pdf_path = "/home/ubuntu/upload/OWASPAgentic-AI-Threats-and-Mitigations_v1.0a.pdf"
output_dir = "/home/ubuntu/owasp-agentic-ai-spanish/images"

# Crear directorio si no existe
os.makedirs(output_dir, exist_ok=True)

# Convertir páginas específicas a imágenes
for page_num in pages_with_diagrams:
    try:
        images = convert_from_path(pdf_path, first_page=page_num, last_page=page_num, dpi=200)
        if images:
            image_path = os.path.join(output_dir, f"page_{page_num:02d}.png")
            images[0].save(image_path, "PNG")
            print(f"Guardada página {page_num} como {image_path}")
    except Exception as e:
        print(f"Error procesando página {page_num}: {e}")

print("Extracción de imágenes completada")

