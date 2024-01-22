
import os
from argparse import ArgumentParser

PATH = '/Users/cookie/Documents/Advent-of-Code'


def parse_arguments():
    parser = ArgumentParser()
    #? <--- input --->
    parser.add_argument('day',
                        type=str,
                        help='please enter the day of the month')
    parser.add_argument('-y', '--year',
                        type=str,
                        default='2023',
                        help='please enter the year of the quiz, default 2023')

    return parser.parse_args()



def make_dir(year: str, day: str) -> str:
    if not os.path.exists(
        day_path := os.path.join(
            PATH, year, day
            )
        ):
        
        os.mkdir(day_path)
    return day_path

def make_template(year: str, day: str) -> None:
    with open(os.path.join(PATH, year, day,
                           f"{day}.in"), 'w') as f:
        pass
    
    with open(os.path.join(PATH, year, day,
                           f"{day}.test"), 'w') as f:
        pass
    
    with open(os.path.join(PATH, year, day,
                           f"{day}.py"), 'w') as f:
        f.writelines([
            "\n",
            "import os\n",
            "import re\n",
            "\n\n",
            """with open(os.path.join(os.path.dirname(__file__), f"{os.path.splitext(__file__)[0]}.in")) as f:\n""",
            "    q = f.readlines()\n",
            "\n",
            "#* Question 1\n",
            "a1 = 0\n\n\n"
            'print(f"Answer 1: {a1}")\n\n\n\n',
            "#* Question 2\n",
            "a2 = 0\n\n\n"
            'print(f"Answer 2: {a2}")',
        ])
        


if __name__ == "__main__":
    args = parse_arguments()
    
    year = args.year
    day = f"day{args.day.zfill(2)}"

    path = make_dir(year, day)
    make_template(year, day)
    
    