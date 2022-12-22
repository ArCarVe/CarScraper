FROM python:3.10

WORKDIR /car-scraper/

COPY requirements.txt  ./

ENV PIP_CONFIG_FILE pip.conf
ENV TZ=America/Sao_Paulo

RUN groupadd -r carscraper && useradd -r -s /bin/false -g carscraper carscraper && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    apt-get update  && \
    pip install --upgrade pip && \ 
    pip install -r requirements.txt && \
    mkdir /car-scraper/src/ && \
    mkdir /car-scraper/src/log/ 
     
COPY src /car-scraper/src

RUN chown -R carscraper:carscraper /car-scraper

USER carscraper

ENTRYPOINT ["python", "/car-scraper/src/main.py"]