# Assamese Voice into Text

A web application for converting Assamese speech into text built with Streamlit.

## Features

- Simulated voice recording and transcription
- Colorful display of Assamese alphabet
- Cultural elements including Bihu dance illustrations
- Traditional Assamese-themed design

## Installation

1. Clone or download this repository
2. Install the required packages:

```bash
pip install -r dependencies.txt
```

## Running the Application

To run the application locally:

```bash
streamlit run app.py
```

The application will be available at http://localhost:8501

## Deployment Options

### 1. Deploy on a VPS or Dedicated Server

1. Copy all files to your server
2. Install dependencies: `pip install -r dependencies.txt`
3. Run with: `streamlit run app.py`
4. For production, consider using a process manager like Supervisor or PM2

### 2. Deploy with Docker

If you have Docker installed:

```bash
# Build the Docker image
docker build -t assamese-voice-app .

# Run the container
docker run -p 8501:8501 assamese-voice-app
```

Access the application at http://localhost:8501

### 3. Deploy on Cloud Platforms

This application can be deployed on cloud platforms that support Python applications:

- Heroku
- Google Cloud Platform
- Azure
- AWS

## Files Description

- `app.py`: Main Streamlit application
- `utils.py`: Utility functions for voice recording simulation
- `background.py`: Background styling and header components
- `icons.py`: SVG icons and cultural illustrations
- `assamese_alphabet.py`: Assamese alphabet display functionality
- `.streamlit/config.toml`: Streamlit configuration
- `dependencies.txt`: Required Python packages
- `Dockerfile`: Docker configuration for containerization

## Notes

This is a demonstration version with simulated voice recording. In a production environment, you would need to implement actual speech recognition for Assamese.