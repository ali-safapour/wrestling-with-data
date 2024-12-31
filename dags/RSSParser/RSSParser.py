from bidi.algorithm import get_display
import arabic_reshaper
import feedparser
from RSSParser.DB.db import get_db
from RSSParser.DB.services.hash_service import hash_exists, add_hash
import hashlib

def fa_print(text):
    reshaped_text = arabic_reshaper.reshape(text)
    display_text = get_display(reshaped_text)
    print(display_text)



def rss_parser_operation():
    rss_urls = [
        "https://www.asriran.com/fa/rss/allnews",
        "https://www.irna.ir/rss"
    ]

    db = next(get_db())
    
    with open('output_rss.txt', 'w', encoding='utf-8') as output_file:
        for rss_url in rss_urls:
            feed = feedparser.parse(rss_url)
            # fa_print(f"عنوان فید: {feed.feed.title}")
            # fa_print(f"توضیحات: {feed.feed.description}")
            # fa_print(f"لینک: {feed.feed.link}\n")
            print('this is the url', rss_url)
            for entry in feed.entries:
                # check if the same entry has been fetched already
                sha256_hash = hashlib.sha256(f"{entry.title}{entry.published}".encode()).hexdigest()
                print(sha256_hash)
                if hash_exists(db, sha256_hash):
                    continue
                add_hash(db, sha256_hash)
                try:
                    data = entry.title
                    fa_print(f"عنوان: {entry.title}")
                except:
                    pass
                else:
                    output_file.write(f"عنوان: {entry.title}")
                    
                try:
                    fa_print(f"لینک: {entry.link}")
                except:
                    pass
                else:
                    output_file.write(f"لینک: {entry.link}")

                try:
                    fa_print(f"تاریخ: {entry.published}")
                except:
                    pass
                else:
                    output_file.write(f"تاریخ: {entry.published}")

                try:
                    fa_print(f"خلاصه: {entry.summary}\n")
                except:
                    pass
                else:
                    output_file.write(f"خلاصه: {entry.summary}\n")