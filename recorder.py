import pyaudio
import wave
import time
import os

# script to record audio from microphone, save to file

def record_audio(filename, duration=2):
    # set up audio stream
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=44100, input=True,
                        frames_per_buffer=1024)
    frames = []

    # record audio
    for i in range(0, int(44100 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    # save audio to file
    stream.stop_stream()
    stream.close()
    audio.terminate()

    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    wavefile = wave.open(filename, 'wb')
    wavefile.setnchannels(1)
    wavefile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wavefile.setframerate(44100)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

if __name__ == '__main__':

    directory = 'samples/song_of_time'
    existing_files = os.listdir(directory)
    newest_sample = max([int(file.split('_')[1].split('.')[0]) for file in existing_files]) if existing_files else 0

    for i in range(newest_sample+1,newest_sample+1+20):
        print(f'Recording sample {i} in 3...')
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Recording...")
        record_audio(f'{directory}/sample_{i}.wav', 6)
        print("Done!")