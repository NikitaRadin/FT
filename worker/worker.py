import sys
import socket
from Sample import Sample
from Experiment import Experiment


id, host, port = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(socket.SOMAXCONN)
conn, addr = sock.accept()
while True:
    request = conn.recv(1024).decode('utf8').split()
    if not request:
        break
    if id == 1:
        sample = Sample(int(request[0]), int(request[1]), int(request[2]))
        response = sample.calculate_mean(int(request[3]), int(request[4]))
    elif id == 2:
        sample = Sample(int(request[0]), int(request[1]), int(request[2]))
        response = sample.calculate_variance(int(request[3]), int(request[4]))
    elif id == 3:
        experiment = Experiment(int(request[0]), int(request[1]), int(request[2]), int(request[3]), int(request[4]))
        response = experiment.start_mean_experiment()
    elif id == 4:
        experiment = Experiment(int(request[0]), int(request[1]), int(request[2]), int(request[3]), int(request[4]))
        response = experiment.start_variance_experiment()
    conn.send(' '.join(list(map(lambda x: str(x), response))).encode('utf8'))
conn.close()
sock.close()
