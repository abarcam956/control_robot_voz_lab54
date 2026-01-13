import sounddevice as sd
import numpy as np
from scipy.io import wavfile
from speaker_verifier import extraer_embedding

SAMPLERATE = 16000
DURACION = 4

print("🎤 GRABA TU PERFIL DE VOZ")
print("Di claramente: 'activar robot'")
print("Grabando!!")

audio = sd.rec(int(DURACION * SAMPLERATE),
               samplerate=SAMPLERATE,
               channels=1,
               dtype='int16')
sd.wait()

print("✅ Grabación terminada")

# Guardar WAV para escucharlo
wavfile.write("audio_autorizado.wav", SAMPLERATE, audio)
print("✅ Guardado: audio_autorizado.wav")

# Extraer y guardar embedding
embedding = extraer_embedding(audio.flatten())
np.save("perfil_autorizado.npy", embedding)
print("✅ Guardado: perfil_autorizado.npy")
print("🎉 ¡Perfil listo! Ahora ejecuta: python main.py")
