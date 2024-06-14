import gradio as gr
import whisper
from translate import Translator
import os

os.environ["COQUI_TOS_AGREED"] = "1"
# # Set the TTS_TOS environment variable
# os.environ["TTS_TOS"] = "non-commercial"

# Loading the base model
model = whisper.load_model("base")


def speech_to_text(audio_file):
    """
    :param audio_file: Input audio file
    :return: result["text"] - The transcribed text after processing the input
    """
    result = model.transcribe(audio_file)
    print(result["text"])
    return result["text"]  # Only first tuple


# Defining the Translate Function
def translate(text, language):
    """

    :param text: Input text to be translated
    :param language: Language choice
    :return: translated_text - The translated text
    """
    translator = Translator(to_lang=language)
    translated_text = translator.translate(text)
    return translated_text


# Initialize TTS model outside the function to avoid reinitialization on each call
from TTS.api import TTS

tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)


# Speech to Speech Function
def s2s(audio, language):
    """

    :param audio:
    :param language:
    :return:
    """
    print(audio)
    # Load the audio file from the file path
    result_text = speech_to_text(audio)
    translated_text = translate(result_text, language)

    # Generate speech using the input audio as the speaker's voice
    tts_model.tts_to_file(text=translated_text,
                          file_path="output.wav",
                          speaker_wav=audio,
                          language=language)

    return [result_text, translated_text, "output.wav"]


# List of supported language codes
language_names = ["Arabic", "Portuguese", "Chinese", "Czech", "Dutch",
                  "English", "French", "German", "Italian", "Polish",
                  "Russian", "Spanish", "Turkish", "Korean",
                  "Hungarian", "Hindi"]
language_options = ["ar", "pt", "zh-cn", "cs", "nl", "en", "fr", "de",
                    "it", "pl", "ru", "es", "tr", "ko", "hu", "hi"]

language_dropdown = gr.Dropdown(choices=zip(language_names, language_options),
                                value="es",
                                label="Target Language",
                                )

translate_button = gr.Button(value="Synthesize and Translate my Voice!")
transcribed_text = gr.Textbox(label="Transcribed Text")
output_text = gr.Textbox(label="Translated Text")
output_speech = gr.Audio(label="Translated Speech", type="filepath")

# Gradio interface with the transcribe function as the main function
demo = gr.Interface(
    fn=s2s,
    inputs=[gr.Audio(sources=["upload", "microphone"],
                     type="filepath",
                     format='wav',
                     show_download_button=True,
                     waveform_options=gr.WaveformOptions(
                         waveform_color="#01C6FF",
                         waveform_progress_color="FF69B4",
                         skip_length=2,
                         show_controls=False,
                     )
                     ),
            language_dropdown],
    outputs=[transcribed_text, output_text, output_speech],
    theme=gr.themes.Soft(),
    title="Speech-to-Speech Translation (Demo)"
)

demo.launch(debug=True, share=True)
