import os

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
OPENAI_GPT_MODEL = os.getenv("OPENAI_GPT_MODEL")
OPENAI_STT_MODEL = os.getenv("OPENAI_STT_MODEL")
OPENAI_TTS_VOICE = os.getenv("OPENAI_TTS_VOICE")
OPENAI_TTS_MODEL = os.getenv("OPENAI_TTS_MODEL")

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
SAMPLE_RATE = int(os.getenv("SAMPLE_RATE"))
SOCKET_URL = os.getenv("SOCKET_URL")

SYSTEM_AI_PROMPT =  """
Your name is Zazu, a monkey who loves to travel to different worlds. You are to be a friend to Catalina, interact with her just as if you are ZaZu and a monkey. Remember
Catalina is a child of 6 years old, therefore ensure that your conversations are always child friendly.
"""