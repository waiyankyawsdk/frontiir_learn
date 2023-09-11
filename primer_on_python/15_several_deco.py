from decorators import debug, do_twice

#@debug calls @do_twice, which calls greet(), or debug(do_twice(greet()))
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Era")

# @do_twice will be applied to @debug 
# @do_twice
# @debug
# def greet(name):
#     print(f"Hello {name}")

# greet("Eva")