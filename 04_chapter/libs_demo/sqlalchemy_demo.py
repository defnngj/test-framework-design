# sqlalchemy_demo.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.orm import sessionmaker


# 数据库连接
engine = create_engine("mysql+pymysql://root:198876@localhost/dev4",
                       connect_args={'charset': 'utf8'})
Session = sessionmaker(bind=engine)
s = Session()

Base = declarative_base()


class User(Base):
    """User表对象"""

    __tablename__ = 'user'  # 定义表名

    # 定义字段类型
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(100))
    email = Column(String(100))

    def __repr__(self):
        return "<id:%s name:%s email:%s>" % (self.id, self.name, self.email)


# 查询user表
user = s.query(User).filter(User.name == 'admin').first()
print(f"id:{user.id}, name:{user.name}, email:{user.email}")

