import markdown

def TextToHtml(Text):
    return markdown.markdown(Text,extensions=['tables'])

def MarkdownToHtml(Path):
    with open(Path,"r",encoding="utf-8") as InputFile:
        Text=InputFile.read()
        return markdown.markdown(Text,extensions=['tables'])
