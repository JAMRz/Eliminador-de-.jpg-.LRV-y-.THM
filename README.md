# 🧹 Limpieza automática de archivos GoPro (JPG / LRV / THM)

Script en **Python** para eliminar rápidamente archivos innecesarios generados por cámaras **GoPro** u otros dispositivos que crean archivos auxiliares como `.LRV` y `.THM`.

El script elimina automáticamente **sin pedir confirmación** todos los archivos con las extensiones:

- `.jpg`
- `.lrv`
- `.thm`

📁 **Solo afecta la carpeta donde se encuentra `borrar.py`.**

---

## 🚀 ¿Para qué sirve?

Las cámaras GoPro generan archivos adicionales que muchas veces no se necesitan:

| Extensión | Uso                      |
| --------- | ------------------------ |
| `.JPG`    | Miniaturas               |
| `.LRV`    | Video de baja resolución |
| `.THM`    | Thumbnail                |

Este script permite **limpiar la carpeta en segundos**, ideal después de copiar los videos `.MP4`.

---

## 📦 Requisitos

- Python **3.8 o superior**
- Sistema operativo: **Windows / Linux / macOS**

---

## ▶️ Uso

1. Coloca el archivo **`borrar.py`** dentro de la carpeta que deseas limpiar.
2. Ejecuta el script:

```bash
python borrar.py
```
