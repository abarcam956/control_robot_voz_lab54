# modules/security_logger.py
from datetime import datetime

def registrar_evento(texto: str, similitud: float, autorizado: bool, comando: str):
    estado = "✅ AUTORIZADO" if autorizado else "❌ NO_AUTORIZADO"
    linea = (f"{datetime.now()} | {estado} | sim={similitud:.3f} | "
             f"'{texto}' | {comando}\n")
    with open("security_log.txt", "a", encoding="utf-8") as f:
        f.write(linea)
    print(linea.strip())
