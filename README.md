# Engineeringprojects - Data Modeling

## Summary of a pproject. 
<p> In this project I am creating dimensional and fact tables.  This data available in JSON format and contains metadata about a song and artist of that song. </p>
Dataset is divided in _two_ formats. 
1. Song dataset 
2. Log dataset.

Dataframes from the files were created using pandas dataframe. Following facts and dimension tables were created:


### Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong
Column Names: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables, col is an abbreviation of column name
1. users - users in the app
   col:user_id, first_name, last_name, gender, level
2. songs - songs in music database
   col:  song_id, title, artist_id, year, duration
3. artists - artists in music database
   col: artist_id, name, location, latitude, longitude
4. time - timestamps of records in songplays broken down into specific units
   col: start_time, hour, day, week, month, year, weekday
   

## Steps followed to create ETL process.
#### Created tables
1. Wrote CREATE statements in sql_queries.py to create each table.
2. Wrote DROP statements in sql_queries.py to drop each table if it exists.
3. Ran create_tables.py to create your database and tables.
4. Ran test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to   close the connection to the database after running this notebook.

#### Built ETL process
 Developed ETL Process in etl.ipynb notebook to develop ETL processes for each table. 
 Ran test.ipynb notebook to confirm records. 
 reran create_table.py to reset tables. 
 
 ### Built ETL pipeline
 
 Completed etl.ipynb to complete etl.py file to process datasets.  
 Ran create_table.py before running etl.py to rest tables. 
 Rn test.ipynb file to confirm records.

