import yaml
from car_model import CarModel
from car_component import CarComponent

component_dict = {}

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        print(data)
    car_data = data['cars']
    car_models = []
    for model in car_data:
        engine = component_dict.get(model['engine'], CarComponent(model['engine']))
        component_dict[model['engine']] = engine
        
        gearbox = component_dict.get(model['gearbox'], CarComponent(model['gearbox']))
        component_dict[model['gearbox']] = gearbox
        
        headlights = component_dict.get(model['headlights'], CarComponent(model['headlights']))
        component_dict[model['headlights']] = headlights
        
        dashboard = component_dict.get(model['dashboard'], CarComponent(model['dashboard']))
        component_dict[model['dashboard']] = dashboard
        
        car = CarModel(name=model['Car_model'], engine=engine, gearbox=gearbox, headlights=headlights, dashboard=dashboard)
        car_models.append(car)
    return car_models


