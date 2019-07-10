# First, make sure only the first line in serve.py is uncommented
    # app.run(debug=False, host='0.0.0.0', port=5000)      # Use for production with Docker
    # app.run(debug=True, port=5000)                       # Use for development / debug


FROM ubuntu:18.10
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN pip3 install uwsgi
RUN pip3 install flask
RUN pip3 install numpy
RUN pip3 install sklearn
COPY ./models ./app/models
COPY ./serve.py ./app
WORKDIR ./app
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["serve.py"]

# docker build -t sklearn-serving-image:latest .
# docker run -d -p 5000:5000 --restart always sklearn-serving-image