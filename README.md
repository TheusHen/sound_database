# Auto Sound Database Generator
[![AI Model DeepSeek R1](https://img.shields.io/badge/Model-Gemini%202.0%20Flash-536af5?color=536af5&logoColor=white)](https://gemini.google.com/)

This project generates a database of alarm sounds, sirens, and English TTS (Text-to-Speech) messages using Python. The audio files are organized into specific folders and can be used in alert systems, testing, automation, or various applications.

## Features

- Automatic generation of alarm sounds with different frequencies and durations.
- Creation of sirens with tone variation.
- Generation of English TTS messages using pyttsx3.
- Organization of files into `sounds/alarms`, `sounds/sirens`, and `sounds/tts`.
- Detailed logs and execution time measurement for each step.

## Directory Structure

```
sounds/
  alarms/   # .wav alarm files
  sirens/   # .wav siren files
  tts/      # .wav TTS message files
generator.py
requirements.txt
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/TheusHen/sound_database.git
   cd sound_database
   ```

2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

   > **Note:** You may need to have `ffmpeg` installed for pyttsx3 to work on some systems.

## Usage

Run the main script to generate all sounds:

```sh
python generator.py
```

The generated files will be in the `sounds/alarms`, `sounds/sirens`, and `sounds/tts` folders.

## Example Sound Generation

The script creates sounds such as:

- `sounds/alarms/alarm1.wav` (default alarm)
- `sounds/sirens/siren1.wav` (various sirens)
- `sounds/tts/warning.wav` (TTS message)

## Automation via GitHub Actions

The project includes a workflow (`.github/workflows/sound.yml`) for automatic updating of sounds and code using Deepseek R1.

## License

This project is under the [Unlicense](LICENSE), allowing free use for any purpose.

## Contributing

Feel free to open issues or pull requests with suggestions for new sounds or code improvements.

## Author

Developed by TheusHen.
