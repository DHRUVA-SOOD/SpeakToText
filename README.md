# SpeakToText - Audio to Text Converter

## Overview

This project is a media transcription tool that utilizes OpenAI's Whisper model to convert various audio and video files into text. The transcribed text is then saved as a JSON file in a specified directory.

## Features

- Supports multiple media file formats: `.mp3`, `.wav`, `.mp4`, `.mkv`, `.flac`, `.aac`, `.mov`, `.avi`
- Recursively scans directories for media files
- Transcribes media using Whisper
- Saves transcriptions in JSON format
- Supports CUDA acceleration for faster processing (if available)

## Requirements

- Python 3.8+
- PyTorch
- OpenAI Whisper
- FFmpeg
- Chocolatey (for Windows users to install FFmpeg)

## Installation

### 1. Install Dependencies

```sh
pip install torch whisper
```

### 2. Install FFmpeg

#### Windows:

Install FFmpeg using Chocolatey:

```sh
choco install ffmpeg
```

Ensure that the FFmpeg binary is accessible in `C:\ProgramData\chocolatey\bin`.

#### Linux/macOS:

```sh
sudo apt install ffmpeg  # Debian-based
brew install ffmpeg      # macOS (Homebrew)
```

## Usage

1. Modify the `input_directory` and `output_directory` variables in `transcriber.py` to your desired locations.
2. Run the script:

```sh
python transcriber.py
```

## Output

- Transcribed text is saved in JSON files inside the output directory.
- The output JSON files contain:
  ```json
  {
      "file": "<original file path>",
      "transcription": "<transcribed text>"
  }
  ```

## Notes

- If a CUDA-compatible GPU is available, the model will run on GPU for faster transcription.
- If running on Windows, ensure that `msvcrt.dll` is available.

## License

This project is released under the MIT License.

## Author

[Your Name]\
[Your GitHub Profile](https://github.com/yourgithub)

