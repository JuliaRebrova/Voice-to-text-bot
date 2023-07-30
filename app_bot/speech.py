import speech_recognition as sr


r = sr.Recognizer()


def recognize(filepath: str) -> str:
    sample_audio = sr.AudioFile(filepath)
    with sample_audio as audio_file:
        # r.adjust_for_ambient_noise(audio_file)
        audio_content = r.record(audio_file)
    text = r.recognize_google(audio_data=audio_content, language="ru-RU")
    return text
