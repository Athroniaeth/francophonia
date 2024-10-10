# Use the official Python 3.12 image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Upgrade pip and install Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Copy the Poetry configuration files
COPY pyproject.toml poetry.lock ./

# Install dependencies from the lock file
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the application source code and documentation
COPY src/ src/
COPY docs/ docs/
COPY mkdocs.yml .

# Build mkdocs documentation
RUN mkdocs build

# Set the command to run the application
CMD ["python", "src/francophonia/"]
