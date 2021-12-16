
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
ans1 = None

for i, bus in enumerate(f[1].split(',')):
    if bus.isdigit():
        bus = int(bus)
        this = bus * (t//bus)
        nxt = bus * (t//bus + 1)
        wait = nxt-t
        
        if wait < earliest:
            earliest = wait
            ans1 = bus * earliest
            
print(ans1)

'''
An x in the schedule means there are no constraints on what bus IDs must depart at that time.
What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?
'''

buses = f[1].split(',')

def mod_inverse(a,n):
    # find some x such that (a*x) % n == 1
    a = a % n
    if n == 1:
        return 1    
    for x in range(1, n):
        if (a*x) % n == 1:
            return x
    
# n busses
# bus k at index i departs at a time t+i
# t+i % k == 0
# t % k == -i
# t % k = k-i
# index = (k - (i%k)) % k
def get_earliest_time():
    ids = []
    fullProduct = 1
    for i in range(len(buses)):
        item = buses[i]
        if item != 'x':
            k = int(item)
            i = i % k
            ids.append(((k-i)%k,k))
            fullProduct *= k

    total = 0
    for i,k in ids:
        partialProduct = fullProduct // k

        inverse = mod_inverse(partialProduct,k)
        assert (inverse * partialProduct) % k == 1

        term = inverse * partialProduct * i
        total += term

    return total % fullProduct


print(get_earliest_time())
