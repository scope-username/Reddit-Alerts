FROM python:3

#Create App Directory
WORKDIR /app

#Install Dependencies
COPY src/requirements.txt ./
RUN pip install -r requirements.txt

#Bundle App Source
COPY src /app

#Run the App
CMD ["python3", "script.py"]
