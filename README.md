# Laboratorio 54: Control por voz de un robot industrial 4.0

## Objetivo

Integrar reconocimiento de voz offline (**Vosk**) con **Tkinter** para controlar un semáforo industrial tricolor simulado, **añadiendo verificación biométrica de hablante** para comandos críticos.

**Seguridad 4.0 implementada**: Solo voces autorizadas pueden ejecutar "activar robot" y "detener robot".

## Comandos

| Comando | Acción | Requiere verificación |
|---------|--------|----------------------|
| `"activar robot"` | 🟢 Enciende sensores | **✅ SÍ** |
| `"detener robot"` | ⚪ Apaga sensores | **✅ SÍ** |
| `"temperatura alta"` | 🔴 Alerta temperatura | ❌ NO |
| `"revisar sensores"` | 🆗 Estado sensores | ❌ NO |
| `"salir"` | 👋 Cierra app | ❌ NO |

## Requisitos

- **Python 3.9+**
- **Micrófono funcional**
- **Dependencias mínimas** (3 paquetes):
```bash
pip install -r requirements.txt  # vosk sounddevice numpy

🚀 Instalación y Primer Uso
bash
# 1. Clonar repositorio
git clone <tu-repo>
cd control_robot_voz_lab54

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Descargar modelo Vosk español (50MB)
# Se descarga automáticamente o manual: vosk-model-small-es-0.42.zip

# 4. GRABAR TU PERFIL DE VOZ (IMPORTANTE - 1 vez)
python grabar_perfil.py
# → Di "activar robot" durante 5 segundos 🎤

# 5. Ejecutar
python main.py
🎮 Demo de Uso
text
1. Pulsa "🎤 ESCUCHAR"
2. Di un comando (5 segundos)
3. Sistema muestra: "Texto: 'activar robot' | Similitud: 0.82"
4. Si eres autorizado → Robot se activa 🟢
5. Si no → "🔒 ACCESO DENEGADO"
🔐 Funcionalidades de Seguridad
Verificación Biométrica
Extrae embedding de voz (energía + espectro)

Compara con perfil autorizado (audio_autorizado.npy)

Umbral 0.7: ≥ autorizado, < bloqueado

Registro de Eventos
Archivo security_log.txt:

text
2026-01-13T09:03:45 | ✅ AUTORIZADO | sim=0.823 | 'activar robot' | activar robot
2026-01-13T09:04:12 | ❌ NO_AUTORIZADO | sim=0.342 | 'activar robot' | BLOQUEADO: activar
