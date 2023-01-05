from datetools import DateTools as DT
import os

class Day:
    def __init__(self, numberResolutions):
        self._finished = []
        for i in range(0, numberResolutions):
            self._finished.append(False)


def main():
    cmd = """osascript -e '
    tell application "Terminal"
        set bounds of front window to {700, 50, 1412, 510}
    end tell
    '
    """

    os.system(cmd)

if __name__ == "__main__":
    main()
    DT.printYear(2023)
