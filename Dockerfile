FROM python
COPY . /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip3 --no-cache-dir install -r requirements.txt
CMD [ "python","/usr/src/app/app.py" ]
