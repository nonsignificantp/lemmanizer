FROM tiangolo/uvicorn-gunicorn-fastapi

# Copia la aplicacion dentro del container
COPY ./app /app

# Descarga de dependencias
RUN pip install stanza 

# Descarga el modelo ejecutando python desde la linea de comando
RUN python -c "import stanza; stanza.download('es', package='ancora', processors='tokenize,mwt,pos,lemma', verbose = False) "
