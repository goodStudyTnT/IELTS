from gtts import gTTS
from playsound import playsound

# Enter the text you want to convert to speech
# text = "Hello, how are you?"
text = """
ability"""

# Choose the language for the speech (e.g. 'en' for English)
language = 'en'

# Create a gTTS object and specify the language
tts = gTTS(text=text, lang=language)

# Save the speech as an mp3 file
tts.save('speech.mp3')

# Play the mp3 file
playsound('speech.mp3')