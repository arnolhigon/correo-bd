

import xml.etree.ElementTree as ET

def leer_xml(ruta):

    tree = ET.parse(ruta)
    root = tree.getroot()

    for child in root:
        print(f"Etiqueta: {child.tag}, Atributos: {child.attrib}, Contenido: {child.text}")

archivo_xml = "C:\\Users\\ADM_ANARVAEZ\\Downloads\\efw\\archivo\\a.xml"
leer_xml(archivo_xml)
