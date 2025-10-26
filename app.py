"""
Streamlit Web Interface for Voice Clone PDF Reader
"""

import streamlit as st
import logging
import os
import tempfile
from voice_clone_pdf_reader import PDFReader, VoiceCloneTTS, SileroTTSEngine, TTSEngine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Voice Clone PDF Reader",
    page_icon="🎙️",
    layout="wide"
)

# Title
st.title("🎙️ Voice Clone PDF Reader")
st.markdown("Convert PDF documents to speech using your custom voice for Indian languages and English")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Language selection
    languages = {
        "English": "english",
        "Hindi": "hindi",
        "Telugu": "telugu",
        "Tamil": "tamil",
        "Kannada": "kannada",
        "Bengali": "bengali",
        "Marathi": "marathi",
        "Gujarati": "gujarati",
        "Urdu": "urdu",
        "Punjabi": "punjabi",
        "Malayalam": "malayalam",
        "Odia": "odia"
    }
    
    selected_lang = st.selectbox(
        "Select Language",
        list(languages.keys()),
        index=0,
        help="Select the language of your PDF content"
    )
    language = languages[selected_lang]
    
    st.markdown("---")
    
    # TTS Engine selection
    st.header("🎙️ TTS Engine")
    tts_engine = st.radio(
        "Choose TTS Engine",
        ["Coqui XTTS (Voice Cloning)", "Silero TTS (Best Quality)", "Basic TTS"],
        index=0,
        help="Coqui XTTS supports voice cloning. Silero TTS offers best quality for Indian languages."
    )
    
    st.markdown("---")
    
    # Voice cloning is mandatory for Coqui XTTS
    st.header("🎤 Voice Sample")
    voice_required = tts_engine == "Coqui XTTS (Voice Cloning)"
    if voice_required:
        st.info("⚠️ **Required**: Upload a voice sample to clone for speech generation")
    else:
        st.info("ℹ️ Optional: Upload a voice sample (for Coqui XTTS only)")
    
    uploaded_voice = st.file_uploader(
        "Upload Voice Sample (WAV, MP3)",
        type=["wav", "mp3"],
        help="Upload a 5-15 second audio clip of the voice you want to clone"
    )
    
    voice_sample = None
    if uploaded_voice:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(uploaded_voice.read())
            voice_sample = tmp_file.name
        st.success(f"✅ Voice sample uploaded: {uploaded_voice.name}")

# Main area
col1, col2 = st.columns(2)

with col1:
    st.header("📄 Upload PDF")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload a PDF document to convert to speech using your voice"
    )
    
    if uploaded_file:
        st.success(f"✅ Uploaded: {uploaded_file.name}")
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name
        
        # Check if voice sample is required and uploaded
        voice_required = tts_engine == "Coqui XTTS (Voice Cloning)"
        if voice_required and voice_sample is None:
            st.warning("⚠️ Please upload a voice sample in the sidebar first!")
            st.info("Voice cloning requires a voice sample for speech generation.")
        elif not voice_required or voice_sample:
            # Process PDF button
            button_text = "🚀 Convert PDF to Speech"
            if tts_engine == "Coqui XTTS (Voice Cloning)":
                button_text = "🚀 Convert PDF to Speech with Your Voice"
            elif tts_engine == "Silero TTS (Best Quality)":
                button_text = "⚡ Convert PDF to Speech (High Quality)"
            
            if st.button(button_text, type="primary"):
                with st.spinner("Processing PDF..."):
                    try:
                        # Read PDF
                        reader = PDFReader(pdf_path)
                        text = reader.extract_text()
                        
                        if not text:
                            st.error("❌ No text extracted from PDF")
                            st.info("Make sure the PDF contains readable text (not scanned images)")
                        else:
                            st.success(f"✅ Extracted {len(text)} characters from PDF")
                            
                            # Show a preview of the text
                            with st.expander("📄 Preview Extracted Text"):
                                st.text(text[:500] + "..." if len(text) > 500 else text)
                            
                            # Convert to speech using selected TTS engine
                            spinner_text = "🎤 Generating speech..."
                            if tts_engine == "Coqui XTTS (Voice Cloning)":
                                spinner_text = "🎤 Generating speech with your voice... This may take a few minutes"
                            elif tts_engine == "Silero TTS (Best Quality)":
                                spinner_text = "⚡ Generating high-quality speech..."
                            
                            with st.spinner(spinner_text):
                                output_dir = "outputs"
                                os.makedirs(output_dir, exist_ok=True)
                                output_file = os.path.join(
                                    output_dir, 
                                    f"{uploaded_file.name.replace('.pdf', '')}_{language}.wav"
                                )
                                
                                # Select TTS engine based on user choice
                                if tts_engine == "Coqui XTTS (Voice Cloning)":
                                    if not voice_sample:
                                        st.error("❌ Voice sample required for voice cloning")
                                    else:
                                        tts = VoiceCloneTTS(
                                            language=language,
                                            voice_sample=voice_sample
                                        )
                                        audio_path = tts.speak(text, output_file=output_file)
                                        
                                elif tts_engine == "Silero TTS (Best Quality)":
                                    tts = SileroTTSEngine(language=language)
                                    audio_path = tts.speak(text, output_file=output_file)
                                    
                                else:  # Basic TTS
                                    tts = TTSEngine(language=language)
                                    audio_path = tts.speak(text, output_file=output_file)
                                
                                st.success("🎉 Audio generated successfully!")
                                
                                # Display audio player
                                with col2:
                                    st.header("🔊 Generated Audio")
                                    st.audio(output_file, format="audio/wav")
                                    
                                    # Show file info
                                    file_size = os.path.getsize(output_file)
                                    st.info(f"📊 File size: {file_size / 1024:.2f} KB")
                                    
                                    # Download button
                                    with open(output_file, "rb") as f:
                                        st.download_button(
                                            label="📥 Download Audio",
                                            data=f.read(),
                                            file_name=os.path.basename(output_file),
                                            mime="audio/wav"
                                        )
                    
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        logger.error(f"Processing error: {e}", exc_info=True)

with col2:
    st.header("🔊 Output Audio")
    st.info("Upload a PDF and voice sample to generate speech")

# Footer
st.markdown("---")
st.markdown(
    """
    ### ✨ How it Works
    1. **Upload a voice sample** - Provide a 5-15 second audio clip of the voice you want to use
    2. **Select the language** - Choose the language of your PDF content
    3. **Upload your PDF** - Upload the document you want to convert to speech
    4. **Generate** - The app will clone your voice and convert the PDF to speech using it!
    
    ### 📝 Supported Languages
    **English** (default), Hindi, Telugu, Tamil, Kannada, Bengali, Marathi, Gujarati, Urdu, Punjabi, Malayalam, and Odia
    
    ### 🎯 Features
    - 🎙️ **Voice Cloning** - Use your own voice for speech generation
    - 📄 **PDF Processing** - Extract text from any PDF document
    - 🌏 **Multi-language Support** - Works with Indian languages and English
    - 🔊 **High-quality TTS** - Professional quality speech synthesis
    """
)
