from pydub import AudioSegment

sound = AudioSegment.from_mp3("test.mp3")

# sound._data is a bytestring
raw_data = sound._data