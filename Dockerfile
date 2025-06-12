FROM registry.cn-hangzhou.aliyuncs.com/alex_pc_docker/python:3.12-slim

WORKDIR /opt

COPY . .

RUN pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

CMD ["python","app.py"]
