# 🔷 QR Master Pro — Edición Jeferson Jaimes

<p align="center">
  <img alt="banner" src="https://via.placeholder.com/1200x320/0f1724/00b4d8?text=QR+Master+Pro+-+Diseña+QRs+Profesionales" style="border-radius:12px; box-shadow: 0 8px 24px rgba(2,6,23,0.6)"/>
</p>

<p align="center">
  <a href="https://github.com/JAIMES4224D/QR-Master-Pro/blob/main/LICENSE"><img alt="license" src="https://img.shields.io/github/license/JAIMES4224D/QR-Master-Pro?style=for-the-badge&color=blue"></a>
  <a href="https://www.python.org/"><img alt="python" src="https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python"></a>
  <a href="https://github.com/JAIMES4224D"><img alt="author" src="https://img.shields.io/badge/Dev-Jeferson%20Jaimes-ff0066?style=for-the-badge"></a>
  <img alt="status" src="https://img.shields.io/badge/Status-Local%20App-lightgrey?style=for-the-badge" />
</p>

<p align="center">
  <strong style="font-size:1.05rem;">Generador de códigos QR elegante, personalizable y con vista previa en tiempo real — pensado para diseñadores, marcas y desarrolladores.</strong>
</p>

---

Índice
- Demo Rápido
- Características
- Instalación
- Uso Rápido
- Personalización (colores y logos)
- Exportación / Impresión
- Galería
- Contribuir
- Licencia & Contacto

---

## ✨ Demo rápido

> Interfaz moderna con modo oscuro, selector HEX y vista previa en vivo.

<p align="center">
  <!-- Reemplazar con GIF real cuando esté disponible -->
  <img alt="preview" src="https://via.placeholder.com/900x420/071133/00b4d8?text=Preview+-+QR+Master+Pro" style="border-radius:10px; box-shadow: 0 10px 30px rgba(2,6,23,0.6)"/>
</p>

---

## 🚀 Características principales

- Diseño contemporáneo con Dark Mode y controles intuitivos.
- Vista previa en tiempo real: ves el QR mientras editas.
- Selector de color HEX para módulos y fondo.
- Exportación PNG en alta resolución (configurable).
- Control de tamaño, margen, y nivel de corrección de errores (L/M/Q/H).
- Inserción de logo/imagen central (con ajuste de área segura).
- Plantillas y presets para usos rápidos (Corporate, Poster, Minimal).
- Código base en Python con dependencia mínima (qrcode + Pillow).

---

## 🔧 Instalación (rápida)

Requisitos:
- Python 3.8+

Clona y entra en el repo:
```bash
git clone https://github.com/JAIMES4224D/qr-master-pro.git
cd qr-master-pro
```

Instala dependencias:
```bash
pip install -r requirements.txt
# ó
pip install qrcode[pil] pillow
```

Lanza la aplicación:
```bash
python QR_Master_Pro_Design.py
```
(La app abrirá una ventana GUI si está implementada con tkinter/Qt; si es CLI, mostrará opciones.)

---

## ⚙️ Uso rápido (ejemplos)

Generar desde la UI:
1. Ingresa texto/URL/vCard.
2. Ajusta colores, tamaño y nivel de corrección.
3. Visualiza y exporta.

Uso CLI (ejemplo conceptual — adaptar a parámetros reales):
```bash
python QR_Master_Pro_Design.py \
  --text "https://example.com" \
  --size 1200 \
  --bg "#0f1724" \
  --color "#00b4d8" \
  --margin 8 \
  --error H \
  --output "mi_qr_hd.png"
```

---

## 🎨 Personalización rápida

Paleta recomendada (copiar HEX):
<p align="center">
  <img alt="#0f1724" src="https://img.shields.io/badge/%20-#0f1724-0f1724?style=for-the-badge&logoColor=white" />
  <img alt="#00b4d8" src="https://img.shields.io/badge/%20-#00b4d8-00b4d8?style=for-the-badge&logoColor=white" />
  <img alt="#2b6cb0" src="https://img.shields.io/badge/%20-#2b6cb0-2b6cb0?style=for-the-badge&logoColor=white" />
  <img alt="#ffffff" src="https://img.shields.io/badge/%20-#ffffff-white?style=for-the-badge&logoColor=black" />
</p>

Consejos:
- Para logos centrales usa un área ≤ 20% del total y sube el nivel de corrección a H.
- Para impresión, exporta > 3000 px y revisa sangrado/márgenes.
- Para contraste accesible, verifica relación de contraste entre puntos y fondo.

---

## 🖼️ Galería (placeholders — reemplaza por capturas reales)

<p align="center">
  <img alt="gallery1" src="https://via.placeholder.com/280x280/001630/00b4d8?text=QR+1" style="margin:8px; border-radius:8px;">
  <img alt="gallery2" src="https://via.placeholder.com/280x280/071133/ffd166?text=QR+2" style="margin:8px; border-radius:8px;">
  <img alt="gallery3" src="https://via.placeholder.com/280x280/0f1724/00ffb3?text=QR+3" style="margin:8px; border-radius:8px;">
</p>

---

## 📦 Exportación & Calidad de impresión

- Formato recomendado: PNG para web y pruebas; SVG/PDF ideal para impresión (si se implementa).
- DPI sugerido: 300 DPI para impresiones de alta calidad.
- Margen: usa margen ≥ 4 para mejor lectura en scanners.

---

## 🤝 Contribuir

¿Quieres ayudar? ¡Gracias!
1. Haz fork del repo.
2. Crea una rama: feature/tu-idea.
3. Añade cambios y tests (si procede).
4. Abre un Pull Request describiendo los cambios y una captura o GIF.

Ideas de mejora
- Exportación SVG/PDF
- Presets temáticos y paletas accesibles
- Batch generation (API / CLI)
- Interfaz web

---

## ❓ Preguntas frecuentes

P: ¿Puedo incrustar un logo grande?
R: Sí, pero aumenta corrección de error a H y limita el tamaño del logo para no romper el escaneo.

P: ¿Soporta vCard?
R: Sí. Construye la cadena vCard estándar y pásala como texto.

P: ¿Se puede automatizar?
R: Sí — se puede añadir soporte CLI o API para generación masiva.

---

## ⚖️ Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

---

## ✉️ Contacto

Jeferson Jociney Jaimes Passuni — GitHub: [@JAIMES4224D](https://github.com/JAIMES4224D)  
Hecho con ❤️ y diseño cuidado.
