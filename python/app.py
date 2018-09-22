CLIENT_ID = 'b17c56e6-f400-42c7-81a6-346716ecbc55'
CLIENT_SECRET = '2ee5b1f9-97ec-44cf-9411-61061c9c3ce2'

import smartcar
from flask import Flask, request, jsonify

app = Flask(__name__)

client = smartcar.AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='http://localhost:5000/callback',
    scope=['read_vehicle_info', 'read_location', 'read_odometer', 'control_security']
)
# control_security allows locking and unlocking
# there's also control_security:unlock and control_security:lock

@app.route('/', methods=['GET'])
def index():
    auth_url = client.get_auth_url(force=True)
    return '''
        <h1>Hello, Hackbright!</h1>
        <a href=%s>
          <button>Connect Car</button>
        </a>
    ''' % auth_url

@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    access = client.exchange_code(code)
    
    print(access)

    return jsonify(access)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
