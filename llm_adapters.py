from openai import OpenAI
import settings

class OpenAILLM:
    def __init__(self):
        self.llm = OpenAI()
        self.messages = [
            ("system",settings.SYSTEM_AI_PROMPT)
        ]

    def invoke(self, message):
        self.messages.append(("user", message))
        messages = self.messages.copy()

        chat_completion = self.llm.chat.completions.create(
            model= settings.OPENAI_GPT_MODEL,
            messages=[{"role": m[0], "content": m[1]} for m in messages]
        )
        
        response = chat_completion.choices[0].message.content
        self.messages.append(("assistant", response))

        return response

    def text_to_audio(self, text, audio_file_path):
        response = self.llm.audio.speech.create(
            model=settings.OPENAI_TTS_MODEL,
            voice=settings.OPENAI_TTS_VOICE,
            input=text
        )

        response.stream_to_file(audio_file_path)