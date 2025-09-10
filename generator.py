import os
import time
import numpy as np
import traceback
from gtts import gTTS
from pydub import AudioSegment
import soundfile as sf

DEBUG = True

def debug_log(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")

def log(msg):
    print(f"[LOG] {msg}")

start_total = time.time()
log("Starting sound generation...")

os.makedirs("sounds/alarms", exist_ok=True)
os.makedirs("sounds/sirens", exist_ok=True)
os.makedirs("sounds/tts", exist_ok=True)

SAMPLE_RATE = 44100  # Hz

def generate_tts(text, filename):
    debug_log(f"generate_tts called with text='{text}', filename='{filename}'")
    try:
        log(f"Generating TTS (gTTS): '{text}' in {filename}")
        start = time.time()

        # gTTS só gera MP3 → salvar temporário e depois converter para WAV
        tmp_mp3 = filename.replace(".wav", ".mp3")
        tts = gTTS(text=text, lang="en")
        tts.save(tmp_mp3)

        sound = AudioSegment.from_mp3(tmp_mp3)
        sound.export(filename, format="wav")

        os.remove(tmp_mp3)

        elapsed = time.time() - start
        log(f"TTS generated in {elapsed:.2f} seconds.")
        debug_log(f"TTS file written: {filename}")

    except Exception as e:
        log(f"Error in generate_tts: {e}")
        traceback.print_exc()

def generate_alarm(freq, duration_ms, filename):
    debug_log(f"generate_alarm called with freq={freq}, duration_ms={duration_ms}, filename='{filename}'")
    try:
        log(f"Generating alarm: freq={freq}Hz, duration={duration_ms}ms in {filename}")
        start = time.time()
        duration = duration_ms / 1000
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        tone = 0.5 * np.sin(2 * np.pi * freq * t)
        sf.write(filename, tone, SAMPLE_RATE)
        elapsed = time.time() - start
        log(f"Alarm generated in {elapsed:.2f} seconds.")
        debug_log(f"Alarm file written: {filename} (shape={tone.shape})")
    except Exception as e:
        log(f"Error in generate_alarm: {e}")
        traceback.print_exc()

def generate_siren(freqs, duration_ms, filename):
    debug_log(f"generate_siren called with freqs={freqs}, duration_ms={duration_ms}, filename='{filename}'")
    try:
        log(f"Generating siren: freqs={freqs}, duration={duration_ms}ms in {filename}")
        start = time.time()
        duration = duration_ms / 1000
        total_samples = int(SAMPLE_RATE * duration)
        siren = np.zeros(total_samples)
        segment_samples = total_samples // len(freqs)

        for i, freq in enumerate(freqs):
            t = np.linspace(0, segment_samples / SAMPLE_RATE, segment_samples, False)
            siren[i * segment_samples:(i + 1) * segment_samples] = 0.5 * np.sin(2 * np.pi * freq * t)
            debug_log(f"Siren segment: freq={freq}, samples={segment_samples}")

        sf.write(filename, siren, SAMPLE_RATE)
        elapsed = time.time() - start
        log(f"Siren generated in {elapsed:.2f} seconds.")
        debug_log(f"Siren file written: {filename} (shape={siren.shape})")
    except Exception as e:
        log(f"Error in generate_siren: {e}")
        traceback.print_exc()

try:
    generate_tts("Warning!", "sounds/tts/warning.wav")
    generate_alarm(1000, 1000, "sounds/alarms/alarm1.wav")
    generate_siren([700, 1200, 700, 1200], 2000, "sounds/sirens/siren1.wav")

    generate_alarm(1500, 500, "sounds/alarms/alarm2.wav")
    generate_alarm(800, 1500, "sounds/alarms/alarm3.wav")
    generate_alarm(2000, 700, "sounds/alarms/alarm4.wav")

    generate_siren([400, 900, 400, 900], 2500, "sounds/sirens/siren2.wav")
    generate_siren([1000, 500, 1500, 500], 3000, "sounds/sirens/siren3.wav")

    generate_tts("Emergency! Please evacuate the building.", "sounds/tts/emergency.wav")
    generate_tts("System check complete. All systems operational.", "sounds/tts/system_check.wav")
    generate_tts("Attention! This is a test of the alarm system.", "sounds/tts/test_alarm.wav")

    # New Alarms
    generate_alarm(600, 2000, "sounds/alarms/alarm5.wav")
    generate_alarm(2500, 300, "sounds/alarms/alarm6.wav")
    generate_alarm(440, 1200, "sounds/alarms/alarm7.wav")
    generate_alarm(300, 800, "sounds/alarms/alarm8.wav")
    generate_alarm(1800, 600, "sounds/alarms/alarm9.wav")
    generate_alarm(1200, 1800, "sounds/alarms/alarm10.wav")
    generate_alarm(900, 400, "sounds/alarms/alarm11.wav")
    generate_alarm(1600, 1000, "sounds/alarms/alarm12.wav")

    # New Sirens
    generate_siren([300, 600, 900, 1200], 4000, "sounds/sirens/siren4.wav")
    generate_siren([1500, 1300, 1100, 900, 700, 500], 5000, "sounds/sirens/siren5.wav")
    generate_siren([600, 800, 1000, 1200, 1000, 800, 600], 6000, "sounds/sirens/siren6.wav")
    generate_siren([400, 600], 3000, "sounds/sirens/siren7.wav")
    generate_siren([1800, 1500, 1200], 4500, "sounds/sirens/siren8.wav")

    # New TTS messages
    generate_tts("Intruder alert! Zone compromised.", "sounds/tts/intruder.wav")
    generate_tts("All clear. Situation resolved.", "sounds/tts/all_clear.wav")
    generate_tts("Caution! High voltage area.", "sounds/tts/high_voltage.wav")
    generate_tts("Fire detected! Evacuate immediately.", "sounds/tts/fire.wav")
    generate_tts("Attention, please. There is a security breach.", "sounds/tts/security_breach.wav")
    generate_tts("Automated system rebooting.", "sounds/tts/reboot.wav")
    generate_tts("Power failure detected. Initiating backup systems.", "sounds/tts/power_failure.wav")
    generate_tts("Critical error! System shutdown imminent.", "sounds/tts/critical_error.wav")
    generate_tts("Temperature levels exceeding safe limits.", "sounds/tts/temperature_warning.wav")
    generate_tts("Network connection lost. Attempting to reconnect.", "sounds/tts/network_lost.wav")
    generate_tts("Incoming message.", "sounds/tts/incoming_message.wav")
    generate_tts("Warning: obstacle detected.", "sounds/tts/obstacle_detected.wav")
    generate_tts("Elevated threat level detected. Proceed with caution.", "sounds/tts/threat_level.wav")
    generate_tts("System overheating. Please check ventilation.", "sounds/tts/overheating.wav")
    generate_tts("Account locked due to multiple failed attempts.", "sounds/tts/account_locked.wav")
    generate_tts("Attention, a package has arrived at the front desk.", "sounds/tts/package_arrival.wav")
    generate_tts("Malfunction detected in sector seven.", "sounds/tts/malfunction_sector_seven.wav")
    generate_tts("Unidentified object detected. Please investigate.", "sounds/tts/unidentified_object.wav")
    generate_tts("Breach in containment field. Seal the sector.", "sounds/tts/containment_breach.wav")

except Exception as e:
    log(f"Error during sound generation: {e}")
    traceback.print_exc()

elapsed_total = time.time() - start_total
log("All sounds generated successfully!")
log(f"Total execution time: {elapsed_total:.2f} seconds.")
debug_log(f"Script finished at {time.strftime('%Y-%m-%d %H:%M:%S')}")
