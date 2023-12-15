from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

def generate_audio(text):
    # generate audio from text
    audio_array = generate_audio(text)

    write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
    
    Audio(audio_array, rate=SAMPLE_RATE)

def main():
    print("Olá! Este é o terminal de conversão de texto para fala. Digite o texto que quer converter em áudio ou exit para sair!")
    input = ""
    while True:
        input = input("Digite seu texto")
        if input == 'exit':
            print("Até mais!")
            return 
        generate_audio(input)

if __name__ == '__main__':
    main()

