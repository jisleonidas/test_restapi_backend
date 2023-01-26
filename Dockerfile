# FROM localhost/rockylinux-9-flask
FROM public.ecr.aws/docker/library/rockylinux:9
# FROM registry.access.redhat.com/ubi9/ubi-minimal:latest

RUN dnf install -y python3 python3-pip
# RUN microdnf install -y python3 python3-pip

RUN pip install flask flask_restful pandas

WORKDIR /app

COPY . .

# COPY users.csv .

EXPOSE 5000

ENTRYPOINT ["python3", "api.py"]
