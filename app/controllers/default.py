from flask import request, render_template, redirect, url_for, abort
from app import app, db
from app.models.compiler import Compiler, InvalidCompiler
from app.models.function import Function
from app.models.order_dict import OrderDict

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
        'coefficients' : OrderDict(),
        'error': str(),
        'function_graph' : str(),
        'function_math' : str(),
        'solve_real' : dict(),
    }
    # se nao ter o que requisitar eh recebido None
    try:
        input_function = request.args.get('input_function')
        if not input_function:
            raise Exception("Função vazia!")
    except Exception as identifier:
        print("\n\nControl Error: %s \n" %(identifier))
    else:
        dic_page['input_function'] = input_function
        try:
            compiler = Compiler(input_function)
            if not compiler.valid_function():
                raise InvalidCompiler()
        except InvalidCompiler as identifier:
            print("\n\n Control error: %s \n" %(identifier))
            dic_page['error'] = compiler.error
            print(dic_page['error'])
        except Exception as identifier:
            print("\n\n Control error: %s \n" %(identifier))
        else:
            #requisitar coeficientes via get, caso eles ja estejam expressos pelo usuario anteriormente
            for coefficient in compiler.dic_coefficients:
                valor = request.args.get(coefficient)
                if valor:
                    compiler.dic_coefficients[coefficient] = valor
            #a funcao sorted ordena o dicionario de forma alfabetica | o método sort_key ordenada o dicionario
            print('Dic coeficientes: ', compiler.dic_coefficients)
            dic_page['coefficients'] = compiler.dic_coefficients.sort_key()
            print('Dic coeficientes: ', compiler.dic_coefficients)
            #concatenar a string para o grafico
            dic_page['function_graph'] = (compiler.compiler_function_web() %(compiler.dic_coefficients))
            dic_page['function_math'] = (compiler.compiler_fucntion_math() %(compiler.dic_coefficients))
            #criar funcao
            try:
                function = Function(compiler.compiler_function_python(), compiler.dic_coefficients)
            except Exception as identifier:
                print("\n\n Control error: %s \n" %(identifier))
            else:
                dic_page['solve_real'] = function.get_solve()
    finally:
        return render_template('graph_function.html', dic=dic_page)


@app.route('/about')
def about():
    return render_template('about.html')
