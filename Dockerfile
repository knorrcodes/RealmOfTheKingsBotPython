FROM python:3.9.0
COPY . /work
WORKDIR /work
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "src/bot.py"]