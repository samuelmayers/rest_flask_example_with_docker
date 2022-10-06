FROM python:3.9-alpine
COPY . /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip install --upgrade pip && pip --no-cache-dir install -r requirements.txt
CMD [ "python","app.py" ]
