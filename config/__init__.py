import pymysql
from .settings import LOCAL

if not LOCAL:
    pymysql.install_as_MySQLdb()