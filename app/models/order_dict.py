from collections import OrderedDict

class OrderDict(OrderedDict):

    """A classe OrderDict cria uma classe baseado no OrderedDict da biblioteca collections do Python """

    def add(self, key, value):
        """O método add adiciona um novo itens a classe"""

        add = OrderedDict([(key, value)])
        self.update(add)

    def sort_key(self):
        """ O método sort ordena o OrderedDict com base na key """
        order_dic = self.copy()
        order_dic_keys = sorted((order_dic.keys()))

        self.clear() #limpa o dicionario

        for key in order_dic_keys:
            self.add(key, order_dic[key])

if __name__ == "__main__":
    
    dic = MyOrderedDict({
        'b' : 7,
        'e' : 9,
        'a' : 10
    })
    print("Teste order_dict")
    print("Ordenando o dic: %s" %(dic))
    dic.sort_key()
    print("Resultado: ", dic)

    print()
    dic = MyOrderedDict()
    print("Ordenando o dic: %s" %(dic))
    dic.sort_key()
    print("Resultado: ", dic)

    print()
    dic = MyOrderedDict({
        'gdfhb' : 7,
        'sahd' : 9,
        'sahe' : 10
    })
    print("Teste order_dict")
    print("Ordenando o dic: %s" %(dic))
    dic.sort_key()
    print("Resultado: ", dic)


    print()
    dic = MyOrderedDict({
        'baaasa' : 7,
        'bbaaa' : 9,
        'peso' : 10
    })
    print("Teste order_dict")
    print("Ordenando o dic: %s" %(dic))
    dic.sort_key()
    print("Resultado: ", dic)


    print()
    dic = MyOrderedDict({
        'b' : 7,
        'e' : 9,
        'a' : 10
    })
    print("Teste order_dict")
    print("Ordenando o dic: %s" %(dic))
    dic.sort_key()
    print("Resultado: ", dic)