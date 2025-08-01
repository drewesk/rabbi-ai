FROM continuumio/miniconda3

WORKDIR /app

COPY conda.yaml .

RUN conda env update -n base -f ./conda.yaml --prune

COPY . .

CMD ["streamlit", "run", "App.py"]