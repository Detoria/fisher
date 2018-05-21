DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:hzw0527@localhost:3306/fisher'  # mysql 数据库 + cymysql 数据库驱动 （pipenv install cymysql）

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
SECRET_KEY = 'uhqwdxxsdfrtghskwhflakskjhrhchfhr'