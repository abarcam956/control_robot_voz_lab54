# grabar_perfil.py
import sounddevice as sd
import numpy as np
from speaker_verifier import extraer_embedding

print("🎤 GRABA TU PERFIL DE VOZ (di 'activar robot')")
audio = sd.rec(int(5*16000), samplerate=16000, channels=1, dtype='int16')
sd.wait()
embedding = extraer_embedding(audio.flatten())
np.save("audio_autorizado.npy", embedding)
print("✅ ¡Perfil guardado! Ahora puedes usar el sistema.")
