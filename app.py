"""
Streamlit Web Interface for Voice Clone PDF Reader
"""

import streamlit as st
import logging
import os
import tempfile
from voice_clone_pdf_reader import PDFReader, VoiceCloneTTS

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
    
    # Voice cloning is mandatory
    st.header("🎤 Voice Sample")
    st.info("⚠️ **Required**: Upload a voice sample to clone for speech generation")
    
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
        
        # Check if voice sample is uploaded
        if voice_sample is None:
            st.warning("⚠️ Please upload a voice sample in the sidebar first!")
            st.info("Upload a 5-15 second audio clip of the voice you want to use for speech generation.")
        else:
            # Process PDF button
            if st.button("🚀 Convert PDF to Speech with Your Voice", type="primary"):
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
                            
                            # Convert to speech using voice cloning
                            with st.spinner("🎤 Generating speech with your voice... This may take a few minutes"):
                                output_dir = "outputs"
                                os.makedirs(output_dir, exist_ok=True)
                                output_file = os.path.join(
                                    output_dir, 
                                    f"{uploaded_file.name.replace('.pdf', '')}_{language}.wav"
                                )
                                
                                # Always use voice cloning
                                tts = VoiceCloneTTS(
                                    language=language,
                                    voice_sample=voice_sample
                                )
                                
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
