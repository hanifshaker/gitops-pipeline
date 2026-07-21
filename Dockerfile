# Download a lightweight Python image to use
FROM python:3.9-slim
# Creates a folder named "/app" inside the container and set it as the active directory
WORKDIR /app
# Copy app.py from the local machine and into /app
COPY app.py .
# Install dependencies to run app.py
RUN pip install --no-cache-dir flask requests
# Documents which port the container will listen on at runtime
EXPOSE 8080
# These commands will automatically run once the container starts
CMD ["python", "app.py"]