from psycopg2 import pool

from validator import is_crud


class Database(object):

    def __init__(self, host, database, user, password,
                 port=5432, min_connection=1, max_connection=20):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.min_connection = min_connection
        self.max_connection = max_connection
        self._create_connection_pool()

    def _create_connection_pool(self):
        self.connection_pool = pool.ThreadedConnectionPool(
            self.min_connection, self.max_connection,
            user=self.user, password=self.password,
            host=self.host, port=self.port,
            database=self.database)

    def _get_connection(self):
        # Hard push until success
        try:
            connection = self.connection_pool.getconn()
            if connection.closed != 0:
                # Closed
                return _get_connection()
            return connection
        except pool.PoolError:
            return self._get_connection()
        except:
            return self._get_connection()

    def _put_connection(self, con):
        self.connection_pool.putconn(con)

    def _create_cursor(self, con):
        if con.closed != 0:
            con = self._get_connection()
        return con.cursor()

    def _close_cursor(self, crs):
        crs.close()

    def execute_query(self, query, params=None):
        connection = self._get_connection()
        if not is_crud(query):
            connection.autocommit = True
            return self._execute_with_autocommit(connection, query, params)
        return self._execute_without_autocommit(connection, query, params)

    def _execute_with_autocommit(self, connection, query, params):
        cursor = self._create_cursor(connection)
        cursor.execute(query, params)
        if cursor.description:
            all_data = cursor.fetchall()
            self._close_cursor_connection(cursor, connection)
            return all_data
        self._close_cursor_connection(cursor, connection)
        return True

    def _execute_without_autocommit(self, connection, query, params):
        cursor = self._create_cursor(connection)
        cursor.execute(query, params)
        connection.commit()
        if cursor.description:
            all_data = cursor.fetchall()
            self._close_cursor_connection(cursor, connection)
            return all_data
        self._close_cursor_connection(cursor, connection)
        return True

    def _close_cursor_connection(self, cursor, connection):
        self._close_cursor(cursor)
        self._put_connection(connection)
