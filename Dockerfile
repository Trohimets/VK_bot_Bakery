FROM python:3.9-slim
RUN mkdir /bot_bakery
COPY requirements.txt /bot_bakery
RUN pip3 install -r /bot_bakery/requirements.txt --no-cache-dir
COPY / /bot_bakery
WORKDIR /bot_bakery
CMD ["python3", "bot.py"] 