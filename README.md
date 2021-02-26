# Project Overview
Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. They are interested in understanding what songs users are listening to.

# Project Repository files
1. song_date file contains metadata about a song and the artist of that song. 
2. log_data file contains activity logs from a music streaming app based on specified configurations.

# Database Design
1. Song Dataset:
1.1 songs - song_id, title, artist_id, year, duration
1.2 artists - artist_id, name, location, latitude, longitude

2. Log dataset:
2.1 songplays - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
2.2 users - user_id, first_name, last_name, gender, level
2.3 Time -  start_time, hour, day, week, month, year, weekday

The songplays is a fact table and other tables are dimension.

# Project Structure
1. test.ipynb displays the first few rows of each table to let you check your database.
2. create_tables.py drops and creates your tables.
3. etl.ipynb reads and processes a single file from song_data and log_data and loads the data into the tables.
4. etl.py reads and processes files from song_data and log_data and loads them into the tables.
5. sql_queries.py contains all your sql queries, and is imported into the last three files above.

# ETL Process (etl.py)
1. Main
Connects to psycopg2 database and executes methods, then calls process_data for song_data and Log_data files

2. process_data
The function is called by the Main, gets file path via input parameter and Loops through file directories, then runs one of the process_log_file or process_song_file

3. process_song_file
This procedure processes a song file whose filepath has been provided as an argument.
It extracts the song information in order to store it into the songs table.
Then it extracts the artist information in order to store it into the artists table.

INPUTS: 
cur the cursor variable
filepath the file path to the song file

4. process_log_file
This procedure processes a log file whose filepath has been provided as an argument.
It extracts the time,user and songplay information in order to store it into the time,user and songplay tables.

INPUTS: 
cur the cursor variable
filepath the file path to the song file

# How To Run the Project
1. Run the create_tables.py to rebuild connection and tables
2. Run etl.py to populate tables
