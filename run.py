from socket import gethostbyname, gethostname
from app import app


if __name__ == '__main__':
    app.run(debug=True, host=gethostbyname(gethostname()))
    #gethostbyname(gethostname()) > pega o IP da maquina local
