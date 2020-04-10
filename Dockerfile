FROM python:3
RUN pip install --upgrade pip
COPY dist/ /tmp/dist/
RUN cd /tmp/dist/ && python setup.py test && pip install .
RUN rm -rf /tmp/dist
ENTRYPOINT ["unidoc-utf16"]
WORKDIR /data
CMD ["-h"]
