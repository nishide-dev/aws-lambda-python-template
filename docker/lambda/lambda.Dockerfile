FROM public.ecr.aws/docker/library/python:3.12.0-slim-bullseye

# requirements-dev.lockからrequirements.txtを生成
COPY requirements-dev.lock /tmp/requirements-dev.lock
RUN --mount=type=cache,target=/root/.cache/pip \
    sed '/^-e file:.*/d' /tmp/requirements-dev.lock > /tmp/requirements.txt

# requirements.txtをコピー
COPY /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.1 /lambda-adapter /opt/extensions/lambda-adapter
COPY . /app
WORKDIR /app

CMD ["python", "src/app.py"]
