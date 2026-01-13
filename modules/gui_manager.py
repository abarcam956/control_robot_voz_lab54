import tkinter as tk

def crear_ventana():
    """Crea la ventana principal y devuelve TODOS los widgets (8 valores)."""
    ventana = tk.Tk()
    ventana.title("🤖 Robot Industrial 4.0 - Control por Voz SEGURO")
    ventana.geometry("550x600")
    ventana.config(bg="#1e1e1e")

    # Título
    titulo = tk.Label(ventana, text="🔐 CONTROL SEGURO POR VOZ", 
                      font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#00ffcc")
    titulo.pack(pady=10)

    # Canvas sensores
    canvas = tk.Canvas(ventana, width=450, height=160, bg="#111", highlightthickness=2, 
                       highlightbackground="#333")
    canvas.pack(pady=20)

    # Sensores (apagados)
    temp   = canvas.create_oval(35, 35, 135, 135, fill="grey20", outline="white")
    prox   = canvas.create_oval(155, 35, 255, 135, fill="grey20", outline="white")
    energia = canvas.create_oval(275, 35, 375, 135, fill="grey20", outline="white")

    # Etiquetas de sensores
    canvas.create_text(85, 155, text="TEMP", fill="white", font=("Arial", 10, "bold"))
    canvas.create_text(205, 155, text="PROX", fill="white", font=("Arial", 10, "bold"))
    canvas.create_text(325, 155, text="ENERGÍA", fill="white", font=("Arial", 10, "bold"))

    # Instrucciones
    texto_label = tk.Label(ventana, text="🎤 Pulsa ESCUCHAR y di un comando", 
                          font=("Arial", 12), bg="#1e1e1e", fg="white")
    texto_label.pack(pady=10)

    # Estado seguridad
    estado_label = tk.Label(ventana, text="🔐 Esperando verificación...", 
                           font=("Arial", 14, "bold"), bg="#1e1e1e", fg="orange")
    estado_label.pack(pady=5)

    # Resultado comando
    resultado_label = tk.Label(ventana, text="Listo para comandos seguros", 
                              font=("Arial", 16, "bold"), bg="#1e1e1e", fg="#00ff88")
    resultado_label.pack(pady=10)

    # ✅ DEVUELVE 8 VALORES
    return (ventana, canvas, temp, prox, energia, texto_label, resultado_label, estado_label)
