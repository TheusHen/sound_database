import os
import time
import numpy as np
import pyttsx3
import soundfile as sf

def log(msg):
    print(f"[LOG] {msg}")

start_total = time.time()
log("Iniciando geração de sons...")

os.makedirs("sounds/alarms", exist_ok=True)
os.makedirs("sounds/sirens", exist_ok=True)
os.makedirs("sounds/tts", exist_ok=True)

SAMPLE_RATE = 44100  # Hz

def generate_tts(text, filename):
    log(f"Gerando TTS: '{text}' em {filename}")
    start = time.time()
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    elapsed = time.time() - start
    log(f"TTS gerado em {elapsed:.2f} segundos.")

def generate_alarm(freq, duration_ms, filename):
    log(f"Gerando alarme: freq={freq}Hz, duração={duration_ms}ms em {filename}")
    start = time.time()
    duration = duration_ms / 1000
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * freq * t)
    sf.write(filename, tone, SAMPLE_RATE)
    elapsed = time.time() - start
    log(f"Alarme gerado em {elapsed:.2f} segundos.")

def generate_siren(freqs, duration_ms, filename):
    log(f"Gerando sirene: freqs={freqs}, duração={duration_ms}ms em {filename}")
    start = time.time()
    duration = duration_ms / 1000
    total_samples = int(SAMPLE_RATE * duration)
    siren = np.zeros(total_samples)
    segment_samples = total_samples // len(freqs)

    for i, freq in enumerate(freqs):
        t = np.linspace(0, segment_samples / SAMPLE_RATE, segment_samples, False)
        siren[i * segment_samples:(i + 1) * segment_samples] = 0.5 * np.sin(2 * np.pi * freq * t)

    sf.write(filename, siren, SAMPLE_RATE)
    elapsed = time.time() - start
    log(f"Sirene gerada em {elapsed:.2f} segundos.")

# Sons padrão
generate_tts("Warning!", "sounds/tts/warning.wav")
generate_alarm(1000, 1000, "sounds/alarms/alarm1.wav")
generate_siren([700, 1200, 700, 1200], 2000, "sounds/sirens/siren1.wav")

# Novos sons de alarme
generate_alarm(1500, 500, "sounds/alarms/alarm2.wav")
generate_alarm(800, 1500, "sounds/alarms/alarm3.wav")
generate_alarm(2000, 700, "sounds/alarms/alarm4.wav")

# Novas sirenes
generate_siren([400, 900, 400, 900], 2500, "sounds/sirens/siren2.wav")
generate_siren([1000, 500, 1500, 500], 3000, "sounds/sirens/siren3.wav")

# Novos TTS
generate_tts("Emergency! Please evacuate the building.", "sounds/tts/emergency.wav")
generate_tts("System check complete. All systems operational.", "sounds/tts/system_check.wav")
generate_tts("Attention! This is a test of the alarm system.", "sounds/tts/test_alarm.wav")

elapsed_total = time.time() - start_total
log("Todos os sons gerados com sucesso!")
log(f"Tempo total de execução: {elapsed_total:.2f} segundos.")
