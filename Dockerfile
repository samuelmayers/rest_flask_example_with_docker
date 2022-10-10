FROM python
WORKDIR /usr/src/app
COPY . /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt
CMD [ "python","/usr/src/app/app.py" ]
