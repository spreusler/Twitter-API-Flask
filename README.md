# Twitter-API-Flask

Do you want on-demand sentiment analysis for a given keyword? This project serves you Twitter API access on a Flask framework. Simply enter keyword and you receive the latest tweets and their sentiment via Textblob.

## Files and Folders

- templates - contains html source files for Flask render_template()
- Procfile - Optional for deployment. This project is live on Heroku. Gunicorn is a WSGI HTTP Server Interface for Python.
- app.py - Contains Flask logic
- config_demo.py - File for credentials. Replace variables with your own data.
- requirements.py - Python libraries and dependencies for the project
- utils.py - Twitter API and sentiment analysis logic

## Getting Started

- Download repository
- Insert your own credentials in ``` config_demo.py ``` and rename it to ```config.py```
- Local: Run application with ```python app.py```
- Optional: Deployment to Heroku

### Prerequisites

- Python 3.6
- Install libraries via ```pip install -r requirements.txt```

## Deployment

- Optional: Deployment on Heroku with Gunicorn (Procfile)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
