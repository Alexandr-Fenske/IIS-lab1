import requests
import time
import random

for i in range(50):
    params = {'phone_id': i}
    data = {
        "battery_power": random.randint(500,1999),
        "blue": random.randint(0,1),
        "clock_speed": random.uniform(0.5, 3),
        "dual_sim": random.randint(0,1),
        "fc": random.randint(0,19),
        "four_g": random.randint(0,1),
        "int_memory": random.randint(2,64),
        "m_dep": random.uniform(0.1, 1),
        "mobile_wt": random.randint(80,200),
        "n_cores": random.randint(1,8),
        "pc": random.randint(0,20),
        "px_height": random.randint(0,1907),
        "px_width": random.randint(501,1988),
        "ram": random.randint(263,3989),
        "sc_h": random.randint(5,19),
        "sc_w": random.randint(0,18),
        "talk_time": random.randint(2,20),
        "three_g": random.randint(0,1),
        "touch_screen": random.randint(0,1),
        "wifi": random.randint(0,1)
        } 

    response = requests.post('http://phone-predict:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(0,5))
    print(response.json())