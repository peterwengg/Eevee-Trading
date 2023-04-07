FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
COPY ./Backend/helpers.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./Backend/access_wallet.py .
COPY ./Backend/helpers.py .
CMD [ "python", "./access_wallet.py"]
