"""
Main CLI Application for Voice Clone PDF Reader
"""

import argparse
import logging
import os
from voice_clone_pdf_reader import PDFReader, TTSEngine, VoiceCloneTTS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Voice Clone PDF Reader")
    parser.add_argument("--input", "-i", required=True, help="Input PDF file path")
    parser.add_argument("--output", "-o", help="Output audio file path")
    parser.add_argument("--language", "-l", default="hindi", 
                       help="Target language (default: hindi)")
    parser.add_argument("--voice-clone", action="store_true", 
                       help="Enable voice cloning")
    parser.add_argument("--voice-sample", "-v", 
                       help="Path to reference voice sample for cloning")
    
    args = parser.parse_args()
    
    # Validate input
    if not os.path.exists(args.input):
        logger.error(f"PDF file not found: {args.input}")
        return
    
    # Read PDF
    logger.info(f"Reading PDF: {args.input}")
    reader = PDFReader(args.input)
    text = reader.extract_text()
    
    if not text:
        logger.error("No text extracted from PDF")
        return
    
    logger.info(f"Extracted {len(text)} characters from PDF")
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        base_name = os.path.splitext(os.path.basename(args.input))[0]
        output_path = f"outputs/{base_name}_{args.language}.wav"
        os.makedirs("outputs", exist_ok=True)
    
    # Convert to speech
    logger.info(f"Converting to speech in {args.language}...")
    
    if args.voice_clone:
        if not args.voice_sample:
            logger.error("Voice sample required for voice cloning")
            return
        
        if not os.path.exists(args.voice_sample):
            logger.error(f"Voice sample not found: {args.voice_sample}")
            return
        
        tts = VoiceCloneTTS(language=args.language, voice_sample=args.voice_sample)
        audio_path = tts.speak(text, output_file=output_path)
    else:
        tts = TTSEngine(language=args.language)
        audio_path = tts.speak(text, output_file=output_path)
    
    logger.info(f"✅ Audio generated successfully: {audio_path}")


if __name__ == "__main__":
    main()
