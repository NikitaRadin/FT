import socket
#import pyplot


class Client:
    def __init__(self, host='127.0.0.1', port=5001, timeout=None):
        self.sock = socket.create_connection((host, port), timeout)

    def calculate_mean(self, minimum, maximum, size, thread_number, element_number):
        self.sock.sendall(f'calculate_mean {minimum} {maximum} {size} {thread_number} {element_number}'.encode('utf8'))
        response = self.sock.recv(1024).decode('utf8')
        print(response)

    def calculate_variance(self, minimum, maximum, size, thread_number, element_number):
        self.sock.sendall(f'calculate_variance {minimum} {maximum} {size} {thread_number} {element_number}'.
                          encode('utf8'))
        response = self.sock.recv(1024).decode('utf8')
        print(response)

    def start_mean_experiment(self, minimum, maximum, size, maximum_thread_number, element_number):
        self.sock.sendall(f'start_mean_experiment {minimum} {maximum} {size} {maximum_thread_number} {element_number}'.
                          encode('utf8'))
        response = self.sock.recv(1024).decode('utf8').split()
        durations = list(map(lambda x: float(x), response))
        #pyplot.plot(list(range(1, maximum_thread_number + 1)), durations)
        print(durations)

    def start_variance_experiment(self, minimum, maximum, size, maximum_thread_number, element_number):
        self.sock.sendall(f'start_variance_experiment {minimum} {maximum} {size} {maximum_thread_number} '
                          f'{element_number}'.encode('utf8'))
        response = self.sock.recv(1024).decode('utf8').split()
        durations = list(map(lambda x: float(x), response))
        #pyplot.plot(list(range(1, maximum_thread_number + 1)), durations)
        print(durations)

    def __del__(self):
        self.sock.close()
