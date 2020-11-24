import os
from urllib import parse

import requests
from dotenv import load_dotenv, find_dotenv
from flask import Flask, redirect, jsonify, request

ZOOM_OAUTH_AUTHORIZE_API = 'https://zoom.us/oauth/authorize?response_type=code'

ZOOM_TOKEN_API = 'https://zoom.us/oauth/token?grant_type=authorization_code'

load_dotenv(find_dotenv())

app = Flask(__name__)

PORT = 4000


@app.route('/')
def get_token():
    try:
        if request.args.get('code'):
            code = request.args.get('code')
            redirect_url = os.environ["redirectURL"]

            url = ZOOM_TOKEN_API + '&code=' + code + '&redirect_uri=' + parse.quote_plus(redirect_url)

            response = requests.post(url=url, auth=(os.environ.get("clientID"), os.environ.get('clientSecret')))
            if response.status_code == 200:
                response_json = response.json()
                refresh_token_ = response_json['refresh_token']
                print(refresh_token_)
                return jsonify("refresh token saved")

            else:
                print("get auth code failed")
                response = app.response_class(status=500)
                return response
        else:
            # redirecting
            print("redirecting to authorize app")
            return redirect(location=ZOOM_OAUTH_AUTHORIZE_API + '&client_id=' + os.environ.get(
                "clientID") + '&redirect_uri=' + os.environ["redirectURL"])
    except Exception as e:
        print(e.__str__())
        response = app.response_class(status=500)
        return response


if __name__ == '__main__':
    app.run(port=PORT)
