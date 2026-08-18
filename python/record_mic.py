import sounddevice as sd
import soundfile as sf
sample_rate = 16000
seconds = 3
total_samples = sample_rate * seconds
recording = sd.rec(total_samples, sample_rate, channels=1)
sd.wait()
sf.write("testi.wav", recording, sample_rate)