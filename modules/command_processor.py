# modules/command_processor.py
def procesar_comando(text, canvas, sensores, resultado_label, estado_label, 
                     ventana, autorizado: bool):
    temp, prox, energia = sensores
    text = text.lower()
    comando_final = "NINGUNO"

    if "activar" in text and "robot" in text:
        if autorizado:
            canvas.itemconfig(temp, fill="red")
            canvas.itemconfig(prox, fill="green")
            canvas.itemconfig(energia, fill="yellow")
            resultado_label.config(text="✅ Robot ACTIVADO")
            estado_label.config(text="🟢 Robot activo")
            comando_final = "activar robot"
        else:
            resultado_label.config(text="🔒 ACTIVACIÓN BLOQUEADA")
            estado_label.config(text="❌ Voz no autorizada")
            comando_final = "BLOQUEADO: activar"

    elif "detener" in text and "robot" in text:
        if autorizado:
            canvas.itemconfig(temp, fill="grey20")
            canvas.itemconfig(prox, fill="grey20")
            canvas.itemconfig(energia, fill="grey20")
            resultado_label.config(text="✅ Robot DETENIDO")
            estado_label.config(text="⚪ Detenido")
            comando_final = "detener robot"
        else:
            resultado_label.config(text="🔒 DETENCIÓN BLOQUEADA")
            estado_label.config(text="❌ Voz no autorizada")
            comando_final = "BLOQUEADO: detener"

    elif "temperatura" in text:
        canvas.itemconfig(temp, fill="red")
        resultado_label.config(text="⚠️ ALERTA: Temperatura ALTA")
        comando_final = "alerta temperatura"

    elif "revisar" in text:
        resultado_label.config(text="✅ Sensores OK")
        comando_final = "revisar sensores"

    elif "salir" in text:
        resultado_label.config(text="👋 Cerrando...")
        comando_final = "salir"
        ventana.after(1000, ventana.destroy)

    else:
        resultado_label.config(text="❓ Comando no reconocido")
        comando_final = "desconocido"

    return comando_final
