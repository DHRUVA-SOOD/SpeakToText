import os
import json
import torch
import whisper
import ctypes
import sys
from pathlib import Path

# Update PATH to include FFmpeg
os.environ["PATH"] += os.pathsep + r"C:\ProgramData\chocolatey\bin"

def find_media_files(directory):
    """Recursively find all audio and video files in a directory."""
    media_extensions = {'.mp3', '.wav', '.mp4', '.mkv', '.flac', '.aac', '.mov', '.avi'}
    media_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if Path(file).suffix.lower() in media_extensions:
                media_files.append(os.path.join(root, file))
    return media_files

def transcribe_media(file_path, model):
    """Transcribe the given media file using Whisper."""
    print(f"Transcribing: {file_path}")
    result = model.transcribe(file_path, fp16=False)  # Forcing FP32 execution
    return result['text']

def save_transcription(file_path, transcription, output_dir):
    """Save transcription as a JSON file in the output directory."""
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, Path(file_path).stem + '.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({'file': file_path, 'transcription': transcription}, f, indent=4)
    print(f"Saved transcription: {output_file}")

def process_directory(input_dir, output_dir):
    """Process all media files in the given directory."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        print("CUDA not available. Running on CPU.")
    else:
        print("CUDA available. Running on GPU.")
    
    # Manually assign libc on Windows
    try:
        if sys.platform == "win32":
            libc_name = "msvcrt.dll"  # Microsoft C Runtime
        else:
            libc_name = ctypes.util.find_library("c")

        if libc_name is None:
            raise RuntimeError("Could not find a suitable C library.")
        
        ctypes.CDLL(libc_name)  # Load the library
    except Exception as e:
        print(f"Error loading C library: {e}")
        return
    
    model = whisper.load_model("tiny").to(device)  # Load model to available device
    media_files = find_media_files(input_dir)
    
    for file in media_files:
        transcription = transcribe_media(file, model)
        save_transcription(file, transcription, output_dir)

if __name__ == "__main__":
    input_directory = r"C:\internshhip"  # Change as needed
    output_directory = r"C:\internshhip\transcriptions"
    process_directory(input_directory, output_directory)
