FROM python:3.6

RUN mkdir res

COPY res/ /home/jovyan/work/res/
COPY templates/* /home/jovyan/work/templates/
COPY api.py /home/jovyan/work

COPY requirements.txt /home/jovyan/work

WORKDIR /home/jovyan/work

RUN pip install -r /home/jovyan/work/requirements.txt


EXPOSE 5000
CMD ["python", "api.py"]

