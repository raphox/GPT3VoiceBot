https://www.youtube.com/watch?v=74WPFGAADt4

## Tips

* Generate a API key [here](https://beta.openai.com/account/api-keys) and update the `api_key.py`.

* If you are using Mac, you need to install these dependencies:

  ```
  brew install portaudio
  ```

* Select a language on:

  ```python
  # gpt3Bot.py line 26
  user_input = r.recognize_google(audio,language='pt-BR')

  # gpt3Bot.py line 42
  engine.setProperty('voice', 'com.apple.voice.compact.pt-BR.Luciana')
  ```

* Could you use the `pyttsx3_languages.py` to get the list of available language ids in your system.