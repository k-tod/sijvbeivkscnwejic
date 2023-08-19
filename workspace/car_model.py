from car_component import CarComponent


class CarModel:
    def __init__(self, name, engine, gearbox, headlights, dashboard, common_components=[], unique_components=[]):
        self.name = name
        self.engine = engine
        self.gearbox = gearbox
        self.headlights = headlights
        self.dashboard = dashboard
        self.common_components = common_components
        self.unique_components = unique_components

