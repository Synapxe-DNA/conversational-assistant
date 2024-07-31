import threading

from push_stream_writer import push_stream_writer
from speech_recognition import setup_speech_recognizer


def speech_recognition_with_push_stream(filename):
    """Recognizes speech from a custom audio source using a push audio stream."""
    stream, speech_recognizer, recognition_done, all_results = setup_speech_recognizer()

    # Start push stream writer thread
    push_stream_writer_thread = threading.Thread(
        target=push_stream_writer, args=[stream, filename]
    )
    push_stream_writer_thread.start()

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    recognition_done.wait()
    # Stop recognition and clean up
    speech_recognizer.stop_continuous_recognition()
    push_stream_writer_thread.join()

    return all_results


if __name__ == "__main__":
    filename = "./speech-to-text/samples/sg_lhl_10s_chinese.wav"
    results = speech_recognition_with_push_stream(filename)
    print(results)
