import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    # teams = relationship("Team", backref="user")
    # players = relationship("Player", backref="user")


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(250), nullable=False)
    conference = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref='team')


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return{
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'conference': self.conference,
            'id': self.id,
        }


class Player(Base):
    __tablename__ = 'player'

    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    playerNum = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True)
    position = Column(String(250))
    height = Column(String(250))
    weight = Column(String(250))
    age = Column(Integer, nullable=False)
    college = Column(String(250))
    birthplace = Column(String(250))
    role = Column(String(250))
    
    team_id = Column(Integer, ForeignKey('team.id'))
    team = relationship(Team, backref=backref('player', cascade='all, delete'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref='items')


    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return{
            'firstName': self.firstName,
            'lastName': self.lastName,
            'playerNum': self.playerNum,
            'position': self.position,
            'height': self.height,
            'weight': self.weight,
            'age': self.age,
            'college': self.college,
            'birthplace': self.birthplace,
            'role': self.role,
            'id': self.id,
        }


engine = create_engine('sqlite:///basketballteam.db')

Base.metadata.create_all(engine)
