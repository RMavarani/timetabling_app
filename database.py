from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base= declarative_base()
engine = create_engine('sqlite:///User.db', echo = True)

class table(Base):
        __tablename__='User'
        Id = Column(Integer, primary_key=True)
        Username = Column(String(100),ForeignKey('userInfo'),unique=True,nullable=False)
        Password = Column(String(100), nullable=False)
        Sex= Column(String(50), nullable=False)
        Email= Column(String(500), nullable=False)
        Name= Column(String(100), nullable=False)
        Surname= Column(String(100), nullable=False)
        JobTitle= Column(String(500), nullable=False)
        
        __tablename__='Userstation'
        Id = Column(Integer, primary_key=True)
        station= Column(Integer,unique=True,nullable=False)
        Training= Column(Boolean, nullable=False)
        absent= Column(Boolean, default=False)

        __tablename__='LinkTable'
        Id = Column(Integer, primary_key=True)
        user= relationship('User')
        station= relationship('Userstation')
        
        
        Base.metadata.create_all(bind=engine)

  
    

    
