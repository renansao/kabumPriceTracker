import psycopg2

class Conexao():
    _db=None

    def __init__(self):
        self._db = psycopg2.connect(host='localhost', database='PitaoBotPrd', user='postgres', password='123')

    def executeQuery(self, query):
        try:
            cur = self._db.cursor()
            cur.execute(query)
            rs = cur.fetchall()
            cur.close()
            return rs
        except Exception as e:
            print(e)
            return False

    def executeInsert(self, query):
        try:
            cur = self._db.cursor()
            cur.execute(query)
            cur.close()
            self._db.commit()
            return True
        except Exception as e:
            print(e)
            return False