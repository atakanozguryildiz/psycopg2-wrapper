def is_crud(sql):
    """Check that given sql is insert , update, delete or select

    :param sql: Sql string to check for is_crud

    :return: Boolean result
    """

    crud = ['insert', 'update', 'delete', 'select']

    if not isinstance(sql, str):
        raise TypeError('`sql` argument is not valid. `sql` must be str.')

    if sql == '':
        raise ValueError('Sql statement is empty')

    parts = sql.split(' ')
    first_part = parts[0]
    lower_first_part = first_part.lower()
    if lower_first_part in crud:
        return True
    return False
