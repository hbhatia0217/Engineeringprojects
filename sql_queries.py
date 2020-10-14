# DROP TABLES

songplay_table_drop = "drop table songplay"
user_table_drop = "drop table users"
song_table_drop = " drop table songs"
artist_table_drop = "drop table artists"
time_table_drop = "drop table time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE if not exists songplay(
    songplay_id serial primary key not null, 
    start_time timestamp not null,
    user_id int not null, 
    level varchar, 
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location varchar , 
    user_agent varchar)
""")

user_table_create = ("""
CREATE TABLE if not exists users(
    user_id int primary key,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar)
""")

song_table_create = ("""
CREATE TABLE if not exists songs(
    song_id varchar primary key, 
    title varchar not null,
    artist_id varchar not null, 
    year int, 
    duration numeric)
""")

artist_table_create = ("""
CREATE TABLE if not exists artists(
    artist_id varchar primary key, 
    name varchar not null,
    location varchar,
    latitude varchar, 
    longitude varchar)
""")

time_table_create = ("""
CREATE TABLE if not exists time(
    start_time timestamp primary key, 
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay(
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent) 
    values(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
INSERT INTO users(
    user_id,
    first_name,
    last_name,
    gender,
    level)
    values(%s,%s,%s,%s,%s)
    ON CONFLICT(USER_ID) DO UPDATE
    SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs(
    song_id PRIMARY KEY NOT NULL,
    title,
    artist_id,
    year,
    duration)
    values(%s,%s,%s,%s,%s)
    ON CONFLICT(song_id)DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists DEFAULT VALUES
""")


time_table_insert = ("""
INSERT INTO time(
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday)
    values(%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT(START_TIME) DO NOTHING
""")

# FIND SONGS
/*Formatting it to PEP8 format*/
song_select = ("""
Select s.song_id song_id,a.artist_id artist_id
from songs s inner join artists a 
on s.artist_id = a.artist_id 
where s.title=%s and a.name = %s and s.duration =%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
