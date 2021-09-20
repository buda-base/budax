import pathlib
import markdown


def filter(content):
    questions = []
    lines = content.readlines
        
    
    return questions


def get_questions(dir):
    matches = pathlib.Path(dir).glob("**/*.md")
    for match in matches:
        # print(match)
        content = match.read_text(encoding="utf-8")

        questions = filter(content)

        html_path = pathlib.Path(f'{match.parent}/{match.stem}.html')

        html_path.write_text(html_content, encoding="utf-8")

        print(html_path)

dir = "tutorials/pdf24"
get_questions(dir)

