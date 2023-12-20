# Diamonds price prediction

## Table of contents
- [Problem description]()
- [About the dataset]()
- [Repository files]()
- [How to install dependencies]()
- [Host the server]()
- [Making a prediction]()
- [Docker containerization]()
- [Cloud deployment]()

## Problem description
Diamonds are one of the precious stones bought to wear as jewellery or as investment as well.

This  project is aimed to create a model that predicts diamond prices based on features such as shape, carat, cut, color, clarity, lab and type.

## About the dataset
This dataset was taken from kaggle : https://www.kaggle.com/datasets/miguelcorraljr/brilliant-diamonds. Dataset contains 119307 observations.  

Attribute Information:
 1. id: Diamond identification number provided by Brilliant Earth
 2. url: URL for the diamond details page
 3. shape: External geometric appearance of a diamond
 4. price: Price in U.S. dollars
 5. carat: Unit of measurement used to describe the weight of a diamond
 6. cut: Facets, symmetry, and reflective qualities of a diamond
 7. color: Natural color or lack of color visible within a diamond, based on the GIA grade scale
 8. clarity: Visibility of natural microscopic inclusions and imperfections within a diamond
 9. report: Diamond certificate or grading report provided by an independent gemology lab
 10. type: Natural or lab created diamonds
 11. date_fetched: Date the data was fetched

## Repository files
- `notebook.ipynb` jupyter notebook with EDA and models development
- `train.py` a python script to train a model
- `model=13.bin` binary file with trained model and features encoders
- `diamonds_dataset.csv` dataset
- `Pipfile` and `Pipfile.lock` files with dependencies for environment
- `predict.py` a python script to create a web service based on the model
- `request.py` a python script to send a request to the service and check it's work
- `Dockerfile` a script to generate docker container
- `request_cloud.py` a python script to send a request to the cloud service
- `request_streamlit.py` a python file with frontend part to make requests 
- `requirements.txt` requirements for `request_streamlit.py` file

## How to install dependencies

Clone the project

```bash
git clone https://github.com/boiarchuk-m/Diamonds-price-prediction
```

Go to the project directory

```bash
cd Diamonds-price-prediction
```


Install needed packages to the virtual environment

```bash
pipenv install
```
Activate virtual environment

```bash
pipenv shell
```

## Host the server

You can host the server using this command

```bash
python predict.py
```

Or using waitress 

```bash
waitress-serve --listen=0.0.0.0:9696 predict:app
```

## Making a prediction

To check the work of the web server you can use file `request.py` 
Just run it with this command

```bash
python request.py
```


In the output you will get the price of the diamond

```bash
{'Value': 445.126}

```

## Docker containerization

You can run a web server using docker. First you need to create a docker image using the Dockerfile. Go to the project folder and run this command

```bash
docker build -t diamonds .
```
Now, just use the command below and the model will be served to your local host, and you can make a prediction in the same way as explained above

```bash
docker run -it -p 9696:9696 diamonds
```

## Cloud deployment

The web service was deployed to the google cloud and here are steps how I made it.

First you need to install the gcloud CLI.There is an instructions form google how to make it: https://cloud.google.com/sdk/docs/install

Then you need to open the Google Cloud CLI shell and log in your account 

```bash
gcloud auth login
```
After this you need to configure Docker 
```bash
gcloud auth configure-docker
```
Then, create a project
```bash
gcloud config set project <project_id>
```
Tag an image 
```bash
docker tag image gcr.io/<project_id>/image
```
Push image to Google Container Registry

```bash
docker push gcr.io/<project_id>/image
```

Here is a url to test this cloud service:
https://diamonds-l4pdyslp4q-uc.a.run.app/predict
Also, you can use the file `request_cloud.py` that uses this link to make a request.

Also, I have created a frontend part for deployed service using streamlit. So you can just open this link and try an app without any instalations. https://diamonds-price-prediction-bpzjufvgczsas5jd67xw6r.streamlit.app/ 
