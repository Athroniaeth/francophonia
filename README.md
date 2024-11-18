<div align="center">
<img src="docs/__static/img/logo.png" alt="presentation_1" width="200" height="200">
    <h1 style="font-size: xx-large; font-weight: bold;">FrancophonIA</h1>
    <a href="#">
        <img src="https://img.shields.io/badge/Python-3.12-0">
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/License-MIT-f">
    </a>
    <br>
</div>

Project designed to bring together free resources on artificial intelligence in French (mathematics, algorithms, machine learning, deep learning).

## Installation

This project use `rye`, to install the dependencies, you can run the following command:

```bash
rye install
```

## Usage

This project uses `rye`, a Python environment and package manager. If you don’t have `rye` installed, visit [rye documentation](https://github.com/mitsuhiko/rye) for setup instructions.

```bash
rye run src/francophonia run
```

## Structure

```bash
├── src               # Project source code
├── docs              # Project documentation
│   └── static        # README.md static files
├── tests             # Folder containing software tests
│   ├── units         # Unit tests
│   └── integrations  # Integration tests
├── scripts           # Useful scripts for the project (no CI/CD)
├── ruff.toml         # Ruff configuration file
```

## Containerization

This project uses Docker to containerize the application. The Dockerfile is located at the root of the project. To build the Docker image, you can use the following command:

```bash
docker build -t francophonia .
```

To run the Docker container, you can use the following command:

```bash
docker run -it -p 7860:7860 francophonia
```

### Docker-compose

This project have a `docker-compose.yml` file to run the project in production. To run the project, you can use the
following command:

- build: Build the Docker image if not exists
- d: Mode daemon (run in background)

```bash
docker-compose up --build -d
```

### Tips & Other

For debugging purposes, you can run the following command:

```bash
docker run -it -p 7860:7860 xxxxxx /bin/bash
```

For deleting all Docker containers, you can use the following command:

```bash
docker rm -f $(docker ps -a -q)
```

For deleting all Docker images, you can use the following command:

```bash
docker rmi -f $(docker images -q)
``` 

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request. Ensure your code follows the project's linting and testing standards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
