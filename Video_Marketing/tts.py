from gtts import gTTS

# Text you want to convert to speech
text = "Hello, this is a text-to-speech conversion example we can use this Vortex."

# Create a gTTS object
tts = gTTS(text)

# Save the audio as an audio file
tts.save("output.mp3")

# Optionally, play the generated speech
import os
os.system("mpg321 output.mp3")  # This command may vary based on your system
