import yaml
from car_model import CarModel

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return [CarModel(**model) for model in data]
