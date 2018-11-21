from flask import request, render_template, redirect, url_for, abort
from app import app
from app.models.compiler import Compiler, InvalidCompiler
from app.models.function import Function
from app.models.order_dict import OrderDict
from app.models.models import Question, Answer

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
        print(compiler.dic_coefficients.sort_key())
        return render_template('graph_function.html', dic=dic_page)

@app.route('/question', methods=['POST', 'GET'])
def question():
    try:
        id = request.args.get('id')
    except Exception as identifier:
        print("\n\n Question error: %s \n" %(identifier))
        return abort(404)
    else:
        q = Question(
            text='Lorem ipsum a aenean gravida torquent platea consequat cursus orci commodo ut, nibh vehicula sollicitudin elit rutrum platea pulvinar aenean commodo varius tortor, per risus neque curabitur eros ad nulla netus pulvinar arcu. metus curabitur placerat et ultricies per sem volutpat, libero sollicitudin ornare sagittis taciti leo, dolor adipiscing bibendum tincidunt nibh molestie. maecenas nisl elit ut consequat felis enim nam dictumst nulla vestibulum, dictum cursus consectetur sapien justo adipiscing eget lorem vulputate mattis dictumst, lobortis porta ut libero etiam gravida porta euismod quis. phasellus turpis aenean consequat euismod molestie vel curae in, suscipit porttitor interdum nulla velit dui posuere faucibus, diam tempor hac mi ad euismod diam.',
            graph_function='1*x^3+1*x^2+1*x+1',
            options=[
                Answer('1', 'a', 'Lorem ipsum per accumsan aliquam maecenas, diam vitae ad ornare.'),
                Answer('2', 'b', 'Lorem ipsum per accumsan aliquam maecenas, diam vitae ad ornare.'),
                Answer('3', 'c', 'Lorem ipsum per accumsan aliquam maecenas, diam vitae ad ornare.'),
                Answer('4', 'd', 'Lorem ipsum per accumsan aliquam maecenas, diam vitae ad ornare.'),
                Answer('5', 'e', 'Lorem ipsum per accumsan aliquam maecenas, diam vitae ad ornare.')
                ],
            answer='Lorem ipsum per accumsan aliquam maecenas, diam vitae ad ornare. ',
            name='teste',
            img=None,
            id=5,

        )
        return render_template('question.html', question=q)

@app.route('/about')
def about():
    return render_template('about.html')
