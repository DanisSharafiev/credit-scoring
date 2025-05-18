# Credit Scoring Service

The Credit Scoring Service is a FastAPI-based microservice that predicts the creditworthiness of individuals based on financial parameters such as interest rate and outstanding debt.

## Features

- **Prediction Endpoint**: `/api/credit-score` for predicting credit scores.
- **Health Check**: `/api/health` endpoint to check service status.
- **Logging**: Detailed logging for requests, predictions, and errors.
- **Dockerized**: Easily deployable using Docker.

## API Endpoints

### Health Check
- **URL**: `/api/health`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "status": "healthy"
  }
  ```

### Predict Credit Score
- **URL**: `/api/credit-score`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "interest_rate": 15.0,
    "outstanding_debt": 2000.0
  }
  ```
- **Response**:
  ```json
  {
    "credit_score": "Good"
  }
  ```

## Getting Started

### Prerequisites

- Python 3.10+
- Docker

### Installation

1. Navigate to the `credit-scoring-service` directory:
   ```bash
   cd credit-scoring-service
   ```

2. Build and run the service using Docker:
   ```bash
   docker build -t credit-scoring-service .
   docker run -p 8000:8000 credit-scoring-service
   ```

3. Access the API documentation at `http://localhost:8000/docs`.

## Running Tests

To run tests for the service:
```bash
pytest tests/
```

## License

This service is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
