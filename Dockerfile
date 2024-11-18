# Use the official Python 3.12 image
FROM python:3.12.7-slim

# Set the working directory inside the container
WORKDIR /app

# Upgrade pip and install Poetry
RUN pip install --upgrade pip
RUN pip install uv

# Copy the Rye configuration files
COPY README.md pyproject.toml requirements.lock ./

# Install the application dependencies
RUN uv pip install --no-cache --system -r requirements.lock

# Copy the application source code and documentation
COPY src/ src/
COPY docs/ docs/
COPY mkdocs.yml .

# Build mkdocs documentation
RUN mkdocs build

# Set the command to run the application
CMD ["python", "src/francophonia"]
