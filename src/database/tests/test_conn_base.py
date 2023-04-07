from unittest.mock import Mock

import pytest


def test_pode_criar_objeto_base():
    from database import conn
    conn.psycopg2 = Mock()
    from database.conn import Base

    base = Base()

    assert isinstance(base, Base)


def test_create_table():
    from database import conn
    conn.psycopg2 = Mock()
    from database.conn import Base

    base = Base()
    base.conn.execute = Mock(return_value=True)
    base.create_table()

    base.conn.execute.assert_called()


def test_create_table_error():
    from database import conn
    conn.psycopg2 = Mock()
    from database.conn import Base

    base = Base()
    base.conn.execute = Mock(return_value=False)
    with pytest.raises(Exception):
        base.create_table()


def test_insert_into():
    from database import conn
    conn.psycopg2 = Mock()
    from database.conn import Base

    base = Base()
    base.conn.execute_and_commit = Mock()
    base.insert_into('asdf')

    base.conn.execute_and_commit.assert_called()


def test_select_last():
    from database import conn
    conn.psycopg2 = Mock()
    from database.conn import Base

    base = Base()
    base.conn.select_um = Mock()
    base.select_last()

    base.conn.select_um.assert_called()


def test_select_all():
    from database import conn
    conn.psycopg2 = Mock()
    from database.conn import Base

    base = Base()
    base.conn.select_todos = Mock()
    base.select_all()

    base.conn.select_todos.assert_called()
