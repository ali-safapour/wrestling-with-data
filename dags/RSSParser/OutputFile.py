from typing import Generator, TextIO

def get_file() -> Generator[TextIO, None, None]:
    try:
        file = open('output_rss.txt', 'w', encoding='utf-8')
        yield file
    finally:
        file.close()