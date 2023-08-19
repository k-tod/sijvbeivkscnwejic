import os
from load_yaml import load_yaml
from generate_xml import generate_xml

def main(yaml_file_path, output_folder):
    car_models = load_yaml(yaml_file_path)
    os.makedirs(output_folder, exist_ok=True)
    for car_model in car_models:
        generate_xml(car_model, output_folder)

if __name__ == '__main__':
    main('car_models.yaml', 'output')
