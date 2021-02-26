# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES
# songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
                             (songplay_id serial PRIMARY KEY,
                              start_time bigint not null, 
                              user_id int not null, 
                              level varchar,
                              song_id varchar, 
                              artist_id varchar,
                              session_id int,
                              location varchar, 
                              user_agent varchar)
""")

# user_id, first_name, last_name, gender, level
user_table_create = ("""CREATE TABLE IF NOT EXISTS users
                               (user_id int PRIMARY KEY, 
                                 first_name varchar, 
                                 last_name varchar,
                                 gender varchar, 
                                 level varchar)
""")

# song_id, title, artist_id, year, duration
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs
                               (song_id varchar PRIMARY KEY, 
                                title varchar, 
                                artist_id varchar, 
                                year int,
                                duration numeric)
""")

# artist_id, name, location, lattitude, longitude
artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists
                                 (artist_id varchar PRIMARY KEY, 
                                  name varchar, 
                                  location varchar,
                                  latitude varchar, 
                                  longitude varchar)
""")

# start_time, hour, day, week, month, year, weekday
time_table_create = ("""CREATE TABLE IF NOT EXISTS time
                                  (start_time time PRIMARY KEY, 
                                    hour int, 
                                    day int, 
                                    week int, 
                                    month int, 
                                    year int, 
                                    weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays (start_time, user_id, 
                              level,song_id, artist_id,session_id,
                              location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)""")

user_table_insert = ("""insert into users(user_id,first_name,last_name,gender,level) VALUES (%s, %s, %s, %s, %s) 
                                      ON CONFLICT (user_id) DO UPDATE SET level = excluded.level""")


song_table_insert = ("""insert into songs (song_id, title, artist_id,year,duration) VALUES (%s, %s, %s, %s, %s) 
                                      ON CONFLICT (song_id) DO NOTHING""")

artist_table_insert = ("""insert into artists(artist_id,name,location,latitude,longitude) VALUES (%s, %s, %s, %s, %s) 
                                      ON CONFLICT (artist_id) DO NOTHING""")

time_table_insert = ("""insert into time(start_time,hour,day,week,month,year,weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
                                      ON CONFLICT (start_time) DO NOTHING""")

# FIND SONGS

song_select = ("""select s.song_id,a.artist_id from songs s 
                  left join artists a on s.artist_id = a.artist_id
                  where s.title = (%s)
                  and   a.name = (%s)
                  and   CAST(s.duration AS decimal) = (%s)""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]