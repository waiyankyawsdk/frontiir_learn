from decorators import slow_down

@slow_down
def countdown(start):
    if start < 1:
        print("Liftoff!")
    else:
        print(start)
        countdown(start - 1)
        #recursive function (calling itself)
countdown(5)