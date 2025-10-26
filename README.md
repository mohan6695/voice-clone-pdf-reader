# Voice Clone PDF Reader with Indian Language Support

A complete Python application that reads PDF documents and converts them to speech using voice cloning technology, with support for Indian local languages including Hindi, Telugu, Tamil, Kannada, Bengali, Marathi, Gujarati, and more.

## Features

- 📄 **PDF Reading**: Extract text from PDF documents
- 🎙️ **Voice Cloning**: Clone voices for natural speech synthesis
- 🌏 **Multi-language Support**: Support for major Indian languages (Hindi, Telugu, Tamil, Kannada, Bengali, Marathi, Gujarati, Urdu, Punjabi, etc.)
- 🔊 **High-Quality TTS**: Advanced text-to-speech with voice cloning
- 🎨 **Easy-to-use Interface**: Streamlit web interface for easy interaction
- 🚀 **Batch Processing**: Process multiple PDFs at once

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone or download this repository:
```bash
cd voice-clone-pdf-reader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download voice cloning models:
```bash
python setup_models.py
```

## Usage

### Command Line Interface

```bash
python main.py --input "document.pdf" --language "hindi" --voice_clone
```

### Web Interface

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

### Python API

```python
from voice_clone_pdf_reader import PDFReader, VoiceCloneTTS

# Read PDF
reader = PDFReader("document.pdf")
text = reader.extract_text()

# Convert to speech with voice cloning
tts = VoiceCloneTTS(language="hindi")
tts.speak(text, output_file="output.wav")
```

## Supported Languages

- Hindi (हिंदी)
- Telugu (తెలుగు)
- Tamil (தமிழ்)
- Kannada (ಕನ್ನಡ)
- Bengali (বাংলা)
- Marathi (मराठी)
- Gujarati (ગુજરાતી)
- Urdu (اردو)
- Punjabi (ਪੰਜਾਬੀ)
- Malayalam (മലയാളം)
- Odia (ଓଡ଼ିଆ)

## Project Structure

```
voice-clone-pdf-reader/
├── main.py                 # Main CLI application
├── app.py                  # Streamlit web interface
├── voice_clone_pdf_reader/ # Core library
│   ├── __init__.py
│   ├── pdf_reader.py      # PDF text extraction
│   ├── voice_clone.py     # Voice cloning logic
│   └── tts_engine.py      # TTS engine
├── models/                # Pre-trained models
├── outputs/               # Generated audio files
├── data/                  # Sample files
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## Configuration

Create a `.env` file in the root directory:

```env
TTS_MODEL_PATH=models/
VOICE_CLONE_ENABLED=true
DEFAULT_LANGUAGE=hindi
OUTPUT_FORMAT=wav
```

## Examples

### Basic PDF to Speech

```python
from voice_clone_pdf_reader import PDFReader, TTSEngine

reader = PDFReader("sample.pdf")
text = reader.extract_text()

tts = TTSEngine(language="hindi")
audio = tts.speak(text)
```

### Voice Cloning

```python
from voice_clone_pdf_reader import VoiceCloneTTS

tts = VoiceCloneTTS(
    language="telugu",
    voice_sample="reference_voice.wav"
)

text = "నమస్కారం, ఇది ఒక పరీక్ష సందేశం."
tts.speak(text, output_file="telugu_output.wav")
```

## Troubleshooting

### Common Issues

1. **Model download fails**: Ensure stable internet connection
2. **Memory errors**: Reduce batch size or use GPU
3. **Audio quality issues**: Check input audio quality for voice cloning

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Acknowledgments

- Coqui TTS for the voice cloning framework
- PyPDF2 and pdfplumber for PDF processing
- The TTS community for language models
