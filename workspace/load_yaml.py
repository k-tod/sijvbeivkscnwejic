import yaml
from car_model import CarModel


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    car_data = data['cars']
    return [CarModel(name=model['Car_model'], engine=model['engine'], gearbox=model['gearbox'], headlights=model['headlights'], dashboard=model['dashboard']) for model in car_data]
