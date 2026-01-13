from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import numpy as np

SAMPLERATE = 16000
model = Model("vosk-model-small-es-0.42")
recognizer = KaldiRecognizer(model, SAMPLERATE)

def escuchar():
    """Graba 4s y devuelve (texto, audio_crudo_int16)."""
    print("   🎤 Grabando... (4 segundos)")
    audio = sd.rec(int(4 * SAMPLERATE),
                   samplerate=SAMPLERATE,
                   channels=1,
                   dtype='int16')
    sd.wait()
    
    # Reconocimiento Vosk
    texto = ""
    if recognizer.AcceptWaveform(audio.tobytes()):
        result = json.loads(recognizer.Result())
        texto = result.get("text", "")
    
    return texto, audio.flatten()
