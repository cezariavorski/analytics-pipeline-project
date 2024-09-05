# Analytics Pipeline Project

This project simulates a data pipeline using Python (with a mock Databricks and Snowflake environment), FastAPI for serving data, and a React dashboard for visualizing it.

## Features

- **Data Ingestion and Transformation**: Simulates ingesting mock data using Python and PySpark (as if running in Databricks).
- **Mocked Snowflake Integration**: Instead of connecting to Snowflake, we mock the Snowflake behavior using Python lists to simulate database operations.
- **FastAPI**: A simple API built with FastAPI serves the transformed data.
- **React Dashboard**: The frontend, built in React, visualizes the data.
- **CI/CD Pipeline**: GitHub Actions is used for Continuous Integration (CI) to check code quality via linting and testing.

## Project Structure

```plaintext
analytics-pipeline-project/
├── .github/             # CI/CD workflows
│   └── workflows/
│       └── ci.yml       # GitHub Actions pipeline
├── react-dashboard/      # React frontend
├── src/                 # Python backend and data pipeline
│   ├── data_pipeline.py  # Data pipeline script
│   ├── api.py            # FastAPI backend
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignore file
```

## Requirements

### Python

- Python 3.x
- FastAPI
- Uvicorn
- Pandas
- PySpark

### React

- Node.js
- npm (Node Package Manager)

## Running the Project Locally

### 1. Clone the repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/cezariavorski/analytics-pipeline-project.git
cd analytics-pipeline-project
```

### 2. Install Python dependencies

You need to install the required Python libraries. You can do this by running:

```bash
pip install -r requirements.txt
```

This will install dependencies like `FastAPI`, `Pandas`, `PySpark`, and `Uvicorn`.

### 3. Run the data ingestion script

This script will simulate ingesting data, transforming it using PySpark, and inserting it into a mocked Snowflake database (a simple in-memory list).

```bash
python src/data_pipeline.py
```

You should see the transformed data printed to the console.

### 4. Start the FastAPI server

Start the FastAPI backend, which will serve the data through an API.

```bash
uvicorn src.api:app --reload
```

This will start the server at `http://localhost:8000`. You can view the data at `http://localhost:8000/data`.

### 5. Run the React app

Next, go to the `react-dashboard/` folder and install the required Node.js dependencies.

```bash
cd react-dashboard
npm install
```

Once the installation is done, start the React app:

```bash
npm start
```

The React app will run on `http://localhost:3000` and fetch data from the FastAPI server running on port 8000.

## FastAPI API

- **GET /data**: Returns the mock data from the Python backend.
  
Example response from `http://localhost:8000/data`:

```json
{
  "users": [
    {"name": "Carlos Silva", "age_in_months": 348, "city": "São Paulo"},
    {"name": "Ana Souza", "age_in_months": 420, "city": "Rio de Janeiro"},
    {"name": "Pedro Oliveira", "age_in_months": 504, "city": "Belo Horizonte"}
  ]
}
```

## CI/CD (Continuous Integration)

The project includes a GitHub Actions workflow that runs on every push to the `main` branch. It checks code quality using `flake8` for linting.

### Running CI locally

To run linting locally, make sure `flake8` is installed:

```bash
pip install flake8
flake8 src --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## Future Improvements

- Add actual integration with a Snowflake database.
- Implement additional features in the React dashboard for data manipulation and filtering.
- Expand the FastAPI backend to support more endpoints for CRUD operations.

## License

This project is open-source and available under the MIT License.
