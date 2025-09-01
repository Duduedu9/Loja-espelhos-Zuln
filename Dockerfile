# Usa uma imagem oficial do Python, versão 3.12, otimizada
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Define variáveis de ambiente para o Python no formato correto
ENV PYTHONUNBUFFERED=1

# Copia o arquivo de requisitos para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Copia todo o resto do código para dentro do container
COPY . .

# Comando padrão para rodar a aplicação quando o container iniciar
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]