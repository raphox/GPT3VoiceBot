import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    if 'pt_BR' in voice.languages:
        print(voice, voice.id)
        engine.setProperty('voice', voice.id)
        engine.say("Hello, world.")
        engine.runAndWait()
        engine.stop()