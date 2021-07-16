import datetime
import re
import socket
import urllib
from urllib import parse

from flask import Flask, request, redirect

from config import settings

# General Constants
TOKEN_ENDPOINT = "https://oauth.nicovideo.jp/oauth2/token"
COMMON_HTTP_HEADERS = {"User-Agent": "Hakumai/0.0.1"}
COMMON_400_RESPONSE = "🙈", 400

# Debug Global Vars
LAUNCH_DATETIME = datetime.datetime.today().isoformat(timespec='seconds')
HOST_NAME = socket.gethostname()
IP_ADDRESS = socket.gethostbyname(HOST_NAME)
MASKED_IP_ADDRESS = re.sub(r"\.\d+\.\d+\.", ".xx.xx.", IP_ADDRESS)
IS_DEVELOPMENT = False

app = Flask(__name__)


@app.route('/')
def show_top_page():
    return f"🥺 < {LAUNCH_DATETIME} / {MASKED_IP_ADDRESS}"


@app.route('/oauth-callback')
def oauth_callback():
    code = request.args.get('code')
    if code is None:
        return COMMON_400_RESPONSE
    params = {
        "grant_type": "authorization_code",
        "code": code,
    }
    if IS_DEVELOPMENT:
        params["redirect_uri"] = settings.DEV_REDIRECT_URI
    req = urllib.request.Request(
        TOKEN_ENDPOINT,
        data=__make_request_body(params),
        method="POST",
        headers=COMMON_HTTP_HEADERS,
    )
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return redirect(f"hakumai://?response={body.decode('utf-8')}")


@app.route('/api/v1/refresh-token', methods=["POST"])
def refresh_token():
    token = request.form["refresh_token"]
    if token is None:
        return COMMON_400_RESPONSE
    # print(token)
    params = {
        "grant_type": "refresh_token",
        "refresh_token": token,
    }
    req = urllib.request.Request(
        TOKEN_ENDPOINT,
        data=__make_request_body(params),
        method="POST",
        headers=COMMON_HTTP_HEADERS,
    )
    with urllib.request.urlopen(req) as res:
        body = res.read()
    # print(body.decode('utf-8'))
    return f"{body.decode('utf-8')}"


def __make_request_body(parameters):
    body = dict(parameters, **{
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
    })
    return parse.urlencode(body).encode()
