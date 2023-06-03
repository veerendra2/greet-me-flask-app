FROM python:3.8-alpine
ADD src/ ./src
ADD setup.py setup.py
RUN pip3 install -e .
CMD [ "greet_me" ]