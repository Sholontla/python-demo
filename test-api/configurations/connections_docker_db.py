from sqlalchemy import create_engine

# MySQL
# sudo docker run --name testingmysql  -p 3306:3306 -e MYSQL_PASSWORD=testingdata, -e MYSQL_USER=testingdata, -e MYSQL_DATABASE=testingdata -d mysql:latest
PORT = "9191"
MYSQL_ROOT_PASSWORD = "testpsswd"
MYSQL_USER = "testuser"
MYSQL_DATABASE = "testingdata"

engine_mysql_sqlalchemy = create_engine(f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_ROOT_PASSWORD}@{PORT}/{MYSQL_DATABASE}')
engine_mysql_flask_sqlalchemy = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_ROOT_PASSWORD}@{PORT}/{MYSQL_DATABASE}'


# POSRGRE_SQL
# sudo docker run --name testingdata -e POSTGRES_DB=testingdata -e POSTGRES_USER=testingdata -e POSTGRES_PASSWORD=testingdata -p 5432:5432 -h localhost -d postgres:latest
engine_postgre = create_engine(f"postgresql+psycopg2://{POSTGRE_USER}:{POSTGRE_PASSWORD}@{POSTGRE_HOST}:{POSTGRE_PORT}/{POSTGRE_DB_NAME}", echo=False)



# MS_SQL
# sudo docker run -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=tesstingdata --name 'sql1' -p 1401:1433 -v sql1data:/var/opt/mssql -d mcr.microsoft.com/mssql/server:2019-latest
sudo docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -S localhost -U testing -P 'testingdata' -Q 'ALTER LOGIN SA WITH PASSWORD="testingdata"'
engine_sqlserver = create_engine(f'mssql+pymssql://{SQLSERVER_USER}:{SQLSERVER_PASSWORD}@{SQLSERVER_HOST}:{SQLSERVER_PORT}/{SQLSERVER_DB_NAME}')



# REDIS
# docker run --name containerredis -p 6379:6379 -d redis
# docker exec -it containername redis-cli
# set name 'keyname'
# get key
# set nametemp 'exoirekeyname' EX 10 (sec)
# get nametemp
# exists name / nametemp / etc...
# del name 
# append name 'value'
# append name 'secondvalue'
# siscribe newvideos 
# publish newvideos message'
# pucblish edmond 'message'

# MONGO DB
# docker run -d  --name api1mongo  -p 27017:27017 -h localhost -v ~/mongodb:/db/apidb1 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=mongoadmin mongo:latest
# docker run -d --name api1mongo -p 27017:27017 -h localhost -v ~/mongodb:/db/apidb1 mongo:latest

# docker run --name apicassandra -d -e CASSANDRA_BROADCAST_ADDRESS=10.42.42.42 -p 127.0.0.1:9042:9042 cassandra:3.11

# docker run -d 80:80 docker/getting-started

# ORACLE
# sudo docker login
# sudo docker pull store/oracle/database-enterprise:12.2.0.1