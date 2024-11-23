## Introduction

This application is a simple Python-based GUI tool that fetches and displays various types of textual content (like jokes, verses, and toasts) from specified URLs. It's built using the Tkinter library and demonstrates basic network communication, XML parsing, and GUI capabilities in Python.

## Installation

To run this application, you need to have Python installed on your system. Python 3.x is recommended. This application also requires external libraries such as `requests` and `xmltodict` for network requests and XML parsing, respectively.

### Steps to Install Python

1. Download Python from the official website: [Python Downloads](https://www.python.org/downloads/).
2. Follow the installation instructions for your specific operating system.

### Setting Up the Application

1. Clone the repository or download the source code to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory where the application is stored.
4. Install required dependencies by running:

   pip install requests xmltodict

## Configuration

Before running the application, ensure the URLs in the `send_request_and_display_response` function are set to your desired endpoints. These URLs are where the application fetches the textual content.

## Usage

To run the application, execute the main Python script. If your file is named `main.py`, use the following command:

python main.py

This will open a GUI window with buttons to fetch different types of content. Click on the desired button to fetch and display the content.

## Application Logic

- **GUI Creation**: The application uses Tkinter to create a simple GUI with buttons and a text display area.
- **Network Requests**: Upon clicking a button, the application sends a GET request to the predefined URL.
- **Response Handling**: The received response is displayed in a new window. If the response is in XML format, it's parsed before being displayed.
- **Error Handling**: In case of network errors or issues with the request, an error message is displayed.

## Postman Link

https://www.postman.com/joint-operations-saganist-46223840/sergey/collection/f0sktzv/numbers
