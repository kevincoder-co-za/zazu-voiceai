from flask import Flask, render_template
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from audio_handlers import AudioHandler
from llm_adapters import OpenAILLM
import settings

app = Flask(__name__)
sockets = Sockets(app)


@app.route("/dialer")
def dialer():
    """
    Will return an HTML template softphone dialer. A very basic HTML page.
    """
    return render_template("dialer.html", 
        sample_rate = settings.SAMPLE_RATE,
        socket_url = settings.SOCKET_URL
    )

@sockets.route("/websocket/stream")
def audio_stream(ws):
    """
    The actual websocket to stream the WebRTC session.
    """
    audio_handler = None
    llm = None

    while not ws.closed:
        message = ws.receive()

        if message is None:
            continue
        if isinstance(message, str):
            if "start call" in message:
                print("Call started", flush=True)
                llm = OpenAILLM()
                audio_handler = AudioHandler(llm, ws)
            elif "end call" in message and audio_handler:
                audio_handler.stop()
                llm = None
    
        elif isinstance(message, bytes) or isinstance(message, bytearray):
            audio_handler.stream(bytes(message))

if __name__ == "__main__":
    WEBSOCKET_PORT = 5000
    server = pywsgi.WSGIServer(("", WEBSOCKET_PORT), app, handler_class=WebSocketHandler)
    print(f"Server listening on ws://0.0.0.0:{WEBSOCKET_PORT}")
    server.serve_forever()
