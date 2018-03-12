from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Team, Player

engine = create_engine('sqlite:///basketballteam.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

team1 = Team(name='Rockets', city='Houston', state='Texas', conference='West')
session.add(team1)

player1=Player(name="Ryan Anderson", position="PF", role="Bench", team=team1)
session.add(player1)
session.commit()

player2=Player(name="Trevor Ariza", position="SF", role="Starter", team=team1)
session.add(player2)
session.commit()

player3=Player(name="Tarik Black", position="PF", role="Bench", team=team1)
session.add(player3)
session.commit()

player4=Player(name="Markel Brown", position="SG", role="Bench", team=team1)
session.add(player4)
session.commit()

player5=Player(name="Clint Capela", position="C", role="Starter", team=team1)
session.add(player5)
session.commit()

player6=Player(name="Eric Gordon", position="SG", role="Bench", team=team1)
session.add(player6)
session.commit()

player7=Player(name="Gerald Green", position="SG", role="Bench", team=team1)
session.add(player7)
session.commit()

player8=Player(name="James Harden", position="SG", role="Starter", team=team1)
session.add(player8)
session.commit()

player9=Player(name="Nene Hilario", position="C", role="Bench", team=team1)
session.add(player9)
session.commit()

player10=Player(name="R.J. Hunter", position="SG", role="Bench", team=team1)
session.add(player10)
session.commit()

player11=Player(name="Joe Johnson", position="SG", role="Bench", team=team1)
session.add(player11)
session.commit()

player12=Player(name="Luc Mbah a Moute", position="PF", role="Bench", team=team1)
session.add(player12)
session.commit()

player13=Player(name="Chinanu Onuaku", position="C", role="Bench", team=team1)
session.add(player13)
session.commit()

player14=Player(name="Chris Paul", position="PG", role="Starter", team=team1)
session.add(player14)
session.commit()

player15=Player(name="Zhou Qi", position="PF", role="Bench", team=team1)
session.add(player15)
session.commit()

player16=Player(name="PJ Tucker", position="SF", role="Starter", team=team1)
session.add(player16)
session.commit()

player17=Player(name="Brandan Wright", position="PF", role="Bench", team=team1)
session.add(player17)
session.commit()



team2 = Team(name='Raptors', city='Toronto', state='Ontario, Canada', conference='East')
session.add(team2)

player1=Player(name="OG Anunoby", position="SF", role="Bench", team=team2)
session.add(player1)
session.commit()

player2=Player(name="Lorenzo Brown", position="PG", role="Bench", team=team2)
session.add(player2)
session.commit()

player3=Player(name="DeMar DeRozan", position="SG", role="Starter", team=team2)
session.add(player3)
session.commit()

player4=Player(name="Nigel Hayes", position="SF", role="Bench", team=team2)
session.add(player4)
session.commit()

player5=Player(name="Serge Ibaka", position="PF", role="Starter", team=team2)
session.add(player5)
session.commit()

player6=Player(name="Kyle Lowry", position="PG", role="Starter", team=team2)
session.add(player6)
session.commit()

player7=Player(name="Alfonzo McKinnie", position="SF", role="Bench", team=team2)
session.add(player7)
session.commit()

player8=Player(name="CJ Miles", position="SF", role="Bench", team=team2)
session.add(player8)
session.commit()

player9=Player(name="Malcolm Miller", position="SF", role="Bench", team=team2)
session.add(player9)
session.commit()

player10=Player(name="Lucas Nogueira", position="C", role="Bench", team=team2)
session.add(player10)
session.commit()

player11=Player(name="Jakob Poeltl", position="C", role="Bench", team=team2)
session.add(player11)
session.commit()

player12=Player(name="Norman Powell", position="SF", role="Starter", team=team2)
session.add(player12)
session.commit()

player13=Player(name="Malachi Richardson", position="SG", role="Bench", team=team2)
session.add(player13)
session.commit()

player14=Player(name="Pascal Siakam", position="PF", role="Bench", team=team2)
session.add(player14)
session.commit()

player15=Player(name="Jonas Valanciunas", position="C", role="Starter", team=team2)
session.add(player15)
session.commit()

player16=Player(name="Fred VanVleet", position="PG", role="Bench", team=team2)
session.add(player16)
session.commit()

player17=Player(name="Delon Wright", position="PG", role="Bench", team=team2)
session.add(player17)
session.commit()




team3 = Team(name='Timberwolves', city='Minneappolis', state='Minnesota', conference='West')
session.add(team3)

player1=Player(name="Cole Aldrich", position="C", role="Bench", team=team3)
session.add(player1)
session.commit()

player2=Player(name="Nemanja Bjelica", position="PF", role="Bench", team=team3)
session.add(player2)
session.commit()

player3=Player(name="Aaron Brooks", position="PG", role="Bench", team=team3)
session.add(player3)
session.commit()

player4=Player(name="Anthony Brown", position="SF", role="Bench", team=team3)
session.add(player4)
session.commit()

player5=Player(name="Jimmy Butler", position="SG", role="Starter", team=team3)
session.add(player5)
session.commit()

player6=Player(name="Jamal Crawford", position="SG", role="Bench", team=team3)
session.add(player6)
session.commit()

player7=Player(name="Gorgui Dieng", position="C", role="Bench", team=team3)
session.add(player7)
session.commit()

player8=Player(name="Marcus Georges-Hunt", position="SG", role="Bench", team=team3)
session.add(player8)
session.commit()

player9=Player(name="Taj Gibson", position="PF", role="Starter", team=team3)
session.add(player9)
session.commit()

player10=Player(name="Amile Jefferson", position="PF", role="Bench", team=team3)
session.add(player10)
session.commit()

player11=Player(name="Tyus Jones", position="PG", role="Bench", team=team3)
session.add(player11)
session.commit()

player12=Player(name="Justin Patton", position="C", role="Bench", team=team3)
session.add(player12)
session.commit()

player13=Player(name="Derrick Rose", position="PG", role="Bench", team=team3)
session.add(player13)
session.commit()

player14=Player(name="Jeff Teague", position="PG", role="Starter", team=team3)
session.add(player14)
session.commit()

player15=Player(name="Karl-Anthony Towns", position="C", role="Starter", team=team3)
session.add(player15)
session.commit()

player16=Player(name="Andrew Wiggins", position="SF", role="Starter", team=team3)
session.add(player16)
session.commit()



print "added players"