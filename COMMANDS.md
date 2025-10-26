# Voice Clone PDF Reader - Useful Commands

## 📁 Project Setup

### Activate Virtual Environment
```bash
source venv/bin/activate
```

### Deactivate Virtual Environment
```bash
deactivate
```

## 🚀 Running the Application

### Start Streamlit Web App
```bash
source venv/bin/activate
streamlit run app.py
```

### Run CLI Application
```bash
source venv/bin/activate
python main.py --input "document.pdf" --language english --voice-clone --voice-sample reference.wav
```

### Run Python API
```python
from voice_clone_pdf_reader import PDFReader, VoiceCloneTTS

# Read PDF
reader = PDFReader("document.pdf")
text = reader.extract_text()

# Convert to speech with voice cloning
tts = VoiceCloneTTS(language="english", voice_sample="reference.wav")
audio_path = tts.speak(text, output_file="output.wav")
```

## 🔧 Setup & Installation

### Install Dependencies
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Download TTS Models
```bash
source venv/bin/activate
python setup_models.py
```

### Install Additional Packages
```bash
source venv/bin/activate
pip install gtts watchgod
```

## 📦 Git Commands

### Check Status
```bash
git status
```

### Add Changes
```bash
git add .
```

### Commit Changes
```bash
git commit -m "Your commit message"
```

### View Commit History
```bash
git log --oneline
```

### Add Remote Repository and Push to GitHub

**Step 1:** Create repository at https://github.com/new
- Name: `voice-clone-pdf-reader`
- Choose Public or Private
- Don't initialize with README

**Step 2:** Push to GitHub
```bash
# Add remote (replace YOUR_USERNAME):
git remote add origin https://github.com/YOUR_USERNAME/voice-clone-pdf-reader.git

# Switch to main branch:
git branch -M main

# Push your code:
git push -u origin main
```

**Authentication:**
```bash
# Enable credential helper (macOS):
git config --global credential.helper osxkeychain

# Generate GitHub Personal Access Token:
# Visit: https://github.com/settings/tokens
# Create token with 'repo' scope
# Use token as password when pushing
```

## 🧹 Cleanup Commands

### Remove Generated Audio Files
```bash
rm outputs/*.wav outputs/*.mp3
```

### Clean Python Cache
```bash
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

## 🔍 Useful Commands

### List Installed Packages
```bash
source venv/bin/activate
pip list
```

### Update a Package
```bash
source venv/bin/activate
pip install --upgrade <package-name>
```

### Check Python Version
```bash
source venv/bin/activate
python --version
```

### Check Disk Usage
```bash
du -sh venv/
du -sh outputs/
```

### Find Large Files
```bash
find . -type f -size +100M
```

## 🛠️ Troubleshooting

### Reinstall Dependencies
```bash
source venv/bin/activate
pip install --force-reinstall -r requirements.txt
```

### Check Streamlit Port
```bash
lsof -i :8501
lsof -i :8502
```

### Kill Streamlit Process
```bash
pkill -f streamlit
```

### Test PDF Reading
```bash
source venv/bin/activate
python -c "from voice_clone_pdf_reader import PDFReader; r = PDFReader('test.pdf'); print(r.extract_text())"
```

## 📝 Environment Variables

Create a `.env` file:
```bash
cat > .env << EOF
TTS_MODEL_PATH=models/
VOICE_CLONE_ENABLED=true
DEFAULT_LANGUAGE=english
OUTPUT_FORMAT=wav
EOF
```

## 🌐 Access App

### Local Access
```bash
http://localhost:8501
# or
http://localhost:8502
```

### Network Access
```bash
http://192.168.1.72:8502
```
(Your network IP from the Streamlit output)

