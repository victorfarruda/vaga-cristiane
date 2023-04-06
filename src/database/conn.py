import psycopg2


class Conexao(object):
    _db = None

    def __init__(self):
        self._db = psycopg2.connect(
            host='localhost',
            database='database',
            user='postgres_user',
            password='postgres_password'
        )

    def execute(self, sql, *args, **kwargs):
        try:
            cur = self._db.cursor()
            cur.execute(sql, *args, **kwargs)
            self._db.commit()
        except:
            return False
        return True

    def execute_and_commit(self, sql, *args, **kwargs):
        try:
            cur = self._db.cursor()
            cur.execute(sql, *args, **kwargs)
            self._db.commit()
            _id = cur.fetchone()[0]
            return _id
        except:
            return False

    def select_one(self, sql, *args, **kwargs):
        result = None
        try:
            cur = self._db.cursor()
            cur.execute(sql, *args, **kwargs)
            result = cur.fetchone()
        except:
            return None
        return result

    def select_all(self, sql):
        result = None
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            result = cur.fetchall()
        except:
            return None
        return result

    def fechar(self):
        self._db.close()


class Base:
    SQL_CREATE = ''
    SQL_INSERT = ''
    SQL_SELECT_ALL = ''
    SQL_SELECT_LAST = ''

    def __init__(self):
        self.conn = Conexao()
        self.create_table()

    def create_table(self):
        created = self.conn.execute(self.SQL_CREATE)
        if created is not True:
            raise 'Erro com Base de dados'

    def insert_into(self, values):
        return self.conn.execute_and_commit(self.SQL_INSERT, (values,))

    def select_last(self):
        return self.conn.select_one(self.SQL_SELECT_LAST)

    def select_all(self):
        result = self.conn.select_all(self.SQL_SELECT_ALL)
        return result
