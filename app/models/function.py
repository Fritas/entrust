#from sympy import Lambda, solve, Symbol
from sympy import Lambda,  Symbol, S, solveset
from sympy.abc import x

class Function(object):
    """
    A classe Fuction eh responsavel por representar uma funcao matematica e seus atributos graficos
    """


    def __init__(self, string_function='', dic_coefficients={}):
        """
        O metodo __init__ inicia as variaveis
        """
        self.string_function = string_function
        self.dic_coefficients = dic_coefficients
        self.solve = None
        self.solve_real = None
        self.fun_lamb = None
        if self.string_function:
            self.update(dic_coefficients)

    def solve_function(self):
        """
        O metodo determina a solucao da funcao
        """
        #http://docs.sympy.org/latest/modules/solvers/solvers.html
        #http://docs.sympy.org/latest/modules/solvers/solveset.html
        try:
            funcao = self.string_function %(self.dic_coefficients)
            self.solve = solveset(funcao, x)
            self.solve_real = solveset(funcao, x, domain=S.Reals)
        except Exception as error:
            print('Function Error: ', error)

    def update(self, new_dic_coefficients, generate_coordinates=False):
        """
        O metodo atualiza os dados da funcao com base em novas variaveis e cria o objeto lambda
        """
        self.dic_coefficients = new_dic_coefficients
        self.fun_lamb = Lambda(Symbol('x'), self.string_function %(self.dic_coefficients))
        self.solve_function()

    def get_string(self):
        return self.string_function %(self.dic_coefficients)

    def __str__(self):
        return self.string_function %(self.dic_coefficients)

if __name__ == "__main__":
    f = Function('x**2 - 1')
    print(f.solve_real.__str__())
    print(type(f.solve_real))
