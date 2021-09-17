import pathlib
from markdownify import markdownify as md

matches = pathlib.Path("md").glob("**/*.html")


for match in matches:
    # print(match)
    content = match.read_text(encoding="utf-8")

    new = md(content)

    match.parent.open(f'{match.stem}.md')

    # print(new)

