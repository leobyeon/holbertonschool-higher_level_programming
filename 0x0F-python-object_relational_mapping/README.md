#  0x0F. Python - Object-relational mapping
---


## Description
This project in the High Level Programming series is about:
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table


## Files
---
File|Task
---|---
0-select_states.py | Lists all states from the database hbtn_0e_0_usa
1-filter_states.py | Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
2-my_filter_states.py |  Displays all values in the states table where name matches the argument
3-my_safe_filter_states.py | Display values and prevent a SQL injection
4-cities_by_state.py | Lists all cities from the database hbtn_0e_4_usa
5-filter_cities.py | Take in the name of a state and list all cities of that state
6-model_state.py | Start link class to table in database
7-model_state_fetch_all.py | Lists all State objects from the database hbtn_0e_6_usa
8-model_state_fetch_first.py | Prints the first State object from the database hbtn_0e_6_usa
9-model_state_filter_a.py | Lists all State objects that contain the letter a from hbtn_0e_6_usa
10-model_state_my_get.py | Prints the State object with the name passed as argument from hbtn_0e_6_usa
11-model_state_insert.py | Adds the State object Louisiana to the database hbtn_0e_6_usa
12-model_state_update_id_2.py | Change the name of a State object from the database hbtn_0e_6_usa
13-model_state_delete_a.py | Deletes all State objects with a name containing the letter a from hbtn_0e_6_usa
14-model_city_fetch_by_state.py | Prints all City objects from hbtn_0e_14_usa
model_state.py | Class definition of a State and an instance Base = declarative_base()
model_city.py | Class definition of a City
0-select_states.sql | Example script that creates a states table in hbtn_0e_0_usa with some data
4-cities_by_state.sql | Example script that creates states table in hbtn_0e_4_usa with some data
6-model_state.sql | Example script that creates a database hbtn_0e_6_usa
7-model_state_fetch_all.sql | Example script that insert states
14-model_city_fetch_by_state.sql | Example script that creates database hbtn_0e_14_usa, tables states and cities + some data


## Author
* Leo Byeon
