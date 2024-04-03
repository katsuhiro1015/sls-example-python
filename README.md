# sls-example-python

sls-example-python

## get started

```bash
git clone https://github.com/katsuhiro1015/sls-example-python.git
cd sls-example-python/app
sls deploy
```

## ECR create repository

AWS Console or (Terraform/Cloudformation/CDK)

name: example-python

## AWS Powertools

document

```bash
https://docs.powertools.aws.dev/lambda/python/latest/
```

### install (local development)

```bash
pip install "aws-lambda-powertools[aws-sdk]"
```

## deploy

### ECR Push

```
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.ap-northeast-1.amazonaws.com
docker tag <IMAGE ID> <ACCOUNT_ID>.dkr.ecr.ap-northeast-1.amazonaws.com/example-python:latest
docker push <ACCOUNT_ID>.dkr.ecr.ap-northeast-1.amazonaws.com/example-python:latest
```

### modify serverless.yml

modify ACCOUNT_ID

```bash
image: <ACCOUNT_ID>.dkr.ecr.ap-northeast-1.amazonaws.com/example-python:latest
```

### serverless deploy

```bash
sls deploy
```