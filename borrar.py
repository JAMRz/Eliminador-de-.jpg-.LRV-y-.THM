import os

# Carpeta donde está el script
carpeta = os.path.dirname(os.path.abspath(__file__))

# Extensiones a borrar
extensiones = (".jpg", ".lrv", ".thm")

# Buscar archivos
archivos = [
    f for f in os.listdir(carpeta)
    if f.lower().endswith(extensiones)
]

if not archivos:
    print("No hay archivos JPG, LRV o THM en esta carpeta")
    input("ENTER para salir")
    exit()

print("Archivos eliminados:")
for f in archivos:
    os.remove(os.path.join(carpeta, f))
    print(" -", f)

print(f"\nTotal eliminados: {len(archivos)}")
input("ENTER para salir")
