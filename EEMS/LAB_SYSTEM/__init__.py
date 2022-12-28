from flask import Flask
app = Flask(__name__)
app.config.from_object('LAB_SYSTEM.config')
import LAB_SYSTEM.views