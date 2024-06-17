---
title: {{Speech Translation Synthesis}}
emoji: {{🗣️}}
colorFrom: {{green}}
colorTo: {{indigo}}
sdk: {{gradio}}
sdk_version: "{{4.36.1}}"
app_file: app.py
pinned: true
---

# Speech Translation Synthesis
### A Speech-To-Speech Translator

SDSU's Artificial Intelligence Club Group Project Spring 2024 semester

This is a Gradio-based demo that performs speech-to-speech translation. It uses the Whisper model for speech-to-text transcription, the `translate` library for translation, and the Coqui TTS model for text-to-speech synthesis. 

## Features
- Transcribe speech from an audio file or microphone input
- Translate transcribed text into a selected target language
- Synthesize translated text back into speech using the input speaker's voice

## Requirements
- Python 3.7 or higher
- Required Python packages listed in `requirements.txt`

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/irmtou/speechtranslationsynthesis.git
    cd speechtranslationsynthesis
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```sh
    python app.py
    ```

2. **Access the demo interface:**
    - After running the application, Gradio will provide you with a local URL. Open this URL in your web browser to access the demo interface.

## Code Explanation

- **app.py**: The main application script that sets up the Gradio interface and defines the functions for speech-to-text transcription, translation, and text-to-speech synthesis.

### Key Components
- **speech_to_text(audio)**: Uses the Whisper model to transcribe speech from an audio file.
- **translate(text, language)**: Translates the transcribed text into the target language.
- **s2s(audio, language)**: Combines the transcription and translation functions, then synthesizes the translated text into speech using the input speaker's voice.

### Supported Languages 🗣️
- Arabic 
- Portuguese
- Chinese
- Czech
- Dutch
- English
- French
- German
- Italian
- Polish
- Russian
- Spanish
- Turkish
- Korean
- Hungarian
- Hindi

## License 
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
- SDSU's Artificial Intelligence Club for giving us the idea.
- [Gradio](https://www.gradio.app/) for providing the easy-to-use interface library.
- [Whisper](https://github.com/openai/whisper) for the speech-to-text model.
- [Coqui TTS](https://github.com/coqui-ai/TTS) for the text-to-speech synthesis model.
- [translate](https://pypi.org/project/translate/) for the translation functionality.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## Contact
For questions or support, please contact [elee200@hotmail.com].


