-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament

CREATE TABLE players(
	player_id	SERIAL	PRIMARY KEY	NOT NULL,
	name		TEXT			NOT NULL
);

CREATE TABLE matches(
	match_id	SERIAL	PRIMARY KEY				NOT NULL,
	winner		INT	REFERENCES players (player_id)		NOT NULL,
	loser		INT	REFERENCES players (player_id)		NOT NULL
);

CREATE TABLE byes(
	player_id	INT	REFERENCES players (player_id)	NOT NULL,
	bye		TEXT					NOT NULL
);

CREATE VIEW wins AS 
SELECT players.player_id, players.name, count(matches.winner) AS wins 
	FROM players LEFT JOIN matches 
	ON players.player_id=matches.winner 
	GROUP BY players.player_id;

CREATE VIEW losses AS
SELECT players.player_id, players.name, count(matches.loser) AS losses 
	FROM players LEFT JOIN matches 
	ON players.player_id=matches.loser 
	GROUP BY players.player_id;

CREATE VIEW standings AS
SELECT wins.player_id, wins.name, wins.wins, losses.losses, (wins.wins+losses.losses) AS total_matches 
	FROM wins join losses 
	ON wins.player_id=losses.player_id
	ORDER BY wins.wins DESC;	


