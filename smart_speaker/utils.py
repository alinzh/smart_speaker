import shutil, os
import pygame
import assemblyai as aai
import yaml 
from gtts import gTTS


with open("./conf.yaml", "r") as yamlfile:
    conf = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
    
def clean_music_dir():
    path = "./music_data"
    for item in os.listdir(path):
        try: shutil.rmtree(p) if os.path.isdir(p:=os.path.join(path, item)) else os.remove(p)
        except: pass
        
def run_track(path: str, early_stop: bool = True):
    if os.path.exists(path):
        pygame.init()

        if early_stop:
            pygame.mixer.init(frequency=44100, buffer=1024)
            sound = pygame.mixer.Sound(path)
            sound.play()
            # time.sleep(5)
            # pygame.quit()
        else:
            pygame.mixer.init()  
            sound = pygame.mixer.Sound(path) 
            sound.play()
        return True
    else:
        return False
    
def speech_to_text() -> str:

    aai.settings.api_key = conf['assemblyai_key']

    audio_file = "./input.wav"

    config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best, language_code='ru')
    transcript = aai.Transcriber(config=config).transcribe(audio_file)

    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")

    return transcript.text

def text_to_speech(text: str) -> str:
    # """Synthesizes speech from the input string of text or ssml.
    # Make sure to be working in a virtual environment.

    # Note: ssml must be well-formed according to:
    #     https://www.w3.org/TR/speech-synthesis/
    # """
    # # Instantiates a client
    # client = texttospeech.TextToSpeechClient()

    # # Set the text input to be synthesized
    # synthesis_input = texttospeech.SynthesisInput(text="Hello, World!")

    # # Build the voice request, select the language code ("en-US") and the ssml
    # # voice gender ("neutral")
    # voice = texttospeech.VoiceSelectionParams(
    #     language_code="ru-RU", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    # )

    # # Select the type of audio file you want returned
    # audio_config = texttospeech.AudioConfig(
    #     audio_encoding=texttospeech.AudioEncoding.MP3
    # )

    # # Perform the text-to-speech request on the text input with the selected
    # # voice parameters and audio file type
    # response = client.synthesize_speech(
    #     input=synthesis_input, voice=voice, audio_config=audio_config
    # )

    # # The response's audio_content is binary.
    # with open("output.mp3", "wb") as out:
    #     # Write the response to the output file.
    #     out.write(response.audio_content)
    #     print('Audio content written to file "output.mp3"')
    
    # STUPED WAY:( 
    tts = gTTS(text=str(text), lang='ru', slow=False)
    tts.save("output.mp3")
        
