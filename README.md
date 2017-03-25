# FSNDP3 - Full Stack Nano Degree Project 3: Tournament

This project is a backend database for a tournament using swiss paring system.
To run the project, you need to have virtualbox, vagrant installed.

The virtualbox envirionment will be configured by vagrant.
The vagrant configuration files are provided by Udacity full stack nano degree project 3 or 4.

## Prerequisites
* Install VirtialBox and Vagrant

* Use a command line console which supports SSH (Linux commandline or git bash)

## Getting Started
* clone the repository to your local machine
* in command line window, navigate to the repository
* Change directory to the directory which has Vagrantfile in it, and run
```
vagrant up
```
* If vagrant is up successfully, run
```
vagrant ssh
```
* After you login with ssh, change directory by typing:
```
cd /vagrant/tournament
```

## Setting up the database
Type the following command to create the database under this directory
```
psql -f tournament.sql
```
The script will try to delete database 'tournament' if it exists. then create the database, tables, and views from scratch.

## Runing the test file
type the following command in the command window to see the test result of this course.
```
python tournament_test.py
```

# Security
All the arguments are properly escaped with psycopg2 query parameters.

# Extra information
## About Tournament.py File
There are 7 functions you can call to perform certain operations to the database.
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

## Authors

* **Sean Fan** - *Initial work* - [SeanFan84](https://github.com/seanfan84)

## License

This project is not licensed.

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
