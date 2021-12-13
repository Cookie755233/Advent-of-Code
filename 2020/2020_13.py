f = open('./2020_13.in').read().splitlines()

'''
Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest timestamp you could depart on a bus. The second line lists the bus IDs that are in service according to the shuttle company; entries that show x must be out of service, so you decide to ignore them.

The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on. The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when the bus departs, you can ride that bus to the airport!

To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport. (There will be exactly one such bus.)
What is the ID of the earliest bus you can take to the airport 

What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?
'''

t = int(f[0])

earliest = 100000
ID = None

for i, bus in enumerate(f[1].split(',')):
    # Part I
    if bus.isdigit():
        bus = int(bus)
        nxt = bus * (t//bus + 1)
        wait = nxt-t
        print(nxt, wait)
        
        if wait < earliest:
            earliest = wait
            ID = i
    
    # Part II
        nxt = bus * ((t-i)//bus + 1)
        wait =  nxt - t
        
    # print(ID, earliest)
print(earliest * ID)