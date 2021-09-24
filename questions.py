from pathlib import Path
import re
import csv


def write_csv(path, data):
    with open(path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def get_questions(dir):
    matches = Path(dir).glob("**/*.md")

    data = []

    for match in matches:
        print(match)
        content = match.read_text(encoding="utf-8")
        lines = content.splitlines()

        for line in lines:
            # print(line)
            if re.match(r".*[༡-༩]༽", line) or re.match(r".*○", line):
                data.append([match.parent,line])
        

    questions_path = Path(f'data.csv')

    write_csv(questions_path, data)


        # print(html_path)

dir = "howtoguides/"
get_questions(dir)

