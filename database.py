from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base= declarative_base()
engine = create_engine('sqlite:///User.db', echo = True)

class table(Base):
        __tablename__='User'
        Id = Column(Integer, primary_key=True, autoincrement=True)
        Username = Column(String(100),ForeignKey('userInfo'),unique=True,nullable=False)
        Password = Column(String(100), nullable=False)
        Name= Column(String(100), nullable=False)
        Surname= Column(String(100), nullable=False)
        JobTitle= Column(String(500), nullable=False)
        
        __tablename__='Userstation'
        Id = Column(Integer, primary_key=True, autoincrement=True)
        station= Column(Integer,unique=True,nullable=False)
        training= Column(Boolean, default=False)
        absent= Column(Boolean, default=False)
        standUp= Column(Boolean, default=False)
        
        __tablename__='LinkTable'
        Id = Column(Integer, primary_key=True,autoincrement=True )
        user= relationship('User')
        station= relationship('Userstation')
        
        
        Base.metadata.create_all(bind=engine)

  
    

    
