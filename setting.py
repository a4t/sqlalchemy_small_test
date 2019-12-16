import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import scoped_session


DATABASE = 'mysql://%s:%s@%s:%s/%s' % (
    os.environ['username'],
    os.environ['password'],
    os.environ['host'],
    os.environ['port'],
    os.environ['database'],
)

engine = create_engine(
    name_or_url=DATABASE,
    connect_args={'charset': 'utf8mb4'},
    pool_recycle=10,
)


session = scoped_session(
  sessionmaker(
        autocommit = False,
        bind = engine
    )
)
