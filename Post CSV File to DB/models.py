from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class TeamsData(Base):  
    __tablename__ = "Scraped data on teams"  
    
    ID = Column(Integer, primary_key=True, unique= True)
    name = Column(String, index=True)  
    wins= Column(Integer, index=True)
    losses = Column(Integer, index=True)
    goals_for = Column(Integer, index=True)
    goals_against = Column(Integer, index=True)
