PROJECT:

This project is created to practice creating a datawarehouse with star schema.  There is one fact table in the schema called Sonplays and 4 dimenstions: users, time, songs, artists. This datawarehouse is created using AWS s3 and redshift database. Data is stored in log file and song file in s3 bucket.  

Description of process
First, script create_tables.py creates staging, dimension and fact tables. Then, script etl.py loads json data from S3 to Redshift staging table. Finally, it loads from staging table to dimension and fact table by using INSERT INTO ... SELECT ... syntax.

Staging tables
log_data provide event data recorded in json file under log_data directory

song_data provide song and artist data recorded in json file under song_data directory

Dimension tables
songs provide song data which were played

artists provide artist data whose songs were played

users provide user data who played songs

time provide time data when users played songs

Fact table
songplays provide event data which describe who, when and what songs are played
Those tables are designed using STAR schema, which can easily analyze various aspects. I assumed we can specify artists and songs of event data by its name and title.


Queries run:

I wrote queries such as select * from log_data limit 10;

Similar to above query was writted for song_data as well. 

