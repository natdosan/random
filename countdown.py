import time

def countdown(t):
    while t: # while t > 0
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs) # inserts mins and secs into visual timer format
        print(timer, end='\r') # overrite previous line
        time.sleep(1)
        t-=1 # incriment until 0 
    print('Get to see Angie <3')
t=input("Enter the time in seconds: ")

countdown(int(t))

# Next: Turn into a webapp