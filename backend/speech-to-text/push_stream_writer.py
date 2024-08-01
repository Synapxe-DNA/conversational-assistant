def push_stream_writer(stream, filename):
    """Simulates an audio source by pushing audio data from a WAV file into the stream."""
    with open(filename, "rb") as audio_file:
        wav_header_size = 44  # Standard WAV header size
        audio_file.read(wav_header_size)  # Skip the WAV header
        audio_data = audio_file.read()
        stream.write(audio_data)
        stream.close()
