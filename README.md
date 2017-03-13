# FSNDP3 - Full Stack Nano Degree Project 3: Tournament

This project is a backend database for a tournament using swiss paring system.
The project use postgreSQL, and python.

## Prerequisites
*Install VirtialBox and Vagrant

*Use a command line console which supports SSH (Linux commandline or git bash)

h## Getting Started
*clone the repository to your local machine
*in command line window, navigate to the repository
*Change directory to the directory which has Vagrantfile in it, and run
```
vagrant up
```
*If vagrant is up successfully, run
```
vagrant ssh
```
then type
```
cd /vagrant/tournament
```

## Create the database
Type the following command to create the database under this directory
```
psql tournament.sql
```
This creates the database and establish the connection too. Type
```
\q
```
to get back to shell, or type 
```
help
```
for more information if you want to play around with the database.

### However, I do not recommand you to do so.


## Tournament.py File
There are 7 functions you can call to manipulate data
### 1. registerPlay(name)
Adds a player to the tournament database.
### 2. deletePlayers()
Remove all the player records from the database
### 3. countPlayers()
Returns the number of players currently registered.
### 4. playerStandings()
Returns a list of the players and their win records, sorted by wins.
### 5. reportMatch(winner,loser)
Records the outcome of a single match between two players.
### 6. delateMatch()
Remove all the match records from the database.
### 7. swissParings()
Returns a list of pairs of players for the next round of a match

## Tournament_test.py
This module is provided by Udacity in order to quickly test the above functions.

## Authors

* **Sean Fan** - *Initial work* - [SeanFan84](https://github.com/seanfan84)

## License

This project is not licensed.

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
