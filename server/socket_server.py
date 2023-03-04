import time
import json
import csv

#SERVER = 'localhost'
SERVER = 'localhost'
WAITING_PORT = 8765
CSV_FILENAME = '/server/temp_humid_date.csv'

LOOP_INTERVAL = 5

def server_test(server_v1=SERVER, waiting_port_v1=WAITING_PORT):
    import socket
    import threading
    
    def recv_data1024(socket1, client_address):
        data_r = socket1.recv(1024)
        print(data_r)
        data_json = data_r.decode('utf-8')
        data_list = json.loads(data_json)
        data_list = [data_list[0]["temp"], data_list[0]["humid"], data_list[0]["date"]]

        with open(CSV_FILENAME, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data_list)

        time.sleep(LOOP_INTERVAL)

        print("Now, closing the data socket.")
        socket1.close()

    socket_w = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_w.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    node_s = server_v1
    port_s = waiting_port_v1
    socket_w.bind((node_s, port_s)) 

    BACKLOG = 5
    socket_w.listen(BACKLOG)

    print('Waiting for the connection from the client')

    try:
        while True:
            socket_s_r, client_address = socket_w.accept()
            print('Connection from ' 
                  + str(client_address) 
                  + " has been established.")
            thread = threading.Thread(target=recv_data1024, 
                args=(socket_s_r, client_address))
            thread.start()

    except KeyboardInterrupt:
        print("Now, closing the waiting socket.")
        socket_s_r.close()

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")

    hostname = SERVER
    waiting_port = WAITING_PORT
    
    server_test(hostname, waiting_port)
