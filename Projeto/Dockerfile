# Use a imagem oficial do Python como base
FROM python:3.12

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o conteúdo atual do diretório para o diretório de trabalho no contêiner
COPY . /app

# Instale os pacotes necessários listados no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 8000 para acesso externo
EXPOSE 8000

# Defina a variável de ambiente
ENV PORT 8000

# Comando para iniciar o aplicativo usando Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]
