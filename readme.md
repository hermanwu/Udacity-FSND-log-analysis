# Log-Analysis
This project sets up a mock PostgreSQL database for a fictional news website. 
The provided Python script uses the psycopg2 library to query the database 
and produce a report that answers the following three questions 
(view database structure in the table_structures.txt file): 


## Questions:
* What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
* Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
* On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

## Instructions:
* install <a href="https://www.vagrantup.com/">Vagrant</a> and 
<a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox.</a>
* start virtual machine by running 'vagrant up' to setup the machine, 
and 'vagrant ssh' to login (vagrant file included in the project)
* download <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">data</a>
* unzip newsdata.zip to extract newsdata.sql
* run 'psql -d news -f newsdata.sql' to load database
* run 'log.py'  (using python 2.7)
