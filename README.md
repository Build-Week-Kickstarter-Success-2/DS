# Kickstarter App - DS14/15 Build Week

TODO: Refine this readme document + TODO!
## Installation

Download the repo and navigate there from the command line:

```sh
git clone git@github.com:s2t2/twitoff-15.git
cd twitoff-15
```

## Setup

Setup a virtual environment and install required packages

```sh
pipenv --python 3.7
pipenv shell
pipenv install Flask pandas numpy scikit-learn python-dotenv gunicorn category_encoders

```



## Run the Flask app locally

Via forms

```sh
FLASK_APP=web_app flask run
```
Via API

```sh
python web_app/app.py
```
Test the API by running a post request on 'localhost:12345/predict' with the following input
```sh
[
    {"category": "software", "pitch": "i am the goose that lays golden eggs", "a": 1, "b": 20}
]
```
Output should be in the following format
```
{
  "prediction": "[1]"
}
```

## Deploy the app to Heroku

Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```sh
 $ heroku login 
 ```

Create a new Git repository
Initialize a git repository in a new or existing directory

```sh
$ cd my-project/
$ git init
```

```sh
$ heroku git:remote -a kickstarter-ds15
```
Deploy your application
Commit your code to the repository and deploy it to Heroku using Git.

```sh
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
Existing Git repository
For existing repositories, simply add the heroku remote

```sh
$ heroku git:remote -a kickstarter-ds15
```

