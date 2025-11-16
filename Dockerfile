FROM python:3.11-slim

ENV TMPDIR=/tmp
ENV PIP_CACHE_DIR=/tmp/pip_cache

WORKDIR /app

COPY dep_whls/ /dep_whls

COPY codebase/ ./codebase

#RUN pip install --no-index --find-links=/dep_whls -r codebase/requirements.txt

CMD ["/bin/bash"]