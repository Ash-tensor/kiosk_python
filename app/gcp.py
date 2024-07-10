from google.cloud import speech
import io

client = speech.SpeechClient()

# 음성 파일을 로드합니다.
with io.open("path/to/your/audiofile.wav", "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
    enable_automatic_punctuation=True,
    enable_word_time_offsets=True
)

# 음성 인식 요청을 보냅니다.
response = client.recognize(config=config, audio=audio)

# 결과를 출력합니다.
for result in response.results:
    alternative = result.alternatives[0]
    print(f"Transcript: {alternative.transcript}")
    print(f"Confidence: {alternative.confidence}")
    for word in alternative.words:
        print(f"Word: {word.word}, Start Time: {word.start_time.total_seconds()}, End Time: {word.end_time.total_seconds()}")
