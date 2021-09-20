from pathlib import Path
import markdown
import re


def get_questions(dir):
    matches = Path(dir).glob("**/*.md")
    for match in matches:
        print(match)
        content = match.read_text(encoding="utf-8")
        lines = content.splitlines()

        for line in lines:
            # print(line)
            if re.match(r".+[༡-༩]༽", line) or re.match(r"😊", line):
                print(line)

        # print(f"{match.stem}- {questions}")

        # html_path = Path(f'{match.parent}/{match.stem}.html')

        # html_path.write_text(html_content, encoding="utf-8")

        # print(html_path)

dir = "tutorials/"
get_questions(dir)

