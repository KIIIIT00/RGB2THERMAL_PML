FROM python:3.12

# Set the working directory
WORKDIR /workspace

ENV PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    HF_HOME=/workspace/.cache/huggingface

ENV LANG=C.UTF-8

COPY requirements.txt /workspace/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /workspace/requirements.txt

CMD ["/bin/bash"]