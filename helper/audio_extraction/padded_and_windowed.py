import librosa
import numpy as np
def extract_windowed_features(audio_list, classes, segment_duration=1.5, window_duration=1.0):
    windowed_features = []

    for audio_file in audio_list:
        # Load an audio file
        y, sr = librosa.load(audio_file, mono=True)  # Load audio in mono

        # Extract the label (the part of the file name before the extension)
        label = audio_file.split('/')[-1].split('.')[0].split('\\')[-1]

        # Define the number of samples per segment and window
        segment_samples = int(sr * segment_duration)
        window_samples = int(sr * window_duration)

        # Create a Hanning window
        window = np.hanning(window_samples)

        # Split the audio into overlapping segments
        for start in range(0, len(y) - segment_samples + 1, int(sr * window_duration)):
            end = start + segment_samples
            segment = y[start:end]

            # Apply the window to the center of each segment
            window_start = (segment_samples - window_samples) // 2
            window_end = window_start + window_samples
            windowed_segment = segment[window_start:window_end] * window

            # Extract chroma feature using chroma_cqt
            chroma = librosa.feature.chroma_cqt(y=windowed_segment, sr=sr)

            # Flatten the chroma matrix to obtain a feature vector
            chroma_vector = chroma.flatten()

            # Append the dictionary to the list
            windowed_features.append([
                chroma_vector,
                classes[label]
            ])

    return windowed_features