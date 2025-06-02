import gradio as gr
import os
import numpy as np
from scipy.io.wavfile import write
from utils import speech_to_text
from agents_system import main
import noisereduce as nr  

SAVE_PATH = "./input.wav"
os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

def reduce_noise(audio_data, sample_rate):
    noise_sample = audio_data[:int(0.05 * sample_rate)]
    reduced_noise = nr.reduce_noise(
        y=audio_data, 
        sr=sample_rate,
        y_noise=noise_sample,
        prop_decrease=0.9  
    )
    return reduced_noise

def normalize_audio(audio_data):
    max_val = np.max(np.abs(audio_data))
    if max_val > 0:
        return audio_data / max_val
    return audio_data

def save_audio(audio, filename=SAVE_PATH):
    sample_rate, data = audio
    
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)
    
    data = reduce_noise(data, sample_rate)
    data = normalize_audio(data)
    data = (data * 32767).astype(np.int16)
    
    write(filename, sample_rate, data)
    return f"{filename}"

def chat(audio, history):
    if audio is None:
        return history
    
    save_audio(audio)
    input = speech_to_text()
    answer = main(input)
    history.append((input, answer))  
    
    return history

with gr.Blocks(title="Smart Speaker better then ALICE") as demo:
    
    chatbot = gr.Chatbot(height=300, bubble_full_width=False)
    
    with gr.Row():
        audio_input = gr.Audio(
            sources=["microphone"],
            type="numpy",
            label="Тут нажать и говорить )",
            interactive=True,
            waveform_options={"show_controls": False},
            elem_classes="audio-input"
        )
    
    audio_input.stop_recording(
        fn=chat,
        inputs=[audio_input, chatbot],
        outputs=[chatbot],
        queue=False
    )

if __name__ == "__main__":
    demo.launch()