from .stack import Stack

class MathException(Exception):
    pass

class StateError(Exception):


    def __init__(self, actual_value, previous_value):
        self.actual_value = actual_value
        self.previous_value = previous_value
        print(self)

    def __str__(self):
        if self.actual_value == "@":
                return ('A função não pode termincar com o valor "%s".' \
                %(self.previous_value))
        elif self.previous_value:
            return 'O símbolo "%s" não pode ocorrer após o símbolo "%s".'\
            %(self.actual_value, self.previous_value)
        
        return ('A função não pode começar com o valor "%s".' %(self.actual_value))

class ValueNotAccepted(Exception):


    def __init__(self, value):
        self.value = value
        print(self)

    def __str__(self):
        return ('O caracter "%s" não é aceito pelo sistema!' %(self.value))

class EmptyStack(Exception):

    def __init__(self):
        print(self)

    def __str__(self):
        return ('Algum parênteses/módulo foi aberto e não foi fechado corretamente!')

class Compiler(object):
    """
    Esta classe implementa um compilador.
    O compilador gerara ao final uma string com a funcao compilada e um dicionario de variaveis para a mesma.
    """

    state_machine = (
        #0, 1, 2, 3, 4, 5, 6,  7,  8,  9,  10
        (0,	0, 0, 0, 0, 0, 0,  0,  0,  0,  0),#0
        (2,	3, 0, 5, 6, 0, 1,  9,  0,  12, 15),#1
        (0,	0, 0, 0, 0, 0, 2,  0,  0,  0,  0),#2
        (0,	0, 0, 5, 6, 0, 3,  9,  0,  12, 15),#3
        (0,	3, 0, 5, 6, 0, 4,  9,  0,  12, 15),#4
        (2,	3, 4, 5, 0, 0, 5,  0,  11, 14, 15),#5
        (2,	3, 4, 5, 6, 7, 6,  0,  11, 14, 15),#6
        (0,	0, 0, 0, 8, 0, 7,  0,  0,  0,  0),#7
        (2,	3, 4, 5, 8, 0, 8,  0,  11, 14, 15),#8
        (2,	3, 0, 5, 6, 0, 9,  10, 0,  12, 15),#9
        (2,	3, 0, 5, 6, 0, 9,  9,  0,  12, 15),#10
        (2,	3, 4, 5, 6, 0, 11, 9,  11, 0,  15),#11
        (2,	3, 0, 5, 6, 0, 12, 9,  0,  13, 15),#12
        (2,	3, 0, 5, 6, 0, 12, 9,  0,  14, 15),#13
        (2,	3, 4, 0, 0, 0, 13, 0,  11, 0,  0),#14
        (2,	3, 4, 5, 6, 0, 5,  0,  11, 14, 0),#15
        )
    dic_lines = {
            0 : 'error',
            1 : 'start',
            2 : 'last',
            3 : 'end',
            4 : 'operator',
            5 : 'coefficient',
            6 : 'number_int',
            7 : 'point',
            8 : 'number_float',
            9 : 'parentheses_start',
            10 : 'parentheses_start',
            11 : 'parentheses_end',
            12 : 'module_start',
            13 : 'module_start',
            14 : 'module_end',
            15 : 'unknown ',
        }
    dic_columns = {
            'end' : 0,
            'signal' : 1,
            'operator' : 2,
            'coefficient' : 3,
            'number' : 4,
            'point' : 5,
            'empty' : 6,
            'parentheses_start'  : 7,
            'parentheses_end'  : 8,
            'module' : 9,
            'unknown' : 10,
        }
    dic_types = {
            'end': ('@', ),
            'signal' : ('+', '-'),
            'operator' : ('/', '*', '^'),
            'coefficient' : ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j',
                          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                          'u', 'v', 'w', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
                          'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                          'P', 'Q', 'R', 'S', 'T','U','V','W', 'X', 'Y', 'Z'),
            'number' : ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'),
            'point' : ('.', ), 
            'empty' : (' ', ''),
            'parentheses_start' : ('(', ),
            'parentheses_end' : (')', ),
            'module' : ('|', ),
            'unknown' : ('x')
        }
    final_states = (2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    stack = Stack()

    def __init__(self, function):
        """
        O metodo __init__ inicializa o compilador com base em uma string
        """
        #retirar vazios e adicionar simbolo final
        function = function.replace(' ', '') + '@'
        #atributos particulares em cada objeto
        self.lista_tokens = list() 
        self.dic_coefficients = dict()
        self.token = str()
        self.error = str()
        self.add_multiplication = False
        self.compiled_string_python = str()
        self.compiled_string_web = str()
        self.compiled_string_math = str()
        ######################################
        self.previous_state = 1
        self.previous_value = str()
        for self.value in function: #verificar o self do for
            if not self.manage_state_machine(): #caso nao tenha erro em estado
                break
            self.manage_token()
            self.manage_stack()
            self.previous_state = self.actual_state
            self.previous_value = self.value
        self.valid_function()
        self.compiler_function_python() #criar uma string para o sympy
        self.compiler_function_web() #criar uma string para a web
        self.compiler_string_math()

    def valid_function(self):
        """
        O metodo valid_function eh responsável por validar a função
        """
        try:
            if not self.stack.isEmpty():
                raise EmptyStack()
        except EmptyStack as error:
            self.error = error
        if not self.error:
            self.valid= True
            return True
        else:
            self.valid = False
            return False

    def manage_stack(self):
        """
        O metodo manage_stack gerencia a pilha responsavel por parenteses e modulos
        """
        #caso seja a abertura de parenteses
        if self.value == '(':
            self.stack.push(self.value)
        #se a pilha nao for vazia e for o fechamento de um parenteses e o topo da pilha ter um parenteses aberto
        elif not self.stack.isEmpty() and\
         self.value == ')' and self.stack.top() == '(':
            self.stack.pop()
        #caso seja modulo
        elif self.value == '|':
            if not self.stack.isEmpty() \
            and self.stack.top() == '|' \
            and (self.actual_state != 12 or self.actual_state != 13): #verifica se nao eh abertura de um modulo
                self.stack.pop()
            else:
                self.stack.push(self.value)

    def manage_state_machine(self):
        """
        O metodo manage_state_machine gerencia a maquina de estados
        A maquina de estado eh modificada a cada loop, variando de acordo com o modelo do automato implementado
        :return : retorna False caso ocorra algum erro de estado e True caso nao tenha nenhum
        """
        #determinar coluna
        self.column = None #necessario iniciar a cada nova secao
        for t in self.dic_types:
            if self.value in self.dic_types[t]:
                self.column = self.dic_columns[t]
        #excecao de coluna
        try:
            #precisa ser is None, senao dara erro no column final
            if self.column is None:
                raise ValueNotAccepted(self.value)
        except ValueNotAccepted as error:
            self.error = error
            return False
        #definir estado
        self.actual_state = self.state_machine[self.previous_state][self.column]
        return self.manage_exception_state()

    def manage_exception_state(self):
        """
        O metodo manage_exception_state eh responsavel por chamar as excecoes da classe
        As excecoes realizao o tratamento de erros e/ou a notificacao especifica do problema
        """
        #excecoes de estado
        try:
            if not self.actual_state: #estado de erro
                raise StateError(self.value, self.previous_value)

            #para numeros seguidos de variavel/incognita
            #Estados: 6 : numero_int e 8 : numero_float
            #Colunas: 3 : variavel e 10 : incognita
            elif (self.previous_state == 6 or self.previous_state == 8) and \
            (self.column == 3 or self.column == 10):
                raise MathException

            #para variavel/incognita seguidas de numero
            #Estado: 5 : variavel e 15: incognita
            #Coluna: 4 : numero
            elif (self.previous_state == 5 or self.previous_state == 15) and self.column == 4:
                raise MathException

            #para incogntas seguida de variavel ou variavel seguida de incongnita
            #Estado: 5: variavel e 15 : incognita
            #Coluna: 3 : variavel e 10 : incognita
            elif (self.previous_state == 5 and self.column == 10) or\
            (self.previous_state == 15 and self.column == 3):
                raise MathException
        except MathException:
            self.add_multiplication = not self.add_multiplication
        except StateError as error:
            self.error = error
            return False
        return True

    def manage_token(self):
        """
        O metodo manage_token gerencia os tokens
        Os tokens sao gerenciados com base na state_machine, sendo finalizados e iniciados por este metodo
        """
        #fechar token
        if self.actual_state in self.final_states \
            and self.previous_state != self.actual_state \
            and self.previous_state in self.final_states:
            self.lista_tokens.append(
                (self.dic_lines[self.previous_state], self.token)
            )
            self.token = ''
        #adicionar token por causa de excecao
        if self.add_multiplication:
            self.lista_tokens.append(('operator', '*'))
            self.add_multiplication = not self.add_multiplication
        self.token += self.value

    def compiler_function_python(self):
        """
        O metodo compiler_fuction concatena a string final da funcao e gera o dicionario de coeficientes
        Este metodo eh o responsavel final do compilador, ele ira concatenar a string da funcao e um dicionario
        para a mesma, que permite a troca dos coeficietnes pelos valores informados no dicionario para o python
        """
        if not self.error: #caso nao tenha erro
            for token in self.lista_tokens:
                value = token[1]
                if token[0] == 'module_start':
                    value = 'abs('
                elif token[0] == 'module_end':
                    value = ')'
                elif token[0] == 'operator' and value == '^':
                    value = '**'
                elif token[0] == 'coefficient':
                    value = '%(' + token[1] + ')s'
                    self.dic_coefficients[token[1]] = 1
                self.compiled_string += value

    def compiler_function_web(self):
        """
        O metodo compiler_fuction concatena a string final da funcao e gera o dicionario de coeficientes
        Este metodo eh o responsavel final do compilador, ele ira concatenar a string da funcao e um dicionario
        para a mesma, que permite a troca dos coeficietnes pelos valores informados no dicionario para o python
        """
        if not self.error: #caso nao tenha erro
            for token in self.lista_tokens:
                value = token[1]
                if token[0] == 'module_start':
                    value = 'abs('
                elif token[0] == 'module_end':
                    value = ')'
                elif token[0] == 'coefficient':
                    value = '%(' + token[1] + ')s'
                    self.dic_coefficients[token[1]] = 1
                self.compiled_string_web += value

    def compiler_string_math(self):
        """
        O metodo compiled_string_math agrega a compiled_string_math com o dic_cofficients para gerar uma string compilada no 
        padrao matematico classico
        """
        if not self.error: #caso nao tenha erro
            for token in self.lista_tokens:
                value = token[1]
                if token[0] == 'coefficient':
                    value = '%(' + token[1] + ')s'
                    self.dic_coefficients[token[1]] = 1
                self.compiled_string_math += value

if __name__ == '__main__':
    c = Compiler('(ax^|2|) + |')
    print('Validade: ', c.valid)
    print('Lista de tokens: ', c.lista_tokens)
    print('Dic', c.dic_coefficients)
    print('String: ', c.compiled_string)
    print('String: ', c.compiled_string %(c.dic_coefficients))
    print('Error: ', c.error)
