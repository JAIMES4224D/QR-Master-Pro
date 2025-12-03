# 🔷 QR Master Pro — Edición Jeferson Jaimes

<p align="center">
  <img alt="banner" src="https://via.placeholder.com/1200x320/0f1724/00b4d8?text=QR+Master+Pro+-+Diseña+QRs+Profesionales" style="border-radius:12px; box-shadow:0 8px 24px rgba(2,6,23,0.6)" />
</p>

<p align="center">
  <a href="https://github.com/JAIMES4224D/QR-Master-Pro/blob/main/LICENSE"><img alt="license" src="https://img.shields.io/github/license/JAIMES4224D/QR-Master-Pro?style=for-the-badge&color=blue"></a>
  <a href="https://www.python.org/"><img alt="python" src="https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python"></a>
  <a href="https://github.com/JAIMES4224D"><img alt="author" src="https://img.shields.io/badge/Dev-Jeferson%20Jaimes-ff0066?style=for-the-badge"></a>
  <a href="https://github.com/JAIMES4224D/QR-Master-Pro/stargazers"><img alt="stars" src="https://img.shields.io/github/stars/JAIMES4224D/QR-Master-Pro?style=for-the-badge&color=yellow"></a>
</p>

<p align="center"><strong>Generador de códigos QR elegante, personalizable y con vista previa en tiempo real.</strong></p>

---

<p align="center">
  <strong>Contenido</strong> • <a href="#demo">Demo</a> • <a href="#caracteristicas">Características</a> • <a href="#instalacion">Instalación</a> • <a href="#uso">Uso</a> • <a href="#contribuir">Contribuir</a> • <a href="#contacto">Contacto</a>
</p>

---

## ✨ Demo
<p align="center">
  <img alt="preview" src="https://via.placeholder.com/900x420/071133/00b4d8?text=Preview+-+QR+Master+Pro" style="border-radius:10px; box-shadow:0 10px 30px rgba(2,6,23,0.6)" />
</p>

---

## 🚀 Características principales
<p align="center">Generación de QR (URL, texto, vCard, Wi‑Fi) • Vista previa en vivo • Personalización de colores y logo • Exportación PNG en alta resolución</p>

- Compatibilidad: Windows, macOS, Linux
- Control de tamaño: 100–3000 px
- Margen configurable y niveles de corrección (L/M/Q/H)
- Inserción de logo con ajuste automático y recomendaciones de contraste

---

## 🔧 Instalación rápida

Clona el repo y crea un entorno:

```bash
git clone https://github.com/JAIMES4224D/QR-Master-Pro.git
cd QR-Master-Pro
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
```

Instalación rápida alternativa:

```bash
pip install qrcode[pil] pillow tkinterdnd2
```

Ejecuta la app:

```bash
python QR_Master_Pro_Design.py
```

---

## ⚡ Uso rápido (CLI)

```bash
python QR_Master_Pro_Design.py --text "https://github.com/JAIMES4224D" --output mi_qr.png
```

Parámetros clave: --text, --size, --background, --foreground, --margin, --error-correction, --logo, --logo-size, --dpi, --output.

---

## 🎨 Consejos de diseño (resumen)

- Mantén contraste alto entre módulos y fondo (mínimo 4.5:1).
- Logo ≤ 20% del área total; usar corrección H si hay logo.
- Prueba en múltiples lectores y escala de grises antes de imprimir.
- Margen recomendado para impresión: ≥ 12 px.

---

## 🤝 Contribuir

1. Fork → crear rama feature → PR.
2. Mensajes de commit claros.
3. Sigue el formato de issues y PRs del repo.

---

## ⚖️ Licencia

MIT — ver <https://github.com/JAIMES4224D/QR-Master-Pro/blob/main/LICENSE>

---

## ✉️ Contacto

<p align="center">
  Jeferson Jociney Jaimes Passuni — <a href="https://github.com/JAIMES4224D">@JAIMES4224D</a>
</p>

<p align="center"><em>Hecho con ❤️ — Si te gusta el proyecto, deja una ⭐</em></p>
