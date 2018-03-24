from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Team, Player, User

engine = create_engine('sqlite:///basketballteam.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create User
User1 = User(name="DanSLuong", email="hayate58@gmail.com",
             picture='http://www.daviker.co.uk/wp-content/uploads/profile-blank.png')
session.add(User1)
session.commit()


team1=Team(user_id=1,name='Raptors',city='Toronto',state='Canada',conference='East')
session.add(team1)


player1=Player(user_id=1,firstName="Anunoby",lastName="OG",playerNum="3",position="F",height="6'8",weight="232",age="20",college="Indiana",birthplace="London,England",role="Bench",team=team1)
session.add(player1)
session.commit()



print "added players"