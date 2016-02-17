import socket
import time

from storage import packet_size, store, time_sleep, time_smoke
from utils import _print


def process(code, request):
    while True:
        _print('Esperando {}!'.format(store.get(code)['required']))
        request.send('need'.encode('UTF-8'))

        while True:
            message = request.recv(packet_size).decode('UTF-8')
            if message == 'enable':
                _print('Servido!')
                time.sleep(time_sleep)
                _print('Armando cigarro!')
                time.sleep(time_sleep)
                _print('Fumando!!!')
                time.sleep(time_smoke)
                request.send('enable'.encode('UTF-8'))

            time.sleep(time_sleep)
            if message != 'ack':
                break

        time.sleep(time_sleep)


def init(ip, port, code):
    try:
        request = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        request.connect((ip, port))

        request.send('{}'.format(code).encode('UTF-8'))
        time.sleep(time_sleep)

        resp = request.recv(packet_size).decode('UTF-8')
        if resp == 'accepte':
            process(code, request)
        else:
            _print('Rechazado por el agente.')
        request.close()
    except KeyboardInterrupt:
        _print('Cerrando conexiones...')
        request.close()
