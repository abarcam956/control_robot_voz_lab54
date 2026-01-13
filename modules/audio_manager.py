# modules/audio_manager.py
from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import numpy as np

samplerate = 16000
model = Model("vosk-model-small-es-0.42")
recognizer = KaldiRecognizer(model, samplerate)

def escuchar():
    """Graba 5s y devuelve (texto, audio_crudo)."""
    print("🎤 Grabando...")
    audio = sd.rec(int(5 * samplerate), samplerate=samplerate,
                   channels=1, dtype='int16')
    sd.wait()
    
    # Reconocimiento Vosk
    texto = ""
    if recognizer.AcceptWaveform(audio.tobytes()):
        result = json.loads(recognizer.Result())
        texto = result.get("text", "")
    
    return texto, audio.flatten()
