# Log-Analysis
This short program will get data from a postgresql database and answer following three questsions 
(view database structure in the table_structures.py file): 


## Questions:
* What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
* Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
* On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

## Instructions:
* install Vagrant and Virtual Box
* start virtual machine by running 'vagrant up' to setup the machine, and 'vagrant ssh' to login
* download <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">data</a>
* run 'psql -d news -f newsdata.sql' to load database
* run 'log.py'
