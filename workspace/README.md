Based on the requirements, we will need the following core classes and functions:

1. `CarComponent`: A class to represent a car component. It will have attributes such as `name` and `uid`.

2. `CarModel`: A class to represent a car model. It will have attributes such as `name`, `common_components` (a list of `CarComponent` objects), and `unique_components` (a list of `CarComponent` objects).

3. `load_yaml`: A function to load the yaml file and return a list of `CarModel` objects.

4. `generate_xml`: A function to generate an xml file for each `CarModel` object.

5. `main`: The entry point of the script. It will call `load_yaml` to get the list of `CarModel` objects, and then call `generate_xml` for each `CarModel` object.

Now, let's write the code for each file.

requirements.txt
