-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

create database tournament;

\c tournament;

CREATE table players (
	id serial primary key,
	name text,
	time timestamptz default CURRENT_TIMESTAMP
);


Insert into players(name) values ('user1');
Insert into players(name) values ('user2');
Insert into players(name) values ('user3');
Insert into players(name) values ('user4');
Insert into players(name) values ('user5');
Insert into players(name) values ('user6');


CREATE TABLE matches (
	id serial primary key,
	winner integer references players,
	loser integer references players,
	time timestamptz default CURRENT_TIMESTAMP
) ;


insert into matches(winner,loser) values (1,2);
insert into matches(winner,loser) values (3,4);
insert into matches(winner,loser) values (5,6);
insert into matches(winner,loser) values (1,3);
insert into matches(winner,loser) values (1,5);


-- perfect example for outer left join multiple tables
create view playerstanding as
	select p.id as id, p.name as name, count(m1.winner) as wins, count(m2.loser) as loses, count(m1.winner) + count(m2.loser) as total
	from 
		players p 
		left join matches m1 on p.id = m1.winner
		left join matches m2 on p.id = m2.loser
	group by p.id
	order by wins desc;

-- perfect example for window functions
-- https://www.postgresql.org/docs/current/static/functions-window.html
-- this row_number() is Window Functions, the syntax of window function requires over(function)
-- which defines the order for calculation. This is different to display order
-- you can use order by sql to get a different display order.
create view ladder as 
	select playerstanding.id, playerstanding.name , ceiling(1.0 * row_number() over(order by wins, Id) / 2) as ladder 
	from playerstanding 
	order by ladder asc;


-- perfect example for self joint
create view pairing as
	select a.id as id1, a.name as name1, b.id as id2, b.name as name2
	from ladder as a 
	join ladder as b on a.ladder = b.ladder and a.id > b.id
	order by a.ladder asc;






-- create view wins as
-- 	select players.id as id, players.name as name, count(matches.id) as wins
-- 	from players left join matches 
-- 	on players.id = matches.winner
-- 	group by players.id
-- 	order by wins desc;

-- create view loses as
-- 	select players.id as id, players.name as name, count(matches.id) as loses
-- 	from players left join matches 
-- 	on players.id = matches.loser
-- 	group by players.id
-- 	order by loses desc;


-- create view playerstanding as
-- 	select players.id as id, players.name as name, matches.id as matchid from players left join matches on players.id = matches.winner;


