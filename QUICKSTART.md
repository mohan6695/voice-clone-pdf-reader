# Quick Start Guide

## Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Download models:**
```bash
python setup_models.py
```

This will download the XTTS v2 model (~2GB) - ensure you have a stable internet connection.

## Usage

### Option 1: Web Interface (Recommended)

Launch the Streamlit web interface:
```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501` and:
1. Select your language
2. Upload a PDF file
3. Optionally enable voice cloning and upload a voice sample
4. Click "Convert to Speech"
5. Download the generated audio

### Option 2: Command Line

Basic usage:
```bash
python main.py --input document.pdf --language hindi
```

With voice cloning:
```bash
python main.py --input document.pdf --language telugu --voice-clone --voice-sample reference.wav
```

### Option 3: Python API

```python
from voice_clone_pdf_reader import PDFReader, TTSEngine

# Read PDF
reader = PDFReader("document.pdf")
text = reader.extract_text()

# Convert to speech
tts = TTSEngine(language="hindi")
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

## Voice Cloning

For best voice cloning results:
- Use a clear, single speaker audio sample
- Duration: 3-10 seconds
- Format: WAV or MP3
- Sample rate: 16kHz or higher
- Background noise: Minimal

## Troubleshooting

**Problem:** Model download fails
**Solution:** Check your internet connection and ensure you have enough disk space (~3GB)

**Problem:** Audio generation is slow
**Solution:** Use GPU acceleration if available (CUDA-compatible GPU required)

**Problem:** Poor audio quality
**Solution:** Ensure input PDF has clear, readable text. For voice cloning, use high-quality voice samples.

## System Requirements

- **RAM:** Minimum 4GB (8GB recommended)
- **Disk Space:** 5GB free space for models
- **Python:** 3.8 or higher
- **OS:** Windows, macOS, or Linux

## Notes

- First run will download model files (~2GB)
- Audio generation may take time on CPU
- GPU acceleration significantly improves speed
