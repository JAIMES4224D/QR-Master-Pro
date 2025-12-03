import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.colorchooser import askcolor  # Nueva importación necesaria
import qrcode
from PIL import ImageTk, Image, ImageDraw
import os
from datetime import datetime

# --- CLASE PARA BOTONES MODERNOS CON HOVER ---
class ModernButton(tk.Button):
    def __init__(self, master, **kwargs):
        self.default_bg = kwargs.get('bg', '#3B82F6')
        self.hover_bg = kwargs.get('activebackground', '#2563EB')
        self.text_color = kwargs.get('fg', 'white')
        
        # Eliminamos bordes estándar
        kwargs['relief'] = tk.FLAT
        kwargs['borderwidth'] = 0
        kwargs['cursor'] = 'hand2'
        
        super().__init__(master, **kwargs)
        
        # Bindings para efectos hover
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['bg'] = self.hover_bg

    def on_leave(self, e):
        self['bg'] = self.default_bg

# --- APP PRINCIPAL ---
class QRGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Master Pro v4.0 - Jeferson Jaimes Edition")
        self.root.geometry("1050x750")
        self.root.configure(bg="#0F172A") # Fondo Slate Dark
        
        # Configurar redimensionamiento
        self.root.resizable(False, False)
        
        # --- PALETA DE COLORES PREMIUM ---
        self.colors = {
            "bg_main": "#0F172A",      # Fondo principal muy oscuro
            "bg_card": "#1E293B",      # Fondo de tarjetas (Slate-800)
            "primary": "#3B82F6",      # Azul brillante (Blue-500)
            "primary_dark": "#1D4ED8", # Azul oscuro para hover
            "accent": "#10B981",       # Verde esmeralda
            "accent_dark": "#059669",  # Verde oscuro
            "text_main": "#F8FAFC",    # Blanco casi puro
            "text_dim": "#94A3B8",     # Gris claro para subtítulos
            "input_bg": "#334155",     # Fondo de inputs
            "border": "#475569"        # Bordes sutiles
        }
        
        # Fuentes Modernas
        self.fonts = {
            "h1": ("Segoe UI", 28, "bold"),
            "h2": ("Segoe UI", 16, "bold"),
            "body": ("Segoe UI", 11),
            "small": ("Segoe UI", 9),
            "button": ("Segoe UI", 12, "bold")
        }
        
        # Variables de estado
        self.qr_image = None
        self.qr_img_pil = None
        self.selected_qr_color = "#000000"
        self.selected_bg_color = "#FFFFFF"
        
        # Listas de indicadores (para poder actualizarlos luego)
        self.qr_color_indicators = []
        self.bg_color_indicators = []
        
        # Inicializar UI
        self.setup_ui()
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def setup_ui(self):
        # 1. HEADER (ENCABEZADO)
        header_frame = tk.Frame(self.root, bg=self.colors["bg_main"], pady=20)
        header_frame.pack(fill=tk.X)
        
        tk.Label(header_frame, text="QR MASTER PRO", font=self.fonts["h1"], 
                 bg=self.colors["bg_main"], fg=self.colors["primary"]).pack()
        
        tk.Label(header_frame, text="Diseño Profesional & Generación Instantánea", 
                 font=self.fonts["body"], bg=self.colors["bg_main"], fg=self.colors["text_dim"]).pack()

        # 2. CONTENEDOR PRINCIPAL (GRID LAYOUT)
        main_content = tk.Frame(self.root, bg=self.colors["bg_main"])
        main_content.pack(fill=tk.BOTH, expand=True, padx=40, pady=10)
        
        # --- COLUMNA IZQUIERDA (CONTROLES) ---
        left_col = tk.Frame(main_content, bg=self.colors["bg_main"])
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))
        
        # TARJETA 1: DATOS
        self.create_card_data(left_col)
        
        # ESPACIO
        tk.Frame(left_col, height=20, bg=self.colors["bg_main"]).pack()
        
        # TARJETA 2: PERSONALIZACIÓN
        self.create_card_style(left_col)
        
        # --- COLUMNA DERECHA (PREVIEW) ---
        right_col = tk.Frame(main_content, bg=self.colors["bg_main"])
        right_col.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.create_card_preview(right_col)
        
        # 3. BARRA DE ESTADO Y MARCA (FOOTER)
        footer_frame = tk.Frame(self.root, bg=self.colors["bg_card"])
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Estado a la izquierda
        self.status_bar = tk.Label(footer_frame, text="🚀 Listo para crear", 
                                  font=self.fonts["small"], bg=self.colors["bg_card"], 
                                  fg=self.colors["accent"], pady=10)
        self.status_bar.pack(side=tk.LEFT, padx=20)
        
        # Marca del desarrollador a la derecha
        developer_label = tk.Label(footer_frame, 
                                 text="Desarrollado por: Jeferson Jociney Jaimes Passuni", 
                                 font=("Segoe UI", 9, "italic"), 
                                 bg=self.colors["bg_card"], 
                                 fg=self.colors["text_dim"], 
                                 pady=10)
        developer_label.pack(side=tk.RIGHT, padx=20)

    def create_card_data(self, parent):
        card = tk.Frame(parent, bg=self.colors["bg_card"], padx=25, pady=25)
        card.pack(fill=tk.X)
        
        header = tk.Frame(card, bg=self.colors["bg_card"])
        header.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(header, text="📝 Contenido del QR", font=self.fonts["h2"], 
                 bg=self.colors["bg_card"], fg=self.colors["text_main"]).pack(side=tk.LEFT)
        
        tk.Label(card, text="Introduce URL o Texto:", font=self.fonts["body"], 
                 bg=self.colors["bg_card"], fg=self.colors["text_dim"]).pack(anchor="w", pady=(10, 5))
        
        input_container = tk.Frame(card, bg=self.colors["input_bg"], padx=10, pady=8)
        input_container.pack(fill=tk.X)
        
        self.entry = tk.Entry(input_container, font=("Segoe UI", 12), 
                              bg=self.colors["input_bg"], fg="white", 
                              insertbackground="white", relief=tk.FLAT)
        self.entry.pack(fill=tk.X)
        self.entry.bind("<Return>", lambda e: self.generate_qr())
        
        link_btn = tk.Label(card, text="📋 Usar ejemplo: Github Profile", 
                           font=self.fonts["small"], bg=self.colors["bg_card"], 
                           fg=self.colors["primary"], cursor="hand2")
        link_btn.pack(anchor="w", pady=10)
        link_btn.bind("<Button-1>", lambda e: self.set_example("https://github.com/JAIMES4224D"))

    def create_card_style(self, parent):
        card = tk.Frame(parent, bg=self.colors["bg_card"], padx=25, pady=25)
        card.pack(fill=tk.X)
        
        tk.Label(card, text="🎨 Personalización", font=self.fonts["h2"], 
                 bg=self.colors["bg_card"], fg=self.colors["text_main"]).pack(anchor="w", pady=(0, 15))
        
        # --- SELECCION DE COLOR QR ---
        tk.Label(card, text="Color de Puntos:", font=self.fonts["body"], 
                 bg=self.colors["bg_card"], fg=self.colors["text_dim"]).pack(anchor="w")
        
        colors_frame = tk.Frame(card, bg=self.colors["bg_card"])
        colors_frame.pack(anchor="w", pady=(5, 15))
        
        qr_colors = [
            ("#000000", "Negro"), 
            ("#3B82F6", "Azul"), 
            ("#EF4444", "Rojo"), 
            ("#10B981", "Verde"),
            ("#8B5CF6", "Violeta"),
            ("CUSTOM", "Personalizado") # Opción especial
        ]
        
        for color_code, name in qr_colors:
            self.create_color_circle(colors_frame, color_code, "fg")

        # --- SELECCION DE COLOR FONDO ---
        tk.Label(card, text="Color de Fondo:", font=self.fonts["body"], 
                 bg=self.colors["bg_card"], fg=self.colors["text_dim"]).pack(anchor="w")
        
        bg_frame = tk.Frame(card, bg=self.colors["bg_card"])
        bg_frame.pack(anchor="w", pady=5)
        
        bg_colors = [
            ("#FFFFFF", "Blanco"), 
            ("#F1F5F9", "Gris"), 
            ("#FEF3C7", "Crema"),
            ("CUSTOM", "Personalizado") # Opción especial
        ]
        
        for color_code, name in bg_colors:
            self.create_color_circle(bg_frame, color_code, "bg")

    def create_color_circle(self, parent, color, type_selection):
        """Crea un círculo de color seleccionable"""
        canvas = tk.Canvas(parent, width=35, height=35, bg=self.colors["bg_card"], 
                           highlightthickness=0, cursor="hand2")
        canvas.pack(side=tk.LEFT, padx=5)
        
        fill_color = color
        is_custom = False
        
        # Si es el botón de "Custom", lo dibujamos diferente
        if color == "CUSTOM":
            is_custom = True
            fill_color = "#334155" # Color gris oscuro inicial para el botón
            
        oval = canvas.create_oval(5, 5, 30, 30, fill=fill_color, outline=self.colors["border"], width=1)
        
        # Si es custom, dibujamos un "+"
        if is_custom:
            canvas.create_text(17.5, 17.5, text="+", fill="white", font=("Arial", 14, "bold"))

        # Diccionario para guardar referencia de este indicador
        indicator = {
            'canvas': canvas, 
            'oval': oval, 
            'color': color, 
            'type': type_selection,
            'is_custom': is_custom
        }
        
        if type_selection == "fg":
            self.qr_color_indicators.append(indicator)
            # Selección por defecto (Negro)
            if color == "#000000": 
                canvas.itemconfig(oval, outline="white", width=3)
        else:
            self.bg_color_indicators.append(indicator)
            # Selección por defecto (Blanco)
            if color == "#FFFFFF":
                canvas.itemconfig(oval, outline=self.colors["primary"], width=3)

        # Usamos una función lambda para pasar el indicador exacto al hacer click
        canvas.bind("<Button-1>", lambda e, ind=indicator: self.handle_color_click(ind))

    def handle_color_click(self, indicator):
        """Maneja el click en un color (predefinido o custom)"""
        
        final_color = indicator['color']
        
        # Si es el botón Custom, abrir el selector
        if indicator['is_custom']:
            color_code = askcolor(title="Selecciona un color")[1] # [1] devuelve el Hex
            if not color_code: 
                return # Si cancela, no hacemos nada
            
            final_color = color_code
            # Actualizamos el color del círculo custom para mostrar lo que eligió
            indicator['canvas'].itemconfig(indicator['oval'], fill=final_color)
            
        # Actualizar lógica de selección y bordes
        self.update_selection_visuals(indicator, final_color)

    def update_selection_visuals(self, active_indicator, color_code):
        """Actualiza las variables y los bordes visuales"""
        type_selection = active_indicator['type']
        target_list = self.qr_color_indicators if type_selection == "fg" else self.bg_color_indicators
        
        # 1. Actualizar variable de estado
        if type_selection == "fg":
            self.selected_qr_color = color_code
        else:
            self.selected_bg_color = color_code

        # 2. Actualizar visuales (borde brillante solo para el seleccionado)
        for item in target_list:
            width = 1
            outline = self.colors["border"]
            
            # Comparamos identidad del objeto (is) para saber cuál es el activo
            if item is active_indicator:
                width = 3
                # Borde blanco para FG, Azul para BG
                outline = "white" if type_selection == "fg" else self.colors["primary"]
            
            item['canvas'].itemconfig(item['oval'], width=width, outline=outline)

        # 3. Regenerar QR si hay texto
        if self.entry.get():
            self.generate_qr()

    def create_card_preview(self, parent):
        card = tk.Frame(parent, bg=self.colors["bg_card"], padx=25, pady=25)
        card.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(card, text="👁️ Vista Previa", font=self.fonts["h2"], 
                 bg=self.colors["bg_card"], fg=self.colors["text_main"]).pack(pady=(0, 20))
        
        self.preview_frame = tk.Frame(card, bg="#000000", width=320, height=320)
        self.preview_frame.pack_propagate(False) 
        self.preview_frame.pack(expand=True)
        
        self.image_label = tk.Label(self.preview_frame, text="El QR aparecerá aquí", 
                                   font=self.fonts["body"], bg=self.colors["input_bg"], 
                                   fg=self.colors["text_dim"])
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        btn_frame = tk.Frame(card, bg=self.colors["bg_card"])
        btn_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.btn_gen = ModernButton(btn_frame, text="GENERAR CÓDIGO", 
                                   bg=self.colors["primary"], activebackground=self.colors["primary_dark"],
                                   fg="white", font=self.fonts["button"], width=15, height=2,
                                   command=self.generate_qr)
        self.btn_gen.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.btn_save = ModernButton(btn_frame, text="GUARDAR PNG", 
                                    bg=self.colors["accent"], activebackground=self.colors["accent_dark"],
                                    fg="white", font=self.fonts["button"], width=15, height=2,
                                    command=self.save_qr)
        self.btn_save.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))

    def set_example(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)
        self.generate_qr()

    def generate_qr(self):
        data = self.entry.get().strip()
        if not data:
            self.status_bar.config(text="⚠️ Escribe algo para generar el QR", fg="#F59E0B")
            return

        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=2)
            qr.add_data(data)
            qr.make(fit=True)

            self.qr_img_pil = qr.make_image(fill_color=self.selected_qr_color, 
                                            back_color=self.selected_bg_color).convert('RGB')
            
            preview_size = 300
            display_img = self.qr_img_pil.resize((preview_size, preview_size), Image.Resampling.LANCZOS)
            self.qr_image = ImageTk.PhotoImage(display_img)

            self.image_label.config(image=self.qr_image, text="", bg=self.selected_bg_color)
            self.preview_frame.config(bg="white") 
            
            self.status_bar.config(text=f"✅ QR Generado con éxito ({len(data)} caracteres)", fg=self.colors["accent"])

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_qr(self):
        if not self.qr_img_pil:
            messagebox.showwarning("Aviso", "Primero genera un QR.")
            return

        filename = f"QR_{datetime.now().strftime('%H%M%S')}.png"
        file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                 initialfile=filename,
                                                 filetypes=[("PNG", "*.png"), ("JPG", "*.jpg")])
        
        if file_path:
            try:
                self.qr_img_pil.save(file_path)
                messagebox.showinfo("Éxito", f"QR Guardado en:\n{file_path}")
                self.status_bar.config(text="💾 Archivo guardado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRGeneratorApp(root)
    root.mainloop()