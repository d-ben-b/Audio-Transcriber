<!-- @format -->

# Audio-Transcriber

Audio-Transcriber is a user-friendly desktop application designed to transcribe audio files using the Whisper model. It features a simple graphical interface built with tkinter, allowing users to either record audio directly or transcribe existing audio files.

## Features

- **Record Audio**: Record audio directly through the application.
- **Transcribe Audio**: Transcribe audio files to text using the powerful Whisper model.
- **File Support**: Supports WAV and M4A files.
- **Easy-to-use Interface**: Simple and intuitive graphical user interface.

## Installation

### Requirements

- Python 3.6 or newer
- Whisper
- pyaudio
- tkinter (should be included with Python if not you can install using your system's package manager)
- pip install yt-dlp
- pip install openai-whisper
- pip install pyaudio

Before installing Audio-Transcriber, ensure you have Python installed on your system. You can download it from [Python.org](https://www.python.org/downloads/).

### Setup

To install Audio-Transcriber, follow these steps:

1. **Clone the repository** (or download the ZIP file and extract it):

   ```bash
   git clone https://github.com/d-ben-b/Audio-Transcriber.git
   cd AudioTranscriber

   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

3. Run the setup script:

   ```bash
   python setup.py install

   ```

4. Launch the application:
   ```bash
   audio-transcriber
   ```
