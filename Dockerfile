FROM python:3.6

RUN mkdir /service
COPY protobufs /service/protobufs
COPY grpcservice /service/grpcservice

COPY ./requirements.txt /service/grpcservice
COPY ./env.yml /service

WORKDIR /service/grpcservice

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/lastpage.proto

EXPOSE 50051
ENTRYPOINT ["python3", "grpcservice.py"]