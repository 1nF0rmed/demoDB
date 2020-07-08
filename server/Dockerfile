FROM python:3-onbuild
COPY . /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt
CMD ["python", "app.py"]