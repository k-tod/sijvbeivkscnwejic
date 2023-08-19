from lxml import etree


def generate_xml(car_model, output_folder):
    root = etree.Element('car_model', name=car_model.name)
    etree.SubElement(root, 'engine').text = car_model.engine
    etree.SubElement(root, 'gearbox').text = car_model.gearbox
    etree.SubElement(root, 'headlights').text = car_model.headlights
    etree.SubElement(root, 'dashboard').text = car_model.dashboard
    for component in car_model.common_components + car_model.unique_components:
        etree.SubElement(root, 'component', name=component.name, uid=component.uid)
    tree = etree.ElementTree(root)
    tree.write(f'{output_folder}/{car_model.name}.xml', pretty_print=True)

