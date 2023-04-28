import os
from flask import Flask, abort, request, session
from authlib.integrations.flask_client import OAuth
from authlib.integrations.requests_client import OAuth2Session
from authlib.jose import jwt
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
@app.route('/')
def hello():
    return f'Hello from Flask!'


@app.route('/login_with_ekyc')
def login_with_ekyc():
    client_id = os.getenv("EKYC_CLIENT_ID")
    client_secret = os.getenv("EKYC_CLIENT_SECRET")
    scope = 'openid'
    token_endpoint = 'http://localhost:5004/oauth/token'

    client = OAuth2Session(client_id, client_secret,
                           scope=scope,
                           state=app.secret_key)
    
    token = client.fetch_token(
        token_endpoint,
        authorization_response=f"localost:5000?code={request.args['code']}&state={app.secret_key}",
        grant_type="authorization_code")

    user_info = jwt.decode(token['id_token'], "openid-ekyc-secret")
    user_info.validate()
    token["user_info"] = user_info
    return {"token": token}, 200


@app.route("/callback")
def open_id_callback():
    return {
        "code": request.args["code"]
    }, 200
