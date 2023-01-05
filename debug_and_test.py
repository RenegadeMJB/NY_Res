from datetools import DateTools
import os
import sys

year = int(sys.argv[1])

cmd = """osascript -e '
    tell application "Terminal"
        set bounds of front window to {700, 50, 1412, 510}
    end tell
    '
    """
os.system(cmd)

DateTools.printYear(year, 1)