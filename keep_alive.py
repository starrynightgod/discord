from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
	return '𝑺𝒕𝒂𝒓𝒓𝒚𝒏𝒊𝒈𝒉𝒕 𝒔𝒂𝒌𝒖𝒓𝒂 𝒊𝒔 𝒐𝒏𝒍𝒊𝒏𝒆 !'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()