# ZaZu Voice AI

A fun project to experiment with voice AI, and amuse my 6 year old. It's not intended for production use and requires a bit of cleanup, but feel free to use this code however you wish. I also wrote a detailed blog article explaining this project further [here](https://kevincoder.co.za/how-i-used-voice-ai-to-bring-imaginary-characters-to-life).

## What is ZaZu voice AI?
This tool emulates a cartoon character, allowing kids to interact with AI in a safe and fun way. The AI is prompted to portray a monkey character named ZaZu (my own fictional character).

Using WebRTC, we stream audio from the browser to a WebSocket server written in Python.

The socket server will then stream the audio to AssemblyAI for transcription purposes and pass that transcription to OpenAI's GPT4o-mini model to generate a relevant response.

Once a response is returned, we use OpenAI's TTS model to convert the text to audio, and finally, we use FFMPEG to tweak the audio a bit to so that it sounds more like a cartoon character.


## How to install and run?
Firstly, copy "example.env" to ".env" and change the environment variables accordingly. You will need API keys for both OpenAI and Assembly AI.

Next:
```
pip install -r requirements.txt
bash serve.sh
```
If you add the environment variables to your system, you don't need "bash serve.sh" and can simply just run:
```
python server.py
```
After running the above, you can access the WebRTC phone here:
http://127.0.0.1:5000/dialer
