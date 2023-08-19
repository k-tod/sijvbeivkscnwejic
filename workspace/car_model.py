from car_component import CarComponent

class CarModel:
    def __init__(self, name, common_components, unique_components):
        self.name = name
        self.common_components = [CarComponent(**component) for component in common_components]
        self.unique_components = [CarComponent(**component) for component in unique_components]
