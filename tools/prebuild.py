#!/bin/python3

"""Convert tables in MD files to HTML prior to processing by Sphinx."""

from markdown import markdown, markdownFromFile


def mkdown(mdtext):
    """
    Convert MD to HTML.

    Uses the markdown module and tables extension.
    """
    html = markdown(mdtext, extensions=['markdown.extensions.tables'])
    return html


def directmkdown(mdfile):
    """
    Convert MD to HTML from a file.

    Uses the markdownFromFile module and tables extension.
    """
    html = markdownFromFile(mdfile, extensions=['markdown.extensions.tables'])
    return html


def source(file):
    """Open a file containing example MD text."""
    with open(file, 'r') as f:
        result = f.read()
    return result


def output(file, html):
    """Write html to file."""
    with open(file, 'w') as f:
        f.write(html)
    return True


if __name__ == '__main__':
    green = '\033[92m'
    end = '\033[0m'
    mdfile = "example.md"
    mdtext = source(mdfile)
    print("\n" + green + "Standard Markdown with table support:" + end)
    print(mkdown(mdtext) + "\n")
    print(directmkdown(mdfile))
