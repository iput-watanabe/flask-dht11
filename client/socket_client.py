import socket 
import time
import datetime
import json
from get_dht11 import get_dht_data

#SERVER = 'localhost'
host = 'localhost'
port = 8765
data_list = []

WAIT_INTERVAL = 5

def client_test(hostname = host, waiting_port = port, message1 = data_list):

    node_s = hostname
    port_s = waiting_port
    try:
        while True:
            socket_r_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_r_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            socket_r_s.connect((node_s, port_s))
            print('Connecting to the server. ' 
                  + 'node: ' + node_s + '  '
                  + 'port: ' + str(port_s))

            data_s_str = message1
            data_s = data_s_str.encode('utf-8')
            socket_r_s.send(data_s)
            print('I (a client) have just sent data __' 
                + data_s_str 
                + '__ to the server ' + node_s + ' .')

            socket_r_s.close()

            time.sleep(WAIT_INTERVAL)

    except KeyboardInterrupt:
        print("End of this client.")

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    hostname_v = host
    waiting_port_v = port

    temp, humid = get_dht_data()
    now_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    data_list = [{"temp" : temp, "humid": humid, "date" : now_time}]
    data_json = json.dumps(data_list)
    print("Temperature: %f  Humidity: %f" % (temp, humid), now_time)

    client_test(hostname_v, waiting_port_v, data_json)
