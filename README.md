# Open Weather Map
## Search city weather on open weather map API's 

## Requirements
- Python 3.9+
- MySQL 8.0+

Please consult Google if you need to install any of the pre-requisites

## Set Up Installation
- Clone/Download the git repo - `git clone https://github.com/Mhlengi/open_weather_map`
- Create a MySQL database `open_weather_map` with user `*****` and password `******`
- Navigate to the project folder`open_weather_map`
- Install python3 `brew install python3`
- Install pip3 `pip3 install virtualenv`
- Create virtual environment: `virtualenv -p python3 venv`
- Activate a virtual environment: `. venv/bin/activate`
- Install all the python dependencies `pip install -r requirements.txt`
- Run the database migrations `python manage.py migrate`
- In project source folder create `static` and `staticfiles` folders if does not exists 
- Run collect static files `python manage.py collectstatic`
- Create Superuser but not required for this tasks `python manage.py createsuperuser` 
- Start the WebServer `python manage.py runserver`
(*Please note everytime you pull from master you may need to run the migrations and install any new dependencies
- as per the above instructions*)
- Note: Please find `config.py` file in source folder. 
- Then update your `OPEN_WEATHER_MAP_API = "******************************************"` 
- Which can be found here [OpenWeatherMap API Documentation](https://openweathermap.org/api) or Find it from your development team
