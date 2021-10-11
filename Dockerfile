FROM python:3.7-slim
RUN apt-get update && apt-get install build-essential -y
MAINTAINER Eren-Ajani Tshimanga <ajanitshimanga@berkeley.edu>
COPY . .
RUN python3 app.py
# RUN make /contacts-db
CMD ["cat", "count.txt"]
# CMD python3 /contacts-db/helloworld.py
