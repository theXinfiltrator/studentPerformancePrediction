build a machine learning model in the colab and convert it into a .joblib file
use fastapi to make the endpoint using get and post request and integrate the .joblib file with fastapi
use jinja2 to use custom html templates

use docker to containerize the project by building an image and running the container
--project structure
.
├── Dockerfile
├── app
│   ├── app.py
│   ├── regressor.joblib
│   └── static
│       └── index.html
├── readme.txt
└── requirements.txt
use render.com to deploy the docker container in the cload by pushing the project to github and deploy from github
now the web service is live at https://studentperformanceprediction.onrender.com
