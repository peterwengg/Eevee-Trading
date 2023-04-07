FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
COPY ./Backend/helpers.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./Backend/app.py .
COPY ./Backend/invokes.py .
COPY ./Frontend ../Frontend
COPY ./Backend/helpers.py .

# COPY ./Frontend/templates/Login+Register Page ../Frontend
COPY ./Backend/access_wallet.py .
COPY ./Backend/authenticate.py .
COPY ./Backend/swap.py .
COPY ./Backend/check_order.py .
COPY ./Backend/price.py .
COPY ./Backend/make_transaction.py .
COPY ./Backend/topup.py .
CMD [ "python", "./app.py" ]
