import editor
import re


def main():
    """Trim trailing whitespaces in each line of the currently opened document
    in editor.
    """
    contents = editor.get_text()
    # split editor content by trailing whitespaces
    contents = re.split(' +\n', contents)
    # join again with newlines and remove last character, because otherwise
    # there would be an additional newline
    contents = '\n'.join(contents)[:-1]
    editor.replace_text(0, len(editor.get_text()), contents)

    return


if __name__ == '__main__':
    main()

