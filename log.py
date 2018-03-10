import psycopg2

DBNAME = "news"
top_three_article = """
    SELECT articles.title, count(*) as access
    FROM articles LEFT JOIN log
    ON log.path = concat('/article/', articles.slug)
    WHERE log.status LIKE '%200%'
    GROUP BY articles.title
    ORDER BY access DESC
    LIMIT 3;
"""

most_popular_authors = """
    SELECT authors.name, SUM(viewCountPerArticle.count) as accessCount
    FROM authors
    LEFT JOIN
        (SELECT articles.author, count(*)
            from articles LEFT JOIN log
            ON log.path = concat('/article/', articles.slug)
            WHERE log.status LIKE '%200%'
            group by articles.id) as viewCountPerArticle
    on authors.id = viewCountPerArticle.author
    GROUP BY authors.name
    order by accessCount desc;
"""

error_rate_over_one_percent = """
    SELECT * FROM
        (
            SELECT errorCount.date,
               round((errorCount.count::decimal / allCount.count) * 100, 2)
               as errorRate
            FROM
                (SELECT count(*), DATE(log.time) FROM log
                WHERE log.status LIKE '%404%'
                GROUP BY DATE(log.time)) as errorCount

            INNER JOIN

                (SELECT count(*), DATE(log.time) FROM log
                GROUP BY DATE(log.time)) as allCount

            ON errorCount.date = allCount.date
        ) as errorRateTable
    WHERE errorRate > 1;
"""

queries_to_run = []


def get_query_results(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


def print_query_result(results):
    for row in results:
        print row[0], "--", row[1]

db = psycopg2.connect(database=DBNAME)
c = db.cursor()

result1 = get_query_results(c, top_three_article)
print "Most popular three articles of all time (article name - views count)"
print_query_result(result1)
print "\n"

result2 = get_query_results(c, most_popular_authors)
print "Most popular article authors of all time (author name - views count)"
print_query_result(result2)
print "\n"


result3 = get_query_results(c, error_rate_over_one_percent)
print "Days with more than 1% of requests lead to errors (date - error rate %)"
print_query_result(result3)
print "\n"


db.close()
