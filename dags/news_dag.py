from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from RSSParser.RSSParser import rss_parser_operation


default_args = {
    "depends_on_past": False,
    "email": ["thisisalinton@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "news_crawling",
    default_args=default_args,
    description="A dag for managing the crawling of the news websites",
    start_date=datetime.today() - timedelta(days=1),
    schedule="@hourly",
    catchup=False,
) as dag:
    crawler_task = BashOperator(
        task_id="crawl_news_websites",
        bash_command="cd /home/ali/Desktop/wresteling-with-data/dags/ScrapyWebCrawler/datamooncrawling/datamooncrawling && scrapy crawl news_spider"
    )
    
    rss_task = PythonOperator(
        task_id="second_useless_job",
        python_callable=rss_parser_operation
    )
    
crawler_task >> rss_task