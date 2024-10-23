
# Robot Framework Image Color Detection

This project provides a Python function for detecting colored pixels in a screenshot, ignoring the edges based on a configurable tolerance. It is designed to be used with the Robot Framework for test automation and integrates with the `robotframework-browser` library.

## Features
- Detects non-black and non-white pixels in a screenshot.
- Ignores a percentage of the edges to handle cases where a colored border/frame surrounds the image.
- Flexible percentage-based edge tolerance for both width and height, or identical percentage for both axes.
  
## Project Files
- `image_color_detection.py`: Contains the Python function `image_contains_color` which analyzes the screenshot and returns the coordinates of the first colored pixel found.
- `test.robot`: Example test case for integrating with Robot Framework and `robotframework-browser`.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/robotframework-image-color-detection.git
    ```

2. Install the necessary Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add the custom Python library to your Robot Framework test settings:
    ```robot
    Library    ./image_color_detection.py
    ```

## Usage

In your Robot Framework test case:

```robot
*** Settings ***
Library    Browser
Library    ./image_color_detection.py

*** Variables ***
${ELEMENT_SELECTOR}         div#my-element
${TOLERANCE_PERCENTAGE}      5  # Percentage of width and height to ignore

*** Test Cases ***
Find Non-Black-White Pixel With Percentage-Based Edge Tolerance
    New Page    https://example.com
    # Capture screenshot of the specific element
    ${screenshot_path}    Take Element Screenshot    ${ELEMENT_SELECTOR}    path=./element_screenshot.png

    # Call Python function to analyze the screenshot and get pixel coordinates, ignoring the edges
    ${found_color}    ${pixel_x}    ${pixel_y}=    Image Contains Color    ./element_screenshot.png    ${TOLERANCE_PERCENTAGE}

    # Assert that a colored pixel was found
    Should Be True    ${found_color}    No colored pixel found to click

    # Log the coordinates of the pixel
    Log    Non-black/white pixel found at coordinates: ${pixel_x}, ${pixel_y}

    # Optionally, click the pixel on the webpage using Robot Framework
    # Click    ${ELEMENT_SELECTOR}    offset=${pixel_x}, ${pixel_y}
```

## License
This project is licensed under the MIT License. See `LICENSE` for more details.
