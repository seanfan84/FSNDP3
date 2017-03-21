#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from functools import wraps


def con(fun2bdecorated):
    @wraps(fun2bdecorated)
    def decoratedFunction(*args, **kwargs):
        conn = psycopg2.connect("dbname=tournament")
        cursor = conn.cursor()
        result = fun2bdecorated(*args, conn=conn, cursor=cursor)
        conn.close()
        return result
    return decoratedFunction


@con
def deleteMatches(conn, cursor):
    """Remove all the match records from the database."""
    # print "Deleting matches"
    cursor.execute(
        "delete from matches"
    )
    conn.commit()


@con
def deletePlayers(conn, cursor):
    """Remove all the player records from the database."""
    cursor.execute(
        "delete from players"
    )
    conn.commit()


@con
def countPlayers(conn, cursor):
    """Returns the number of players currently registered."""
    cursor.execute(
        "select count(*) from players"
    )
    return cursor.fetchone()[0]


@con
def registerPlayer(name, conn, cursor):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    cursor.execute(
        "insert into players(name) values (%s);", (name,)
    )
    conn.commit()


@con
def playerStandings(conn, cursor):
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    cursor.execute(
        "select p.id as id, p.name as name, count(m1.winner) as wins, \
        count(m1.winner) + count(m2.loser) as total \
        from players p \
        left join matches m1 on p.id = m1.winner \
        left join matches m2 on p.id = m2.loser \
        group by p.id \
        order by wins desc;"
    )
    return cursor.fetchall()


@con
def reportMatch(winner, loser, conn, cursor):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost

    """
    cursor.execute(
        "insert into matches(winner,loser) values (\
        %s,%s);", (winner, loser,)
    )
    conn.commit()


@con
def swissPairings(conn, cursor):
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
    cursor.execute(
        "select * from pairing;"
    )
    return cursor.fetchall()
