
*** Settings ***
Library    Browser
Library    ./image_color_detection.py

*** Variables ***
${ELEMENT_SELECTOR}         div#my-element
${TOLERANCE_PERCENTAGE}      5  # 5% margin for both width and height

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
