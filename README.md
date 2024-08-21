# DataSvc API Project

## Overview

The `DataSvc` API is a Python-based service that reads data from a CSV file located in a local folder, maps the data to objects, and exposes an API to retrieve the data. The project is built using Flask and Flask-RESTX for creating RESTful endpoints and is hosted locally with Swagger for API documentation.

## Project Structure

DataSvc/
│
├── data/
│   └── file1.csv             # CSV file containing the data
│
├── datasvc/
│   ├── __init__.py           # Initializes the Flask application
│   ├── main.py               # Entry point of the application
│   ├── models.py             # Data model definitions
│   ├── service.py            # Logic for reading and processing CSV data
│
├── env/                      # Python virtual environment directory
│
├── tests/
│   ├── __init__.py           # Initializes the test suite
│   ├── test_api.py           # Unit tests for API endpoints
│
├── .gitignore                # Git ignore file
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── setup.py                  # Project setup configuration

## Setup and Installation

### Prerequisites

- Python 3.12 or higher
- `pip` (Python package installer)

### Step 1: Clone the Repository

Clone this repository to your local machine:

git clone https://github.com/Bryanh9111/DataSvc.git
cd DataSvc

### Step 2: Set Up Virtual Environment

Create and activate a virtual environment to manage project dependencies:

python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

### Step 3: Install Dependencies

Install the required Python packages using `pip`:

pip install -r requirements.txt

### Step 4: Add the CSV File

Place your CSV file (`file1.csv`) in the `data` folder. Ensure the CSV file has the correct format that matches your data model.

### Step 5: Run the Application

Start the Flask application:

python -m datasvc.main

The API will be available at `http://localhost:5000`, and the Swagger documentation can be accessed at `http://localhost:5000/swagger/`.

## API Endpoints

### GET /data/read

Retrieves the data from the CSV file and returns it as JSON.

- **URL:** `http://localhost:5000/data/read`
- **Method:** `GET`
- **Response:** JSON array containing the data from the CSV file.

### Example Response

```json
[
  {
    "col1": "value1",
    "col2": "value2",
    "col3": "value3"
  },
  {
    "col1": "value4",
    "col2": "value5",
    "col3": "value6"
  }
]
```

## Testing

### Running Tests

Unit tests are located in the `tests` folder. To run the tests, use the following command:

python -m unittest discover tests

## Customization

- **CSV File Location:** You can modify the CSV file location by updating the path in the `service.py` file.
- **API Routes:** Additional API routes can be added by creating new classes in the `datasvc.main` file and defining new endpoints.