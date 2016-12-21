# coding: utf-8
import appex
import os
import shutil
import console


def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    # list contains two duplicate entries, get first one
    inputfile = appex.get_attachments()[0]
    comps = __file__.split(os.sep)
    # check if file exists
    if os.path.exists(inputfile):
        try:
            # Attempt to move source into destination
            shutil.copy2(inputfile,
                         os.path.join(os.sep.join(
                             comps[:comps.index('Documents')+1]),
                             os.path.basename(inputfile)))
            console.hud_alert(os.path.basename(inputfile) +
                              ' copied successful.')
        except Exception:
            console.hud_alert('Unable to copy ' + inputfile + '.')

if __name__ == '__main__':
    main()
