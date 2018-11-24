# Entrust
Entrust é uma aplicação Web que tem o intuito de solucionar e representar graficamente funções de primeiro ao quarto grau.

## Desenvolvimento
O master do projeto sempre será mantido como a versão oficial, disponível para acesso em entrust.blumenau.ifc.edu.br'.

### Pré-Requisitos
Python 3

VirtualEnv

Você pode baixar o Python 3 através do site oficial na página de [downloads](https://www.python.org/downloads/){:target="_blank"}.

Caso você não tenha a virtualenv, instale-a utilizando:
```
> pip install virtualenv
```
Caso seu sistema operacional não utilize Python 3 por padrão, execute da seguinte forma.
```
> pip3 install virtualenv
```


### Instalação
Crie uma máquina virtual utilizando os seguintes passos:
```
> python -m venv <nome-da-maquina-virtual>
> source <nome-da-maquina-virtual>/bin/activate
```
Caso seu sistema operacional não utilize Python 3 por padrão, execute da seguinte forma.
```
> python3 -m venv <nome-da-maquina-virtual>
> source <nome-da-maquina-virtual>/bin/activate
```

Dentro do diretorio você encontrará o arquivo requirements.txt, instale as bibliotecas com o seguinte comando.
```
> pip install -r requirements.txt
```

Caso seu sistema operacional não utilize Python 3 por padrão, execute da seguinte forma.
```
> pip3 install -r requirements.txt
```

### Executando
Para ligar o servidor e poder acessar ele na web, é preciso que faça esse comando dentro do diretorio do projeto:
```
> python run.py runserver
```

Caso seu sistema operacional não utilize Python 3 por padrão, execute da seguinte forma.
```
> python3 run.py runserver
```

## O Desenvolvimento da aplicação foi feito com as seguintes linguagens e bibliotecas
- [Python](https://www.python.org/){:target="_blank"}
  - [Flask](http://flask.pocoo.org/){:target="_blank"}
  - [SymPy](https://www.sympy.org/pt/index.html){:target="_blank"}
- [JavaScript](https://www.javascript.com){:target="_blank"}
  - [jQuery v3](https://jquery.com){:target="_blank"}
  - [Function Plot](https://mauriciopoppe.github.io/function-plot/){:target="_blank"}
- HTML5
- CSS3
  - [Bootstrap v4.0](https://getbootstrap.com){:target="_blank"}

## Equipe
* Desenvolvedor: Adriano Damasceno da Silva Júnior. Aluno do Curso Técnico em Informática Integrado ao Ensino Médio do IFC Campus Blumenau; adamascenosj@gmail.com. [Currículo Lattes](http://lattes.cnpq.br/8609985120910990){:target="_blank"}. [GitHub](https://github.com/Fritas){:target="_blank"}
* Orientador: Hylson Vescovi Netto. Professor de Informática, IFC Campus Blumenau, hylson.vescovi@ifc.edu.br. [Currículo Lattes](http://lattes.cnpq.br/6155862179794521){:target="_blank"}. [GitHub](https://github.com/hvescovi){:target="_blank"}
* Co-orientador: Riad Mattos Nassiffe. Professor de Informática, IFC Campus Blumenau, riad.nassiffe@ifc.edu.br. [Currículo Lattes](http://lattes.cnpq.br/8149931631827091){:target="_blank"}. [GitHub](https://github.com/riadnassiffe){:target="_blank"}
* Colaborador: Alexandre Veloso dos Santos. Professor de Matemática, IFC Campus Blumenau, alexandre.santos@ifc.edu.br.
