FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get upgrade -y
RUN apt-get install git -y
COPY requirements.txt /requirements.txt

# 1. Go to the root directory
WORKDIR /

# 2. Correctly clone the repository using the 'git clone' command
RUN git clone https://github.com/JishuDeveloper/Ultra-Forward-Bot.git

# 3. Move into the folder you just downloaded
WORKDIR /Ultra-Forward-Bot

# 4. Now install the requirements from inside that folder
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"] 
