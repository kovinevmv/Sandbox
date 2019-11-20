from text_processor import TextProcessor
from utils import is_exclude_path, is_exclude_file
import sys, os, re


def work_with_dir(path):
    for path, dirs, files in os.walk(path):
        stop = is_exclude_path(path)

        if not stop:
            for f in files:
                file_path = f"{path}/{f}".replace('//', '/')
                if not is_exclude_file(file_path):
                    t = TextProcessor(file_path, type_extraction='raw', type_='dir')
                    run_text_processor(t)


def work_with_web(url):
    t = TextProcessor(url, type_extraction='raw', type_='web')
    run_text_processor(t)


def run_text_processor(processor):
    if processor.file_type == 'dir':
        url = re.findall(r"\/([^\/]*\/?)$", sys.argv[2])[0]
        url = processor.url[processor.url.find(url):]
        link = f"{url}"

    if processor.file_type == 'web':
        link = f"[URL]({processor.url})"
    
    errors = processor.validate_words()
    for (word, correct) in errors:
        print(f'{link}: "{word}" заменить на "{correct}"')


def main():
    type_file = sys.argv[1]
    if type_file == 'dir':
        work_with_dir(sys.argv[2])
    if type_file == 'web':
        work_with_web(sys.argv[2])

if __name__ == "__main__":
    main()