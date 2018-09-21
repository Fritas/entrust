from flask import Flask, request, render_template, redirect, url_for
from models.compiler import Compiler, InvalidCompiler
from models.function import Function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('graph_function')) 
    #deve colocar o nome da funcao nao o url

@app.route('/function', methods=['GET', 'POST'])
def graph_function():
    """
        Este metodo renderiza a pagina de grafico do site
    """
    dic_page = {
        'input_function': str(),
        'coefficients' : dict(),
        'error': str(),
        'function_graph' : str(),
        'function_math' : str(),
        'solve_real' : dict(),
    }
    # se nao ter o que requisitar eh recebido None
    try:
        input_function = request.args.get('input_function')
    except Exception as identifier:
        print("\n\nControl Error: ", identifier)
    else:
        if input_function:
            dic_page['input_function'] = input_function
            try:
                compiler = Compiler(input_function)
                if not compiler.valid:
                    raise InvalidCompiler
            except InvalidCompiler as identifier:
                print("\nControl Error: ", identifier)
                dic_page['error'] = compiler.error
            except Exception as identifier:
                print("\n\nControl Error: ", identifier)
            else:
                #concatenar a string para o grafico 
                dic_page['function_graph'] = (compiler.compiled_string_web %(compiler.dic_coefficients))
                dic_page['function_math'] = (compiler.compiled_string_math %(compiler.dic_coefficients))
                #requisitar variveis via get, caso eles ja estejam expressos pelo usuario anteriormente
                for coefficient in compiler.dic_coefficients:
                    valor = request.args.get(coefficient)
                    if valor:
                        compiler.dic_coefficients[coefficient] = valor
                #criar funcao
                try:
                    function = Function(compiler.compiled_string_python,
                                                    compiler.dic_coefficients)
                    print(function.solve_real)
                except Exception as identifier:
                    print('\n\nControl Error: ', identifier)
                else: #realizar caso não aja erros na criacao da function
                    if function.solve_real.is_EmptySet:
                        dic_page['solve_real'] = {}
                    else:
                        dic_page['solve_real'] = function.solve_real
            finally:
                dic_page['coefficients'] = compiler.dic_coefficients
    finally: #em todos os casos deve ser renderizado a pagina function
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
