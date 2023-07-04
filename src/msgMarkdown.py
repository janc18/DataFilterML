import markdown

def TextToHtml(Text):
    """
    Return a string in html format from text in markdown format

    :param Text: string in markdown format
    :return: string in html format.

    """
    return markdown.markdown(Text,extensions=['tables'])

def MarkdownToHtml(Path):
    """
    Return a string in html format from markdown file

    :param Path: path from markdown file.
    :return: string in html format.

    """
 
    with open(Path,"r",encoding="utf-8") as InputFile:
        Text=InputFile.read()
        return markdown.markdown(Text,extensions=['tables'])
