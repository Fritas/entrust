from flask import Flask
from app import app

@app.route('/teste')
def teste():
    return render_template("layout.html")