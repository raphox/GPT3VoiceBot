import openai
import pyttsx3
import speech_recognition as sr
from api_key import API_KEY


openai.api_key = API_KEY

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()

conversation = ""
user_name = "You"
bot_name = "Jarvis"

while True:
    with mic as source:
        print("\nlistening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source, phrase_time_limit=3)
    print("no longer listening.\n")

    try:
        user_input = r.recognize_google(audio,language='pt-BR')
    except:
        continue

    prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "

    conversation += prompt  # allows for context

    # fetch response from open AI api
    response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, max_tokens=100)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

    conversation += response_str + "\n"
    print(response_str)

    engine.setProperty('voice', 'com.apple.voice.compact.pt-BR.Luciana')
    engine.say(response_str)
    engine.runAndWait()
