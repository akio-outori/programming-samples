#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from contextlib import contextmanager

def connect():
	"""Connect to the PostgreSQL database.  Returns a database connection."""
	return psycopg2.connect("dbname=tournament")

@contextmanager	
def cursor():
	"""Function to replace with statements based on feedback.  Provides
	context to with statements that don't have an __exit__ method.
	"""
	DB	= connect()
	cursor	= DB.cursor()
	try:
		yield cursor
	except:
		raise
	else:
		DB.commit()
	finally:
		cursor.close()
		DB.close()

def deleteMatches():
	"""Remove all the match records from the database."""
	with cursor() as query:
		query.execute("DELETE FROM matches")

def deletePlayers():
	"""Remove all the player records from the database."""
	with cursor() as query:
                query.execute("DELETE FROM players")

def countPlayers():
	"""Returns the number of players currently registered."""
	with cursor() as query:
		query.execute("SELECT count(player_id) as num_players FROM players")
		result = query.fetchall()

	return result[0][0]

def registerPlayer(name):
	"""Adds a player to the tournament database.
  
	The database assigns a unique serial id number for the player.  (This
	should be handled by your SQL database schema, not in your Python code.)
  
	Args:
	name: the player's full name (need not be unique).
	"""
	with cursor() as query:
		values	= (name, )
		query.execute("INSERT INTO players (name) values (%s)", values)

def playerStandings():
	"""Returns a list of the players and their win records, sorted by wins.

	The first entry in the list should be the player in first place, or a player
	tied for first place if there is currently a tie.

	Returns:
	
	A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
   	"""
	with cursor() as query:
		query.execute("SELECT player_id, name, wins, total_matches from standings")
		results = query.fetchall()
		
	return results

def reportMatch(winner, loser):
	"""Records the outcome of a single match between two players.

	Args:
	
	winner:  the id number of the player who won
	loser:  the id number of the player who lost
	"""
	with cursor() as query:
		values	= (winner, loser)
		query.execute("INSERT INTO matches (winner, loser) values (%s, %s)", values)

def preventRematch(player1, player2):
	"""Simple method to check for repeat matches.  Return True if
	the pair has already faced off, return False if they havent.
	This is done in the database by looking for winner/loser pairs
	in the matches table.  Both possible permutations are checked.
	"""
	
	with cursor() as query:
		query_string	= """
		SELECT match_id 
		FROM matches 
		WHERE (winner = %s AND loser = %s) 
		OR (winner = %s AND loser = %s);
		"""
		values	= (player1, player2, player2, player1)
		query.execute(query_string, values)	
		results	= query.fetchall()

	result = True if results else False
	return result

def assignPlayer(standings):
	"""Assign a player by removing the first player from the list 
	returned by the database and returning that player's data
	"""
	return standings.pop(0)
 
def assignBye(player):
	"""Assign a Bye to a skipped player if a Bye hasn't already been assigned to them.
	This is done by checking the byes table for a row already matching the player_id
	of the player being checked.  If this returns nothing, then a bye is inserted.
	"""
	with cursor() as query:
		values	= (player, )
		query.execute("SELECT player_id from byes where player_id = %s;", values)
		result	= query.fetchall()
	
	if result:
		with cursor() as query:
			bye	= "round %s" % int(player[3] + 1)
			values	= (player[0], bye)
			query.execute("INSERT INTO byes (player_id, bye) values (%s, %s);", values)
		
		return True
	else:
		return False

def swissPairings():
	"""Returns a list of pairs of players for the next round of a match.
  
	Assuming that there are an even number of players registered, each player
	appears exactly once in the pairings.  Each player is paired with another
	player with an equal or nearly-equal win record, that is, a player adjacent
	to him or her in the standings.
  
	Returns:
	
	A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
	"""

	standings	= playerStandings()
	pairings	= []

	""" Tried to find a simple solution for this.
	Basically, players are assigned via their rankings
	in the standings table of the database.  

	The preventRematch() method checks to see if this pair of 
	players has already faced off in the tournament.  If so, 
	we try to assign player2 (second place) a bye.

	If that player already has a bye, then they're inserted
	back into the matching list in the second slot, effectively
	moving them to the next match (they're forced to face off
	against the person in the next position down, i.e. - the person
	in fourth place).

	Player1 in the initial matchup then faces off against the player
	in third place.  So the logic ends up looking like:

	Player1 vs Player3
	Player2 vs Player4
	"""
	while len(standings) >= 1:

		player1	= assignPlayer(standings)
		player2 = assignPlayer(standings)

		if preventRematch(player1[0], player2[0]) == True:
			if assignBye(player2)	== False:
				standings.insert(1, player2)
			player2	= assignPlayer(standings)

		pairings.append((player1[0], player1[1], player2[0], player2[1]))

	return pairings

