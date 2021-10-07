import pathlib
import markdown
from markdownify import markdownify as to_md
import re

def html2md(dir):
    matches = pathlib.Path(dir).glob("**/*.html")
    for match in matches:
        # print(match)
        content = match.read_text(encoding="utf-8")

        md_content = to_md(content)

        md_path = pathlib.Path(f'{match.parent}/{match.stem}.md')

        md_path.write_text(md_content, encoding="utf-8")

        print(md_path)

def md2html(dir):
    matches = pathlib.Path(dir).glob("**/*.md")
    for match in matches:
        # print(match)
        raw_content = match.read_text(encoding="utf-8")

        # apply image resizing

        content = re.sub(r'!\[(\d+)\]\((.+)\)', '<img src="\g<2>" width="\g<1>">', raw_content)


        html_content = markdown.markdown(content)

        html_path = pathlib.Path(f'{match.parent}/{match.stem}.html')

        html_path.write_text(html_content, encoding="utf-8")

        print(html_path)


md2html("menu")
md2html("howtoguides")

