"""
"""

from flask import render_template

from app import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',\
     mensagem='O URL informado não condiz com nenhuma das nossas páginas. Por favor retorne a página inicial!')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html',\
     mensagem='Tivemos um erro que em breve será corrigido. Agradecemos a paciencia!')
