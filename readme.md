# Python Flask Docker Example

### www.improperintegral.com/article/python-flask-docker-example

### To Get Started
+ py -m venv environment 
+ .\env\Scripts\activate
+ pip install sklearn pandas numpy flask matplotlib (or use requirements.txt)


### Basic Structure
+ train.py - Generates pickled model files to /models folder
+ serve.py - Flask API to serve everything in the /models folder
+ Dockerfile - Generates Docker image containing models folder and serve.py logic