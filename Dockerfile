FROM python:3.8

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install -r requirements.txt

COPY . /api

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]

# docker build -t cocoroiki-api .
# docker tag cocoroiki-api yumekiti/cocoroiki-api
# docker push yumekiti/cocoroiki-api
# docker run -it --rm -p 8080:8080 cocoroiki-api
