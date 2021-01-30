import subprocess
import socket


class Manager:
    def __init__(self, host='127.0.0.1', port=5001):
        self.host = host
        self.port = port

    def run(self):
        for id in range(1, 5):
            subprocess.Popen(['python', 'C:/Users/lenovo/Desktop/FT/worker/worker.py', f'{id}', f'{self.host}',
                              f'{self.port + id}'])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(socket.SOMAXCONN)
        conn, addr = sock.accept()
        while True:
            request = conn.recv(1024).decode('utf8').split()
            if not request:
                break
            operation = request[0]
            parameters = request[1:]
            if operation == 'calculate_mean':  # Отправка воркеру запроса на вычисление математического ожидания
                sock = socket.create_connection((self.host, self.port+1), timeout=None)
                sock.sendall(' '.join(parameters).encode('utf8'))
                response = sock.recv(1024).decode('utf8')
            elif operation == 'calculate_variance':  # Отправка воркеру запроса на вычисление дисперсии
                sock = socket.create_connection((self.host, self.port+2), timeout=None)
                sock.sendall(' '.join(parameters).encode('utf8'))
                response = sock.recv(1024).decode('utf8')
            elif operation == 'start_mean_experiment':  # Отправка воркеру запроса на проведение эксперимента
                # математического ожидания
                sock = socket.create_connection((self.host, self.port+3), timeout=None)
                sock.sendall(' '.join(parameters).encode('utf8'))
                response = sock.recv(1024).decode('utf8')
            elif operation == 'start_variance_experiment':  # Отправка воркеру запроса на проведение эксперимента
                # дисперсии
                sock = socket.create_connection((self.host, self.port+4), timeout=None)
                sock.sendall(' '.join(parameters).encode('utf8'))
                response = sock.recv(1024).decode('utf8')
            conn.send(response.encode('utf8'))
        conn.close()
        sock.close()
