FROM python:3.12

WORKDIR /bolokh

COPY . .

ENV SURNAME=bolokh

CMD ["bash"]