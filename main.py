from modules.gui_manager import crear_ventana
from modules.audio_manager import escuchar
from modules.command_processor import procesar_comando
from modules.speaker_verifier import verificar_hablante, es_autorizado
from modules.security_logger import registrar_evento
import tkinter as tk
import numpy as np

def main():
    ventana, canvas, temp, prox, energia, texto_label, resultado_label, estado_label = crear_ventana()

    def ejecutar_reconocimiento():
        texto_label.config(text="🎤 Escuchando... (4s)")
        ventana.update()

        texto, audio_data = escuchar()
        
        similitud = verificar_hablante(audio_data)
        autorizado = es_autorizado(audio_data)
        
        texto_label.config(text=f"Texto: '{texto}' | Similitud: {similitud:.2f}")
        texto_label.config(fg="green" if autorizado else "red")
        
        comando = procesar_comando(texto, canvas, (temp, prox, energia), 
                                  resultado_label, estado_label, ventana, autorizado)
        
        registrar_evento(texto, similitud, autorizado, comando)

    tk.Button(ventana, text="🎤 ESCUCHAR", command=ejecutar_reconocimiento,
              font=("Arial", 16, "bold"), bg="#00ff88", fg="black",
              width=20, height=2).pack(pady=20)

    tk.Label(ventana, text="🔐 PRIMERO: Graba tu perfil con 'grabar_perfil.py'",
             font=("Arial", 12), bg="#1e1e1e", fg="orange").pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
