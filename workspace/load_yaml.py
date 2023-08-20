import yaml
from car_model import CarModel
from car_component import CarComponent

component_dict = {}

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Get the root key and its associated data
    root_key, products_data = list(data.items())[0]

    products = []
    for product_data in products_data:
        if isinstance(product_data, dict):  # Ensure product_data is a dictionary
            product_name_key = next(iter(product_data))  # Get the first key as the product name key
            product_name = product_data[product_name_key]
            
            components = {}
            for key, value in product_data.items():
                if key != product_name_key:  # Exclude the product name from the components
                    component = component_dict.get(value, CarComponent(value))
                    component_dict[value] = component
                    components[key] = component
            product = CarModel(name=product_name, **components)
            products.append(product)
    return products
