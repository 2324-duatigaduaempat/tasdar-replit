from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return 'TAS.DAR Plan-Z1 running.'
