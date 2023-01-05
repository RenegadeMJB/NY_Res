from datetools import DateTools as DT
from datetime import datetime
import os
import sys

class Day:
    yellow = '\u001b[43m'
    green = '\u001b[42m'
    reset = '\u001b[0m'

    def __init__(self, numberResolutions):
        self._finished = []
        for i in range(0, numberResolutions):
            self._finished.append(False)
        self._color = Day.reset

    def run(self):
        pass

    def checkOff(self):
        for index, res in enumerate(self._finished):
            if res == False:
                self._finished[index] = True
                self.pickColor()
                break
    
    def pickColor(self):
        started = False
        done = False
        if True in self._finished:
            started = True

        if started == True and False not in self._finished:
            done = True

        if done:
            self._color = Day.green
            print(f'{self._color}', flush=True, end='')
        elif started:
            self._color = Day.yellow
            print(f'{self._color}',flush=True,end='')


    
            

def main():
    cmd = """osascript -e '
    tell application "Terminal"
        set bounds of front window to {700, 50, 1412, 510}
    end tell
    '
    """
    os.system(cmd)

    try:
        year = int(sys.argv[1])
        DT.printYear(year)
        input("Please press Enter....")
        DT.clearscrn()
    except ValueError:
        DT.printYear(2023)
    except IndexError:
        DT.printYear(2023)

if __name__ == "__main__":
    main()
    
