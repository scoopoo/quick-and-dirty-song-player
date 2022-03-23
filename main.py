from pydub import AudioSegment
from pydub.playback import play

a=input("insert song path here")
song = AudioSegment.from_mp3(a)
play(song)



