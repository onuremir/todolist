import os
import logging
from config import Config

from flask import Flask, render_template


app = Flask(__name__, template_folder=Config._TEMPLATE_FOLDER, static_folder=Config._STATIC_FOLDER)

logging.warning("VIEWDIR " + app.template_folder)
logging.warning("VIEWDIR " + app.static_folder)

@app.route('/')
def hello_world():
    title = "Add Task"
    data = "ben datatyım :)))"
    return render_template("addtask.html", title=title, data=data)

