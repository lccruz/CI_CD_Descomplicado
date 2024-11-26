# CI/CD Descomplicado: Deploy de Aplicações Python

This repository demonstrates how to set up CI/CD pipelines for Python applications using GitHub Actions and Google Cloud. It includes examples with Django and Flask applications.

## Project Structure

```plaintext
CI_CD_Descomplicado/
├── .github/workflows/         # CI/CD workflows
├── docker-compose.yml         # Docker setup
├── services/
│   ├── django-app/            # Django app
│   └── flask-app/             # Flask app
```
---

## Getting Started

### Prerequisites

Before starting, ensure you have the following tools installed:

- [Docker](https://www.docker.com/products/docker-desktop) and Docker Compose
- Python 3.8+ (for local development and testing)
- A configured [Google Cloud Project](https://cloud.google.com/) for deployment

---

### Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/CI_CD_Descomplicado.git
   cd CI_CD_Descomplicado

2. **Set Up Environment Variables**:
   - Edit these files to configure your environment.

3. **Run Locally**:
   - Build and start services using Docker Compose:
     ```bash
     docker-compose build
     docker-compose up
     ```
4. **Run Tests**:
   - Django app:
     access the container and run the tests
     ```bash
     pytest
     ```
   - Flask app:
     access the container and run the tests
     ```bash
     pytest
     ```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


## Google Cloud Documentation

- [Deploy to Cloud Run with GitHub Actions](https://cloud.google.com/blog/products/devops-sre/deploy-to-cloud-run-with-github-actions/)


## Contributors
- Luciano Camargo Cruz [lccruz](https://github.com/lccruz)
- Davi Duarte [davifduarte](https://github.com/davifduarte)

