# Kickstarter App - DS14/15 Build Week

TODO: Refine this readme document
## Installation

Download the repo and navigate there from the command line:

```sh
git clone https://github.com/Build-Week-Kickstarter-Success-2/DS.git
cd kickstarter
```

## Setup

Setup a virtual environment and install required packages

```sh
pipenv --python 3.7
pipenv shell
pipenv install Flask pandas numpy scikit-learn python-dotenv gunicorn category_encoders

```



## Run the Flask app locally

Load web app:

```sh
FLASK_APP=web_app flask run
```
Test API
- Go to this link https://reqbin.com/ to submit post request to API
- Paste https://ks-ds-15.herokuapp.com/predict and select ‘POST’
Navigate to the Content tab. enter the following JSON input, and click Send
```sh
{
    "category": {
        "0": "Animation"
    },
    "staff_pick": {
        "0": false
    },
    "description_leng": {
        "0": 99
    },
    "usd_goal": {
        "0": 30000
    },
    "cam_length": {
        "0": 60
    }
}
]
```
Output should be in the following format
```
{
    "prediction": "[False]",
    "prediction_proba": 0.14
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

