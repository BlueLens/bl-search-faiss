FROM bluelens/faiss:ubuntu16-py2

#ENV WEB_CONCURRENCY=4

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get install curl
RUN curl https://s3.ap-northeast-2.amazonaws.com/bluelens-style-index/faiss.index -o /opt/app/faiss/faiss.index

RUN pip install --no-cache-dir gunicorn /usr/src/app

ENV INDEX_FILE /opt/app/faiss/faiss.index

#ENV PYTHONPATH $PYTHONPATH:/usr/src/app/faiss

EXPOSE 8080

CMD ["gunicorn", "-k", "gevent", "--timeout", "200", "-b", "0.0.0.0:8080", "bl_search_faiss:app"]



