"""
Voice Cloning Module - Advanced voice cloning capabilities
"""

import os
import logging
import numpy as np
import soundfile as sf
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


class VoiceCloner:
    """Advanced voice cloning utilities."""
    
    def __init__(self, device: Optional[str] = None):
        """
        Initialize Voice Cloner.
        
        Args:
            device: Device to use ('cpu' or 'cuda')
        """
        import torch
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Voice Cloner initialized on {self.device}")
    
    def validate_audio_quality(self, audio_path: str) -> Tuple[bool, str]:
        """
        Validate audio quality for voice cloning.
        
        Args:
            audio_path: Path to audio file
            
        Returns:
            Tuple of (is_valid, message)
        """
        try:
            audio, sr = sf.read(audio_path)
            duration = len(audio) / sr
            
            # Check duration (recommended: 3-10 seconds)
            if duration < 2:
                return False, f"Audio too short ({duration:.1f}s). Need at least 2 seconds."
            if duration > 30:
                return False, f"Audio too long ({duration:.1f}s). Recommended max 30 seconds."
            
            # Check sample rate
            if sr < 16000:
                return False, f"Sample rate too low ({sr}Hz). Need at least 16kHz."
            
            # Check for silence
            max_amp = np.max(np.abs(audio))
            if max_amp < 0.01:
                return False, "Audio appears to be silent or too quiet."
            
            return True, "Audio quality validated"
        
        except Exception as e:
            logger.error(f"Error validating audio: {e}")
            return False, f"Validation error: {e}"
