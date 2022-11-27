FROM python:3.10.8

EXPOSE 81
WORKDIR /App

RUN apt-get update && \
      apt-get -y install sudo && \
      /usr/local/bin/python -m pip install --upgrade pip

COPY . /App
RUN ["pip","install","streamlit"]
# Run the application:
ENTRYPOINT ["sudo","streamlit", "run", "main.py", "--server.headless=true" ,"--server.port", "80"]
