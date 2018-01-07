import argparse
import base64
import openpyxl
import os
import json
import webbrowser
from urllib.parse import quote


def base64_to_file(s, filename):
    """Convert base64-encoded string to file.

    Parameters
    ----------
    s : str
        base64encoded string
    filename : str
        filename of file
    """
    file = open(filename, 'wb')
    file.write(base64.b64decode(s))
    file.close()


def excel_append_line(filename, linedata, sheet_idx=0):
    """Append list as newline to excel sheet.

    Parameters
    ----------
    filename : str
        filename of xlsx-file
    linedata : list
        list, which will be appended as new line in sheet
    sheet_idx : int
        index of sheet, where to append linedata
    """
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook[workbook.get_sheet_names()[0]]
    sheet.append(linedata)
    workbook.save(filename)


def main():
    # argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('filecontents',
                        help='Base64-encoded string of xlsx-file.')
    parser.add_argument('linecontent', nargs='+',
                        help='Content of line to be appended in xlsx-file.')
    parser.add_argument('-f', '--filepath', type=str,
                        help='Filename and path for Excel file.')
    parser.add_argument('-i', '--index', type=int, default=0,
                        help='Sheet index of Excel file.')
    args = parser.parse_args()

    # define filename for temporary file
    filename = 'tmp.xlsx'

    # convert base64-encoded file
    base64_to_file(args.filecontents, filename)

    # append data to file
    excel_append_line(filename, args.linecontent, sheet_idx=args.index)

    # encode newly generated file to base64 and remove temporary file
    file = open(filename, 'rb')
    workflow_input = {'filecontents': base64.b64encode(file.read())
                      .decode('ascii')}
    file.close()
    os.remove(filename)

    # add filepath to dict if available
    if args.filepath is not None:
        workflow_input['path'], \
            workflow_input['filename'] = os.path.split(args.filepath)

    # pass data back to Workflow
    webbrowser.open('workflow://run-workflow?name=SaveBase64ToDropbox&input=' +
                    quote(json.dumps(workflow_input), ''))


if __name__ == '__main__':
    main()
