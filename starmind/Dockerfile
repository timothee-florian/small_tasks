FROM python:3.8
WORKDIR /app

COPY . .
RUN apt-get update -y
RUN apt-get install -y python-enchant
RUN pip3 install pandas
RUN pip3 install pyenchant


CMD [ "python3", "-m", "./levenshtein_distance.py", "file path", "column of interest", "target word", "wanted distance"]
