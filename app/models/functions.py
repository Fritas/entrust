def order_dict(dic):
    if dic:
        new_dic = dict()
        #necessario transformar o retorno do metodo keys() em lista
        list_keys = list(dic.keys())
        #ordena a lista
        list_keys.sort()
        #colocar os dados em um dict de forma ordenada
        for key in list_keys:
            new_dic[key] = dic[key]
        return new_dic
    return None

if __name__ == "__main__":
    dic = {
        'b' : 7,
        'e' : 9,
        'a' : 10
    }
    print("Teste order_dict")
    print("Ordenando o dic: %s" %(dic))
    print("Resultado: ", order_dict(dic))

    dic = dict()
    print("Ordenando o dic: %s" %(dic))
    print("Resultado: ", order_dict(dic))