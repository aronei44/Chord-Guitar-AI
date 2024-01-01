# CHORD GUITAR AI

## Introduction

This project is a part of Chord Guitar AI Product. The purpose of this project is to build a model that can predict the chord of a guitar from an audio file.

## Dataset

Dataset can be found from [here](https://www.kaggle.com/datasets/arwani/guitar-chord-audio-collection). Save audio files in audio folder.

```
- audio/
    - A.wav
    - A#.wav
    - etc
```

## How to run

1. Install dependencies

if your computer is using GPU, run this

```bash
pip install -r requirements.txt
```

if your computer is using CPU, run this

```bash
pip install -r requirements.nogpu.txt
```

2. Run the program

open `main.ipynb` and run all cells for re training the model or open `predict.ipynb` and run all cells for predicting chord from audio file

## Contribution

### Code

1. Fork this repository
2. Clone your forked repository
3. Create new branch
4. Make changes
5. Commit and push your changes
6. Create pull request
7. Wait for review
8. Done

### Dataset

1. Record your guitar sound with standar tuning for 60s each chord
2. You must record with 2 different beat (2/4 and 4/4). 30s for each beat
3. Trim your audio file to 50s only. So the audio file doesn't contain noise from beginning and end of the audio
4. Save your recorded file with .wav format
5. Send your recorded file to [email](mailto:meliodasmeliodas224@gmail.com) with subject "Guitar Chord AI Dataset"

## Contributors

- [Aronei44](https://github.com/aronei44)

