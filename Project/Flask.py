from flask import Flask
from flask import send_from_directory
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "The temperature is 24.0C and the humidity is 34.0% now."

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', 
                               mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    allowed_ip_addr = "192.168.86.56"
    app.run(host=allowed_ip_addr, port=8000, debug=True, threaded=True, use_reloader=False)

