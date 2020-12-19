
#import librosa
#import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def process_wav_to_jpg(file_path, path_save):
    y, sr = librosa.core.load(file_path)
    D = np.abs(librosa.stft(y))
    librosa.display.specshow(librosa.amplitude_to_db(D,ref=np.max), y_axis='log', x_axis='time')
    plt.title('Power spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    name_file = path_save.split('.')[0] + '.png'
    plt.savefig(name_file)
if __name__ == '__main__':
    process_wav_to_jpg(r'c:\Users\тс\Desktop\flask\test.wav', 'test.war')
