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
        'function' : Function(),
        'error': '',
        'function_graph' : '',
    }
    # se nao ter o que requisitar eh recebido None
    input_function = request.args.get('input_function')

    if input_function:
        dic_page['input_function'] = input_function
        try:
            compiler = Compiler(input_function)
        except Exception as error:
            print('\n\nError: ', error)
        if compiler.valid: #se compilador eh valido
            #requisitar variveis via get, caso eles ja estejam expressos pelo usuario anteriormente
            for variable in compiler.dic_variables:
                valor = request.args.get(variable)
                if valor:
                    compiler.dic_variables[variable] = valor
            #criar funcao
            try:
                dic_page['function'] = Function(compiler.string,
                                                compiler.dic_variables)
            except Exception as error:
                print('Error: ', error)
        else:
            dic_page['error'] = compiler.error
        #concatenar a string para o grafico    
        dic_page['function_graph'] = (compiler.compiler_function_web() %(compiler.dic_variables))
        print(dic_page['function'].solve)
    return render_template('graph_function.html', dic=dic_page)

@app.route('/linear_system', methods=['GET', 'POST'])
def graph_linear_system():
    return render_template('graph_linear_system.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)#, host="191.52.7.33")
