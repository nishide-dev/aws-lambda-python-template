FROM public.ecr.aws/docker/library/python:3.12.0-slim-bullseye
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.1 /lambda-adapter /opt/extensions/lambda-adapter

# コピーしてrequirements.txtを作成
COPY requirements-dev.lock /tmp/requirements-dev.lock
RUN sed '/^-e file:.*/d' /tmp/requirements-dev.lock > requirements.txt

COPY . /app
WORKDIR /app

# requirements.txtをインストール
RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "src/app.py"]
