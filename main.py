import whisper
from pydub import AudioSegment
import simpleaudio as sa
import time

file = "wonderful66.mp3"
filename = file[:-4]

# set up the model for speech to text
model = whisper.load_model("base")
# run the model and get the result
result = model.transcribe(file, verbose=False)

# convert the file to wav
audio = AudioSegment.from_mp3(file)
audio.export(filename+'.wav', format="wav")


# load the wav file for playing
wave_obj = sa.WaveObject.from_wave_file(filename+'.wav')
# play the audio
play_obj = wave_obj.play()
# get the current time
previous_time = time.time()
segments = result['segments']
while play_obj.is_playing():
    # get the time since last loop
    current_time = time.time()
    time_diff = current_time - previous_time
    for segment in segments:
        # if the time is between the segments times display the text
        if segment['start'] < time_diff < segment['end']:
            print(segment['text'])
            # now the text has been displayed, delete it
            segments.pop(0)
            break
if __name__ == '__main__':
    pass



