"""
Setup script to download and configure TTS models
"""

import logging
import os
from TTS.api import TTS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def download_models():
    """Download required TTS models."""
    logger.info("Starting model download...")
    
    try:
        # Accept license terms automatically
        import sys
        from io import StringIO
        
        # Create a virtual stdin that auto-accepts
        original_stdin = sys.stdin
        
        try:
            # Set up automatic acceptance
            class AutoInput:
                def readline(self):
                    return "y\n"
                def read(self, size=-1):
                    return "y\n"
            
            sys.stdin = AutoInput()
            
            # Download XTTS v2 for multilingual support
            logger.info("Downloading XTTS v2 model...")
            tts = TTS(
                model_name="tts_models/multilingual/multi-dataset/xtts_v2",
                progress_bar=True
            )
            
            logger.info("✅ Model downloaded successfully!")
            
        finally:
            sys.stdin = original_stdin
        
        # Create directories
        os.makedirs("models", exist_ok=True)
        os.makedirs("outputs", exist_ok=True)
        os.makedirs("data", exist_ok=True)
        
        logger.info("✅ Setup complete!")
        
    except Exception as e:
        logger.error(f"Error downloading models: {e}")
        raise


if __name__ == "__main__":
    print("Voice Clone PDF Reader - Model Setup")
    print("=" * 50)
    download_models()
