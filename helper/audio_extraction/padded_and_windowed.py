import librosa
import numpy as np

def extract_windowed_features(audio_list, classes, segment_duration=1.5, window_duration=1.0, test_rate=0):
    """
    Extracts windowed features from a list of audio files.
    :param audio_list: List of audio files to process
    :param classes: Dictionary of class names and their corresponding numeric value
    :param segment_duration: Duration in seconds of each segment
    :param window_duration: Duration in seconds of each window
    :param test_rate: Rate of test data
    :return: List of windowed features and corresponding labels

    example:

    train_data, test_data = extract_windowed_features(audio_list, classes, segment_duration=1.5, window_duration=1.0, test_rate=0.2)
    """
    windowed_features = []
    test_windowed_features = []

    for audio_file in audio_list:
        if not audio_file.endswith('.wav'):
            continue
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

            # count the number of test data
            test_count = (len(y) - segment_samples + 1) // (int(sr * window_duration))
            test_start = test_count - int(test_count * test_rate)

            # split the data into train and test
            if start >= test_start * int(sr * window_duration):
                test_windowed_features.append([
                    chroma_vector,
                    classes[label]
                ])
            else:
                # Append the dictionary to the list
                windowed_features.append([
                    chroma_vector,
                    classes[label]
                ])

    print("windowed_features: ", len(windowed_features))
    print("test_windowed_features: ", len(test_windowed_features))
    return windowed_features, test_windowed_features