import random
import time
import requests
from datetime import datetime

FOG_URL = "http://100.55.95.0:5000/sensor-data"

while True:
    data = {
        "chair_id": "chair-01",
        "timestamp": datetime.utcnow().isoformat(),
        "seat_pressure": random.randint(60, 100),
        "posture_angle": random.randint(10, 60),
        "heart_rate": random.randint(70, 110),
        "temperature": random.randint(25, 35),
        "movement": random.choice([True, False])
    }

    print(data)
    requests.post(FOG_URL, json=data)
    time.sleep(5)