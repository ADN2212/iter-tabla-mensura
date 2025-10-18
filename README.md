# Iter Tabla Mensura

**Iter Tabla Mensura** es una herramienta desarrollada en **Python** para automatizar la creación de los **cuadros de construcción** de los **planos catastrales** que se depositan en la **Dirección Regional de Mensuras Catastrales** de la **República Dominicana**.  

El programa procesa uno o varios archivos de texto que pueden estar en dos formatos diferentes, explicados en el siguiente video: [Ver video explicativo](https://drive.google.com/file/d/1UHX0GLR2fYpuX8lM41lo6qtbUNeyMCJi/view?usp=drive_link)

---

## Tecnologías utilizadas

El proyecto está desarrollado completamente en **Python**, utilizando principalmente las siguientes librerías (además de la biblioteca estándar):

- **ttkthemes** → para aplicar estilos visuales a las interfaces gráficas basadas en `tkinter`.  
- **openpyxl** → para generar archivos de **Excel** donde se guardan los cuadros de construcción.

---

## Cómo usarlo

1. **Instalar Python**  
   Asegúrate de tener Python instalado en tu sistema operativo. [Descargar Python](https://www.python.org/downloads/)

2. **Crear un entorno virtual**  
   Se recomienda crear un entorno virtual dentro de una carpeta del proyecto. [Guía para crear entornos virtuales en Python](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

3. **Instalar dependencias**  
   Una vez activado el entorno virtual, instala las dependencias necesarias (por ejemplo, con `pip install -r requirements.txt` si el archivo está disponible).

4. **Ejecutar el programa**  
   Abre una terminal (CMD o PowerShell en Windows, o una consola SSH en Linux/Mac) dentro de la carpeta del proyecto y ejecuta:

   ```bash
    python main.py
    ```
5.  **Crear un ejecutable**

Si deseas generar un ejecutable (.exe) del programa para distribuirlo sin necesidad de instalar Python, puedes seguir este tutorial: [Cómo crear ejecutables en Python](https://www.youtube.com/watch?v=sBbWjG8ghtg)

