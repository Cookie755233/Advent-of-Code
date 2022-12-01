
import os
import typer
import datetime
from aocd.models import Puzzle
from aocd import submit
from typing import Optional

app = typer.Typer()
    
class Solver(Puzzle):
    def __init__(self, year, day, user=None):
        super().__init__(year, day, user)
        self._pull_data()

    
    @property
    def base_dir(self):
        return '/Users/cookie/Documents/Advent-of-Code'
    
    @property
    def _year(self):
        return str(self.year)
    
    @property
    def _day(self):
        return f'day-{(self.day)}'
    
    def _check_exists(self, path):
        return os.path.exists(path)
    
    
    def _pull_data(self, part='a'):
        path = os.path.join(self.base_dir, self._year, self._day)
        
        if not self._check_exists(path):
            os.makedirs(path)
            
        with open(os.path.join(path, f'{self._day}_input.txt'), 'w') as f:
            f.write(self.input_data)
            
        
@app.command(short_help='2022/12/2 -> 202202')
def pull(date_: Optional[str] = typer.Argument(None)):
    if not date_:
        return datetime.date.today().day, datetime.date.today().year
    else:
        return date_[-2:], date_[:4]
    
    
def main():
    day, year = app().pull()
    print(day, year)
    solver = Solver(day=day, year=year)
    
    # puzzle = Puzzle(year=2015, day=1)
    # print(puzzle.input_data)

if __name__ == '__main__':
    main()