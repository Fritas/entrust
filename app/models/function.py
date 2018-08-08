from sympy import Lambda, solve, Symbol
from models.compiler import Compiler

class Function(object):
    """
    A classe Fuction eh responsavel por representar uma funcao matematica e seus atributos graficos
    """


    def __init__(self, string='', dic_variables={}, pixels=1080, begin=0, end=0):
        """
        O metodo __init__ inicia as variaveis
        """
        self.string = string
        self.dic_variables = dic_variables
        self.pixels = pixels
        self.begin = begin
        self.end = end
        self.coordinates = [[], []]
        self.solve = []
        self.solve_real = []
        #if self.string:
        #    self.update(dic_variables)

    def define_begin_and_end(self):
        """ O metodo define begind e end caso o usuario nao informe """
        #se ambos os valores forem zero
        if not self.begin and not self.end:
            if len(self.solve) > 1:
                self.begin, self.end = self.solve[0] - 1, self.solve[-1] + 1
            elif len(self.solve) == 1 and self.solve[0] != 0:
                self.begin = - (self.solve[0] * 0.1)
                self.end = self.solve[0] * 0.1
            else:
                self.begin, self.end = -1, 1

        #o begin nunca pode ser maior que o final
        if self.begin > self.end:
            self.begin, self.end = self.end, self.begin

    def generate_coordinates(self):
        """ O metodo gera as coordenadas para o grafico """
        addtion = abs(self.begin - self.end) / self.pixels
        count = 0
        limit = self.pixels * 2
        x = self.begin
        self.coordinates = [[], []]
        #enquanto o grafico nao for desenhado do begin ao end
        while x <= self.end:
            #se a quantidade de loops excede o limite ---> interromper
            if count >= limit:
                break
            #determinar y
            y = self.fun_lamb(x)
            #se os valores forem reais adicionar, os testes ints e float se da pelo fato de atributos int e flaot nao ter o atributo is_real
            if type(y) is int or type(y) is float or y.is_real:
                self.coordinates[0].append(x)
                self.coordinates[1].append(y)
            #adicionar addtion ao x
            x += addtion

    def solve_function(self):
        """ O metodo determina a solucao da funcao """
        #http://docs.sympy.org/latest/modules/solvers/solvers.html
        #http://docs.sympy.org/latest/modules/solvers/solveset.html
        try:
            self.solve = solve(self.string %(self.dic_variables),
                            x = Symbol('x'))
        except Exception as error:
            print('Error: ', error)
        for root in self.solve:
            if root.is_real:
                self.solve_real.append(root)

    def update(self, new_dic_variables):
        """O metodo atualiza os dados da funcao com base em novas variaveis e cria o objeto lambda"""
        self.dic_variables = new_dic_variables
        self.define_begin_and_end()
        self.fun_lamb = Lambda(Symbol('x'), self.string %(self.dic_variables))
        self.solve_function()
        self.generate_coordinates()

    def get_string(self):
        return self.string %(self.dic_variables)

    def __str__(self):
        return self.string %(self.dic_variables)

if __name__ == '__main__':
    f = Function()
    c = Compiler('x*|a|')
    if c.valid:
        f = Function(
            string=c.string,
            dic_variables=c.dic_variables,
            pixels=1080, begin=0, end=0
            )
        print('Solucao: ', f.solve)
        print('Solucao real: ', f.solve_real)
        print('Coordendas: ', f.coordinates)
        #print(f.coordinates[0][0], f.coordinates[0][-1])
