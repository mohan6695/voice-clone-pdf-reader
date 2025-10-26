"""
Voice Clone PDF Reader - A library for converting PDFs to speech with voice cloning
"""

from .pdf_reader import PDFReader
from .tts_engine import TTSEngine, VoiceCloneTTS, GoogleTTSEngine, SileroTTSEngine
from .voice_clone import VoiceCloner

__version__ = "1.0.0"
__all__ = ["PDFReader", "TTSEngine", "VoiceCloneTTS", "GoogleTTSEngine", "SileroTTSEngine", "VoiceCloner"]
