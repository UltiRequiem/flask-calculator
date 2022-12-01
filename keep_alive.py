from flask import Flask
from threading import Thread

app = Flask("")


def run():
    app.run(host="0.0.0.0", port=80)


def keep_alive():
    t = Thread(target=run)
    t.start()
