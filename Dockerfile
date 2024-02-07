# Use a imagem base do Python
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY requirements.txt ./
COPY app.py ./
COPY templates/ ./templates

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta em que a aplicação Flask será executada
EXPOSE 5000

# Comando para iniciar a aplicação Flask quando o contêiner for iniciado
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
