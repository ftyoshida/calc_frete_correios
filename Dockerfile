FROM python:3
RUN apt-get update && apt install -y python3-xmltodict
RUN pip3 install cherrypy urllib3 requests xmltodict
COPY calc-frete-ws.py .
EXPOSE 8080
ENTRYPOINT ["python3", "calc-frete-ws.py"]
