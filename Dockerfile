FROM public.ecr.aws/lambda/python:3.12

COPY app/requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY app/*.py ${LAMBDA_TASK_ROOT}
COPY app/schema/ ${LAMBDA_TASK_ROOT}/schema/

CMD ["handler.hello"]
