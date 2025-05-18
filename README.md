# Credit Scoring Project

This project is a credit scoring system designed to predict the creditworthiness of individuals based on various financial parameters. It includes a FastAPI-based service for predictions and a machine learning model for inference.

## Project Structure

```
credit-scoring/
├── credit-scoring-service/  # Main service for credit scoring
├── data/                    # Training and testing datasets
├── models/                  # Machine learning model and inference logic
├── notebooks/               # Jupyter notebooks for data analysis
├── tests/                   # Unit and integration tests
└── docker-compose.yml       # Docker Compose configuration
```

## Features

- **Credit Scoring Service**: A FastAPI-based service for predicting credit scores.
- **Machine Learning Model**: Pre-trained model for inference.
- **Dockerized Deployment**: Easily deployable using Docker Compose.
- **Unit Tests**: Comprehensive test coverage using `pytest`.

## Getting Started

### Prerequisites

- Python 3.10+
- Docker and Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd credit-scoring
   ```

2. Build and run the service using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Access the API documentation at `http://localhost:8000/docs`.

### Running Tests

To run the tests, use the following command:
```bash
docker-compose exec credit-scoring-service pytest tests/
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.