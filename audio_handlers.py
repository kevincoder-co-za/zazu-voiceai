import os
import uuid
import settings
import assemblyai as aai
import ffmpeg

aai.settings.api_key = settings.ASSEMBLYAI_API_KEY

class AudioHandler(aai.RealtimeTranscriber):
    def __init__(self, llm, ws):
        super().__init__(
            on_data=self.on_data,
            sample_rate=settings.SAMPLE_RATE,
            on_error=lambda x : print(x, flush=True),
            disable_partial_transcripts=True
        )
        self.llm = llm
        self.ws = ws
        self.connect()

    def stop(self):
        self.close()

    def on_data(self, transcript: aai.RealtimeTranscript):
       if isinstance(transcript, aai.RealtimeFinalTranscript) and transcript.text:
            response = self.llm.invoke(transcript.text)
            if response != "":
                self.respond_to_user_prompt(response)
        
    def respond_to_user_prompt(self, transcript):
        tmp_id = str(uuid.uuid4())
        tmp_file = f"/tmp/_{tmp_id}.mp3"
        cartoonified_version = f"/tmp/modified_{tmp_id}.mp3"

        self.llm.text_to_audio(transcript, tmp_file)        
        
        ffmpeg.input(tmp_file).filter('asetrate', 33050).output(cartoonified_version).run()

        audio_data = None
        
        with open(cartoonified_version, "rb") as f:
            audio_data = f.read()

        if os.path.exists(tmp_file):
            os.remove(tmp_file)
        if os.path.exists(cartoonified_version):
            os.remove(cartoonified_version)
    
        if audio_data:
            self.ws.send(audio_data)