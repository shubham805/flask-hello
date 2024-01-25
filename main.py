# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask
from structlog import get_logger

app = Flask(__name__)

log = get_logger()


@app.route("/")
def hello_world():
    log.info("Info log")
    log.debug("Debug log")
    log.error("Error Log")
    print("Console write")
    return "<p>Hello, World!</p>"

app.run(host='0.0.0.0', port=5000)
