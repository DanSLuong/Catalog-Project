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
    if request.method == 'POST':
        newTeam = Team(name=request.form['name'], city=request.form['city'], state=request.form['state'], conference=request.form['conference'])
        session.add(newTeam)
        session.commit()
        return redirect(url_for('showTeams'))
    else:
        return render_template('newTeam.html')

# Edit a Team
@app.route('/teams/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeam(team_id):
    editTeam = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editTeam.name = request.form['name']
        if request.form['city']:
            editTeam.city = request.form['city']
        if request.form['state']:
            editTeam.state = request.form['state']
        if request.form['conference']:
            editTeam.conference = request.form['conference']
        session.add(editTeam)
        session.commit()
        return redirect(url_for('showTeams'))
    else:
        return render_template('editTeam.html', team = editTeam)

# Delete a Team
@app.route('/teams/<int:team_id>/delete/', methods=['GET', 'POST'])
def deleteTeam(team_id):
    teamToDelete = session.query(Team).filter_by(id=team_id).one()
    if request.method == 'POST':
        session.delete(teamToDelete)
        session.commit()
        return redirect('showTeams', team_id=team_id)
    else:
        return render_template('deleteTeam.html', team=teamToDelete)

# List the players of the selected team
@app.route('/teams/<int:team_id>/players/')
@app.route('/teams/<int:team_id>/')
def showPlayers(team_id):
    team = session.query(Team).filter_by(id=team_id).one()
    players = session.query(Player).filter_by(team_id=team_id).all()
    return render_template('players.html', players=players, team=team)

# Add a new player
@app.route('/teams/<int:team_id>/players/new/', methods=['GET', 'POST'])
def newPlayers(team_id):
    if request.method == 'POST':
        newPlayer = Player(name=request.form['name'], position=request.form['position'], role=request.form['role'], team_id=team_id)
        session.add(newPlayer)
        session.commit()
        return redirect(url_for('showPlayers', team_id=team_id))
    else:
        return render_template('newplayers.html', team_id=team_id)
    return render_template('newPlayers.html', team=team)

# Edit a player
@app.route('/teams/<int:team_id>/players/<int:player_id>/edit/', methods=['GET', 'POST'])
def editPlayer(team_id, player_id):
    editPlayer = session.query(Player).filter_by(id=player_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editPlayer.name = request.form['name']
        if request.form['position']:
            editPlayer.position = request.form['position']
        session.add(editPlayer)
        session.commit()
        return redirect(url_for('showPlayers', team_id=team_id))
    else:
        return render_template('editplayerinfo.html', team_id=team_id, player_id=player_id, player=editPlayer)

# Delete a player
@app.route('/teams/<int:team_id>/players/<int:player_id>/delete/', methods=['GET', 'POST'])
def deletePlayer(team_id, player_id):
    playerToDelete = session.query(Player).filter_by(id=player_id).one()
    if request.method == 'POST':
        session.delete(playerToDelete)
        session.commit()
        return redirect(url_for('showPlayers', team_id=team_id))
    else:
        return render_template('deleteplayer.html', player=playerToDelete)





if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)