from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter # Importamos el tamaño de la página (carta)
from reportlab.lib.units import inch # Importamos la unidad de pulgada para mejor posicionamiento

def generar_pdf_informe():
    """Genera un documento PDF simple usando ReportLab."""
    
    # 1. Crear el Objeto Canvas (el "lienzo" del PDF)
    # Especificamos el nombre del archivo de salida
    nombre_archivo = "Informe_Mensual.pdf"
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    
    # --- Configuración del Texto y Posicionamiento ---
    
    # Definimos la posición inicial (X, Y) desde la esquina inferior izquierda
    # La coordenada Y se reduce al movernos hacia abajo en la página
    
    # 2. Título Principal
    c.setFont("Helvetica-Bold", 18) # Establece la fuente y el tamaño
    # Posiciona y dibuja el texto (2 pulgadas desde la izquierda, 10 pulgadas desde abajo)
    c.drawString(2 * inch, 10 * inch, "INFORME AUTOMATIZADO DE PYTHON")
    
    # 3. Línea de Separación
    # Dibuja una línea horizontal
    c.setLineWidth(1) # Grosor de la línea
    c.line(1 * inch, 9.7 * inch, 7.5 * inch, 9.7 * inch)
    
    # 4. Texto de Contenido
    c.setFont("Helvetica", 12)
    # Posiciona el texto del cuerpo un poco más abajo
    y_position = 9.2 * inch
    
    c.drawString(1 * inch, y_position, "Este documento fue generado automáticamente usando la librería ReportLab.")
    y_position -= 0.5 * inch # Baja la posición Y para el siguiente párrafo
    
    c.drawString(1 * inch, y_position, "Objetivo del Ejercicio:")
    y_position -= 0.3 * inch
    
    # 5. Lista con Viñetas (simulada)
    c.drawString(1.5 * inch, y_position, "- Demostrar la instalación de dependencias en un entorno virtual.")
    y_position -= 0.25 * inch
    c.drawString(1.5 * inch, y_position, "- Extender las capacidades de Python para generar archivos especializados (PDF).")
    y_position -= 0.25 * inch
    c.drawString(1.5 * inch, y_position, "- Practicar la llamada de métodos de una librería de terceros.")

    # 6. Número de Página (Ejemplo)
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(7.5 * inch, 0.5 * inch, "Página 1")
    
    # 7. Guardar el PDF (¡El paso final!)
    c.save()
    print(f"✅ ¡Informe PDF generado exitosamente! Archivo: {nombre_archivo}")

# Llamar a la función para ejecutar la generación
if __name__ == "__main__":
    generar_pdf_informe()