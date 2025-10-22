# Generador de Informe PDF

Proyecto sencillo que genera un informe en formato PDF usando la librería ReportLab.

Este repositorio contiene un script Python (`generar_informe.py`) que crea un archivo llamado `Informe_Mensual.pdf` y demuestra el uso básico de ReportLab para dibujar texto, líneas y controlar posiciones en la página.

## Contenido

- `generar_informe.py` — Script principal que genera el PDF.
- `requirements.txt` — Dependencias necesarias para ejecutar el script.

## Requisitos

- Python 3.8 o superior (se recomienda la última versión estable).
- Paquetes Python listados en `requirements.txt`:
  - `reportlab==4.4.4`
  - `pillow==12.0.0`
  - `charset-normalizer==3.4.4`

Es recomendable usar un entorno virtual para instalar las dependencias.

## Instalación (Windows PowerShell)

1. Abrir PowerShell en la carpeta del proyecto (donde está `generar_informe.py`).
2. Crear y activar un entorno virtual:

```powershell
python -m venv .\venv
# Si la política de ejecución impide activar el script, permita temporalmente la ejecución solo para la sesión:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
.\venv\Scripts\Activate.ps1
```

3. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

Nota: si usa CMD en lugar de PowerShell, active el entorno virtual con:

```cmd
.\venv\Scripts\activate
```

## Uso

Ejecutar el script para generar el PDF:

```powershell
python generar_informe.py
```

Salida: se creará el archivo `Informe_Mensual.pdf` en la misma carpeta. El script imprime un mensaje de éxito cuando finaliza.

## Explicación del script `generar_informe.py`

Resumen de las secciones principales:

- Importaciones:
  - `reportlab.pdfgen.canvas` — objeto `Canvas` para dibujar en el PDF.
  - `reportlab.lib.pagesizes.letter` — tamaño de página (carta).
  - `reportlab.lib.units.inch` — unidad para posicionamiento con pulgadas.

- `generar_pdf_informe()`:
  - Crea un `Canvas` con nombre de salida `Informe_Mensual.pdf`.
  - Establece fuente y dibuja un título en la parte superior.
  - Dibuja una línea de separación.
  - Añade párrafos y una lista de viñetas (simulada) moviendo la coordenada Y hacia abajo.
  - Añade un número de página en la parte inferior.
  - Llama a `c.save()` para escribir el archivo en disco.

- Ejecución directa: cuando el archivo se ejecuta como script (`if __name__ == "__main__":`), llama a `generar_pdf_informe()`.

Detalles técnicos útiles:

- Las coordenadas en ReportLab empiezan en la esquina inferior izquierda de la página.
- La variable `inch` facilita calcular posiciones (p. ej. `2 * inch`).

## Estructura de archivos

```
generar_informe.py        # Script para crear Informe_Mensual.pdf
requirements.txt          # Dependencias
README.md                 # Documentación (este archivo)
```

## Solución de problemas comunes

- Error: ModuleNotFoundError: No module named 'reportlab'
  - Causa: no se instalaron las dependencias o no está activado el entorno virtual.
  - Solución: activar el entorno virtual y ejecutar `pip install -r requirements.txt`.

- PowerShell rechaza la ejecución de `Activate.ps1` por políticas de ejecución
  - Solución temporal: ejecutar `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force` antes de activar (se muestra arriba).

- Permisos o bloqueo por OneDrive
  - Si guarda el proyecto dentro de OneDrive y tiene sincronización activa, puede aparecer bloqueo de archivos. Copie el proyecto a una carpeta local sin sincronización o pause la sincronización.

- Problemas con fuentes o rendering en ReportLab
  - ReportLab usa las fuentes del sistema; si necesita fuentes embebidas o personalizadas, registre la fuente con `reportlab.pdfbase.ttfonts.TTFont` y `reportlab.pdfbase.pdfmetrics.registerFont`.

## Mejoras sugeridas (pequeñas ideas)

- Añadir argumentos de línea de comandos para personalizar el título, contenido y nombre de archivo (argparse).
- Permitir generar múltiples páginas y un contenido dinámico (tablas, gráficos, imágenes).
- Añadir pruebas unitarias que verifiquen la creación del archivo y su tamaño esperado.
- Añadir un archivo `LICENSE` si desea especificar una licencia de uso. (Sugerencia: MIT si quiere permitir uso libre con atribución).

## Contribuciones

Si quieres mejorar este script:

1. Haz un fork y crea una rama con tu mejora.
2. Añade pruebas o ejemplos de uso si cambias la interfaz.
3. Envía un pull request describiendo el cambio.

## Licencia

Este repositorio no incluye un archivo de licencia explícito. Si no indicas lo contrario, considera añadir un `LICENSE` (por ejemplo MIT) para dejar claras las condiciones de uso.

---

Si quieres, puedo:

- Añadir un `LICENSE` (por ejemplo MIT) automáticamente.
- Convertir el script para aceptar parámetros CLI (título, salida, lista de items).
- Añadir un pequeño test que verifique la generación del PDF.

Dime qué prefieres y lo implemento.
