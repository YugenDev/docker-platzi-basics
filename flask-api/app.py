import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def getMyInfo():
    value = {
        "name": "Juan Esteban",
        "lastname": "Escobar",
        "socialMedia":
        [
            {"facebookUser": "Juan Yugen"},
            {"instagramUser": "yugoso8512"},
            {"xUser": "YugenDev"},
            {"linkedin": "YugenDev"},
            {"githubUser": "YugenDev"}
        ],
        "blog": "https://yugendev.netlify.app/",
        "author": "Juan Esteban Escobar"
    }
    return json.dumps(value)