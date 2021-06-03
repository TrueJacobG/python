from gtts import gTTS
from playsound import playsound

audio = "speach.mp3"
language = "en"
t = "What's up"
sp = gTTS(text=t, lang=language, slow=False)
sp.save(audio)
playsound(audio)

# thats cool
