# modules/speaker_verifier.py
import numpy as np
from pathlib import Path

PERFIL_AUTORIZADO = Path("audio_autorizado.npy")
UMBRAL_SIMILITUD = 0.7

_EMBEDDING_PERFIL = None

def cargar_perfil():
    """Carga el perfil de voz autorizado."""
    global _EMBEDDING_PERFIL
    if PERFIL_AUTORIZADO.exists():
        _EMBEDDING_PERFIL = np.load(PERFIL_AUTORIZADO)
        return True
    return False

def extraer_embedding(audio_data):
    """Extrae características simples del audio (energía + espectro básico)."""
    # Energía RMS simple
    energia = np.sqrt(np.mean(audio_data**2))
    
    # Espectro de potencia básico (sin FFT completa)
    espectro = np.abs(np.fft.rfft(audio_data[:4000]))  # Primeros 0.25s
    espectro_media = np.mean(espectro)
    espectro_var = np.var(espectro)
    
    return np.array([energia, espectro_media, espectro_var, 
                     np.mean(audio_data), np.std(audio_data)])

def verificar_hablante(audio_data) -> float:
    """Compara audio actual con perfil autorizado."""
    if not cargar_perfil():
        return 0.0
    
    emb_actual = extraer_embedding(audio_data)
    similitud = 1 - np.linalg.norm(_EMBEDDING_PERFIL - emb_actual)
    return max(0.0, float(similitud))

def es_autorizado(audio_data) -> bool:
    return verificar_hablante(audio_data) >= UMBRAL_SIMILITUD
