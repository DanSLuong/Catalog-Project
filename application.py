from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player

app = Flask(__name__)

engine = create_engine('sqlite:///basketballteam.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Homepage. List all of the NBA teams
@app.route('/')
@app.route('/teams/')
def showTeams():
    teams = session.query(Team).all()
    return render_template('teams.html', teams = teams)

# Create a new team
@app.route('/teams/new/', methods=['GET', 'POST'])
def newTeam():
    if request.method = 'POST':
        newTeam = Team(name=request.form['name'])
        session.add(newTeam)
        session.commit()
        return redirect(url_for('showTeams'))
    else:
        return render_template('newTeam.html')

# Edit a Team
@app.route('/teams/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeam(team_id):
    editTeam = session.query(Team).filter_by(id=team_id).one()
    if request.form['name']:
        editTeam.name = request.form['name']
        return redirect(url_for('showTeams'))
    else:
        return render_template('editTeam.html', team = editTeam)

# Delete a Team
@app.route('/teams/<int:team_id>/delete/', methods=['GET', 'POST'])
def deleteTeam(team_id):
    teamToDelete = session.query(Team).filter_by(id=team_id).one()
    if request.method = 'POST':
        session.delete(teamToDelete)
        session.commit()
        return redirect('showTeams', team_id=team_id)
    else:
        return render_template('deleteTeam.html', team=teamToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)