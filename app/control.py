from flask import Flask, request, render_template, redirect, url_for
from models.compiler import Compiler
from models.function import Function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('graph_function')) #deve colocar o nome da funcao nao o url

@app.route('/function', methods=['GET', 'POST'])
def graph_function():
    """"Este metodo renderiza a pagina de grafico do site"""
    dic_page = {
        'input_function': '',
        'coefficients' : dict(),
        'error': '',
        'function_graph' : '',
        'solve_real' : dict()
    }
    # se nao ter o que requisitar eh recebido None
    input_function = request.args.get('input_function')
    if input_function:
        dic_page['input_function'] = input_function
        try:
            compiler = Compiler(input_function)
        except Exception as error:
            print('\n\nControl Error: ', error)
        if compiler.valid: #se compilador eh valido
            #requisitar variveis via get, caso eles ja estejam expressos pelo usuario anteriormente
            for coefficient in compiler.dic_coefficients:
                valor = request.args.get(coefficient)
                if valor:
                    compiler.dic_coefficients[coefficient] = valor
            #criar funcao
            try:
                function = Function(compiler.compiled_string,
                                                compiler.dic_coefficients)
                if function.solve_real.is_EmptySet:
                    dic_page['solve_real'] = {}
                else:
                    dic_page['solve_real'] = function.solve_real
                dic_page['coefficients'] = function.dic_coefficients
            except Exception as error:
                print('\n\nControl Error: ', error)
                dic_page['coefficients'] = compiler.dic_coefficients
        else:
            dic_page['error'] = compiler.error
        #concatenar a string para o grafico    
        dic_page['function_graph'] = (compiler.compiled_string_web %(compiler.dic_coefficients))
    return render_template('graph_function.html', dic=dic_page)

@app.route('/linear_system', methods=['GET', 'POST'])
def graph_linear_system():
    return render_template('graph_linear_system.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html',\
     mensagem='Tivemos um erro que em breve será corrigido. Agradecemos a paciencia!')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',\
     mensagem='O URL informado não condiz com nenhuma das nossas páginas. Por favor retorne a página inicial!')

if __name__ == '__main__':
    app.run(debug=True)
