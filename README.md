Simple wrapper for executing commands and queries

Features
<ul>
<li>Connection Pool</li>
<li>Client cursor</li>
</ul>

<p>For installing package:</p>
<pre>
pip install psycopg2-wrapper
</pre>

<p>For usage: </p>
<pre>
from psycopg2_wrapper.database import Database
database = Database(host='host_name', database='db_name', user='db_user', password='db_password')
result = database.execute_query('select * from user where id=%s', (1,))
</pre>
