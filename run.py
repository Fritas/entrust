"""
File of execute of the application
"""

from socket import gethostbyname, gethostname
from app import manager


if __name__ == '__main__':
    manager.run()
