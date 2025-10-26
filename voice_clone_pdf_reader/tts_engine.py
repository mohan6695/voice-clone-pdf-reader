"""
TTS Engine Module - Text-to-Speech conversion with Indian language support
"""

import os
import logging
from typing import Optional, Union
import tempfile
import torch
from TTS.api import TTS

# Try to import gTTS for better quality Indian language support
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    logging.warning("gTTS not available. Install with: pip install gtts")

logger = logging.getLogger(__name__)


# Language mappings for Indian languages
LANGUAGE_CODES = {
    "hindi": "hi",
    "telugu": "te",
    "tamil": "ta",
    "kannada": "kn",
    "bengali": "bn",
    "marathi": "mr",
    "gujarati": "gu",
    "urdu": "ur",
    "punjabi": "pa",
    "malayalam": "ml",
    "odia": "or",
    "english": "en",
}


class TTSEngine:
    """Basic Text-to-Speech Engine."""
    
    def __init__(self, language: str = "hindi", device: Optional[str] = None):
        """
        Initialize TTS Engine.
        
        Args:
            language: Target language
            device: Device to use ('cpu' or 'cuda')
        """
        self.language = language.lower()
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Load the TTS model."""
        try:
            logger.info(f"Loading TTS model for language: {self.language}")
            
            # Try XTTS v1.5 first (better quality than v2 for some use cases)
            try:
                model_name = "tts_models/multilingual/multi-dataset/xtts"
                logger.info(f"Attempting to load: {model_name}")
                self.model = TTS(
                    model_name=model_name,
                    progress_bar=True,
                    gpu=self.device == "cuda"
                )
            except Exception as e:
                logger.warning(f"XTTS v1.5 failed, falling back to XTTS v2: {e}")
                # Fallback to XTTS v2
                self.model = TTS(
                    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
                    progress_bar=True,
                    gpu=self.device == "cuda"
                )
            
            logger.info(f"TTS model loaded successfully on {self.device}")
        except Exception as e:
            logger.error(f"Error loading TTS model: {e}")
            raise
    
    def speak(self, text: str, output_file: Optional[str] = None) -> str:
        """
        Convert text to speech and save to file.
        
        Args:
            text: Input text
            output_file: Output file path (optional)
            
        Returns:
            Path to output audio file
        """
        if not self.model:
            raise ValueError("Model not loaded")
        
        if output_file is None:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                output_file = tmp_file.name
        
        # Use basic parameters that work with all models
        self.model.tts_to_file(
            text=text,
            file_path=output_file,
            language=LANGUAGE_CODES.get(self.language, "hi")
        )
        
        logger.info(f"Audio saved to: {output_file}")
        return output_file


class GoogleTTSEngine:
    """Google TTS Engine - Better quality for Indian languages."""
    
    def __init__(self, language: str = "hindi"):
        """
        Initialize Google TTS Engine.
        
        Args:
            language: Target language
        """
        self.language = language.lower()
        
        # Map to Google TTS language codes
        self.GTTS_LANGUAGE_CODES = {
            "hindi": "hi",
            "telugu": "te",
            "tamil": "ta",
            "kannada": "kn",
            "bengali": "bn",
            "marathi": "mr",
            "gujarati": "gu",
            "urdu": "ur",
            "punjabi": "pa",
            "malayalam": "ml",
            "odia": "or",
            "english": "en",
        }
    
    def speak(self, text: str, output_file: Optional[str] = None) -> str:
        """
        Convert text to speech using Google TTS.
        
        Args:
            text: Input text
            output_file: Output file path (optional)
            
        Returns:
            Path to output audio file
        """
        if not GTTS_AVAILABLE:
            raise ImportError("gTTS is not installed. Please install it with: pip install gtts")
        
        if output_file is None:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
                output_file = tmp_file.name
        
        lang_code = self.GTTS_LANGUAGE_CODES.get(self.language, "hi")
        
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(output_file)
        
        logger.info(f"Google TTS audio saved to: {output_file}")
        return output_file


class VoiceCloneTTS(TTSEngine):
    """TTS Engine with Voice Cloning support."""
    
    def __init__(
        self,
        language: str = "hindi",
        voice_sample: Optional[str] = None,
        device: Optional[str] = None
    ):
        """
        Initialize Voice Cloning TTS Engine.
        
        Args:
            language: Target language
            voice_sample: Path to reference voice sample for cloning
            device: Device to use
        """
        self.voice_sample = voice_sample
        super().__init__(language, device)
    
    def clone_voice(self, text: str, reference_voice: Optional[str] = None, output_file: Optional[str] = None) -> str:
        """
        Generate speech with voice cloning.
        
        Args:
            text: Input text
            reference_voice: Path to reference voice sample
            output_file: Output file path
            
        Returns:
            Path to output audio file
        """
        if not self.model:
            raise ValueError("Model not loaded")
        
        reference = reference_voice or self.voice_sample
        if not reference:
            raise ValueError("Reference voice sample is required for voice cloning")
        
        if output_file is None:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                output_file = tmp_file.name
        
        try:
            # Use XTTS v2 for voice cloning
            self.model.tts_to_file(
                text=text,
                file_path=output_file,
                speaker_wav=reference,
                language=LANGUAGE_CODES.get(self.language, "hi")
            )
            
            logger.info(f"Voice cloned speech saved to: {output_file}")
            return output_file
        except Exception as e:
            logger.error(f"Error in voice cloning: {e}")
            raise
    
    def speak(self, text: str, output_file: Optional[str] = None) -> str:
        """Convert text to speech with voice cloning."""
        return self.clone_voice(text, output_file=output_file)
