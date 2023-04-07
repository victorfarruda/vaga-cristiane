#Considerações sobre os serviços

#Serviço gateway de entrada
Este serviço recebe uma string do serviço cliente e salva na tabela "comando_recebido".
Ele também cria automaticamente as tabelas de "comando_recebido" e "comando_pendente".
Um comando pendente inicial é inserido para a aplicação poder funcionar.
É possível alterar o comando pendente a ser inserido manualmente no environment do docker-compose.
Este serviço roda de 20 em 20 segundos.
```
docker-compose build entrada
docker-compose up entrada
```

#Serviço cliente gateway de entrada
Este serviço envia uma string (comando) no formado campo1;campo2;campo3;campo4 a ser salvo na tabela "comando_recebido".
O comando (string) a ser enviado pode ser alterado pelo environment do docker-compose.
Este serviço deve ser executado manualmente.
```
docker-compose build entrada
docker-compose build cliente
docker-compose up cliente
```

#Serviço de tratamento de comando
Este serviço cria automaticamente a tabela "tratamento_comando_recebido".
O Serviço de tratamento monitora a tabela de "comando_recebido" e salva os registros que não foram processados na tabela "tratamento_comando_recebido".
Este serviço roda de 20 em 20 segundos.
```
docker-compose build tratamento
docker-compose up tratamento
```
