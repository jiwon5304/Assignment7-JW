import urllib.request
import json
import django
import os
from datetime import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cardoc.settings')
django.setup()

from tires.models import Tire

def BatchTask():
    
    for trimid in [5000,9000,11000,15000]:

        # if not Tire.objects.filter(trimid = trimid).exists():
            url = "https://dev.mycar.cardoc.co.kr/v1/trim/" + str(trimid)

            response    = urllib.request.urlopen(url)
            json_str    = response.read().decode("utf-8")
            data = json.loads(json_str)
            
            front_tire_spec       = data['spec']['driving']['frontTire']['value']
            front_tire_spec_width = front_tire_spec.split('/')[0]
            front_tire_spec_ratio = front_tire_spec.split('/')[1].split('R')[0]
            front_tire_spec_wheel = front_tire_spec.split('/')[1].split('R')[1]

            rear_tire_spec       = data['spec']['driving']['frontTire']['value']
            rear_tire_spec_width = rear_tire_spec.split('/')[0]
            rear_tire_spec_ratio = rear_tire_spec.split('/')[1].split('R')[0]
            rear_tire_spec_wheel = rear_tire_spec.split('/')[1].split('R')[1]

            Tire.objects.create(
                trimid             = trimid,
                front_width        = int(front_tire_spec_width),
                front_aspect_ratio = int(front_tire_spec_ratio),
                front_wheel        = int(front_tire_spec_wheel),
                rear_width         = int(rear_tire_spec_width),
                rear_aspect_ratio  = int(rear_tire_spec_ratio),
                rear_wheel         = int(rear_tire_spec_wheel)
            )

BatchTask()
print("====================================")
print("Success")
print(datetime.now())