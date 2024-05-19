# Instalar OpenSSH server
RUN apt-get update && apt-get install -y openssh-server

# Criar o diretório de execução do SSH
RUN mkdir /var/run/sshd

# Permitir autenticação por senha
RUN echo 'root:Docker!' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expor a porta 2222 para SSH
EXPOSE 2222

# Iniciar o SSH junto com o app
CMD ["sh", "-c", "/usr/sbin/sshd && python app.py"]
