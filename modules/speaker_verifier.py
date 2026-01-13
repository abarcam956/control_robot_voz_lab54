import numpy as np
from pathlib import Path

PERFIL_AUTORIZADO = Path("perfil_autorizado.npy")
UMBRAL_SIMILITUD = 0.25  

_EMBEDDING_PERFIL = None

def cargar_perfil():
    global _EMBEDDING_PERFIL
    if PERFIL_AUTORIZADO.exists():
        _EMBEDDING_PERFIL = np.load(PERFIL_AUTORIZADO)
        return True
    return False

def extraer_embedding(audio_data: np.ndarray) -> np.ndarray:
    """Embedding SIMPLE con numpy (sin dependencias externas)"""
    audio = audio_data.astype(np.float32)
    
    # Características de voz
    energia = np.sqrt(np.mean(audio ** 2))
    espectro = np.abs(np.fft.rfft(audio[:8000])) 
    zeros_crossing = np.mean(np.diff(np.signbit(audio)) != 0)
    
    return np.array([
        energia,
        np.mean(espectro),
        np.std(espectro),
        zeros_crossing,
        np.mean(audio),
        np.std(audio)
    ], dtype=np.float32)

def verificar_hablante(audio_data: np.ndarray) -> float:
    if _EMBEDDING_PERFIL is None and not cargar_perfil():
        return 0.0
    
    emb_actual = extraer_embedding(audio_data)
    distancia = np.linalg.norm(_EMBEDDING_PERFIL - emb_actual)
    similitud = 1.0 / (1.0 + distancia)
    return float(similitud)

def es_autorizado(audio_data: np.ndarray) -> bool:
    return verificar_hablante(audio_data) >= UMBRAL_SIMILITUD
