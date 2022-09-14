import torch
import sounddevice as sd
import time

device = torch.device('cpu')
sample_rate = 48000   

lang = 'ru'
model_id = 'ru_v3'

speaker = 'baya'
put_accent = True
put_yo =True

def speak(text):

	model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
               model='silero_tts',  
               language=lang,
			   speaker=model_id)

	model.to(device)
	audio = model.apply_tts(text=text,
						speaker=speaker,
						sample_rate=sample_rate,
						put_accent=put_accent,
						put_yo=put_yo)
	sd.play(audio, sample_rate)
	time.sleep(len(audio) / sample_rate)
	sd.stop