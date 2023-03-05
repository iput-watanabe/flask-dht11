import adafruit_dht
from board import * 
import time
import datetime

instance_dht = adafruit_dht.DHT11(pin=D4, use_pulseio=False)
WAIT_INTERVAL = 2
WAIT_INTERVAL_RETRY = 5

def get_dht_data():
    temp_dht = 200.0
    humid_dht = 100.0
    try:
        instance_dht.measure()
        temp_dht = instance_dht.temperature
        humid_dht = instance_dht.humidity

    except RuntimeError:
        print("RuntimeError: DHT11 returns wrong values, maybe.: " + str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))
        time.sleep(WAIT_INTERVAL_RETRY)
    except OSError:
        print("OSError: DHT11/22: OS Error, but we ignore it.: "+ str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))
        time.sleep(WAIT_INTERVAL_RETRY)

    return float(temp_dht), float(humid_dht)

def test_get_dht_data():
    count = 0
    tempe = 40.0
    humid = 85.0
    while True:
            tempe, humid = get_dht_data()
            now_time = str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
            print("Temperature: %f  Humidity: %f" % (tempe, humid), now_time)
            time.sleep(WAIT_INTERVAL)
            count += 1
            if(count > 10):
                 break

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    test_get_dht_data()
