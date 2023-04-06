SQL_CREATE_TABLE_COMANDO_PENDENTE = """
CREATE TABLE IF NOT EXISTS COMANDO_PENDENTE (
    id serial primary key,
    CAMPOS varchar(1024) 
);
"""

SQL_INSERT_COMANDO_PENDENTE = f"""
INSERT INTO COMANDO_PENDENTE
VALUES (DEFAULT, %s) 
RETURNING id;
"""

SQL_SELECT_ALL_COMANDO_PENDENTE = """
SELECT * FROM COMANDO_PENDENTE;
"""


SQL_CREATE_TABLE_TRATAMENTO_COMANDO_RECEBIDO = """
CREATE TABLE IF NOT EXISTS TRATAMENTO_COMANDO_RECEBIDO (
    id serial primary key,
    CAMPO1 varchar(256), 
    CAMPO2 varchar(256), 
    CAMPO3 varchar(256), 
    CAMPO4 varchar(256)
);
"""

SQL_INSERT_TRATAMENTO_COMANDO_RECEBIDO = f"""
INSERT INTO TRATAMENTO_COMANDO_RECEBIDO
VALUES (DEFAULT, %s, %s, %s, %s)
RETURNING id;
"""

SQL_SELECT_ALL_TRATAMENTO_COMANDO_RECEBIDO = """
SELECT * FROM TRATAMENTO_COMANDO_RECEBIDO;
"""

SQL_CREATE_TABLE_COMANDO_RECEBIDO = """
CREATE TABLE IF NOT EXISTS COMANDO_RECEBIDO (
    id serial primary key,
    CAMPOS varchar(1024),
    PROCESSADO BOOLEAN NOT NULL DEFAULT FALSE 
);
"""

SQL_INSERT_COMANDO_RECEBIDO = f"""
INSERT INTO COMANDO_RECEBIDO
VALUES (DEFAULT, %s, False)
RETURNING id;
"""

SQL_SELECT_ALL_COMANDO_RECEBIDO = """
SELECT * FROM COMANDO_RECEBIDO WHERE PROCESSADO IS False;
"""

SQL_SELECT_BY_ID_COMANDO_RECEBIDO = """
SELECT * FROM COMANDO_RECEBIDO WHERE ID = %s;
"""

SQL_UPDATE_COMANDO_PROCESSADO = """
UPDATE COMANDO_RECEBIDO 
SET PROCESSADO = True
WHERE ID = %s;
"""