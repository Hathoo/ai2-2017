def print_two(a, b):
    """
    print_two(4, 1, b=1)  # invalid
    print_two(1, a=1)     # invalid
    print_two(b=1, a=4)   # valid
    print_two(a=4, b=1)   # valid
    print_two(b=4, 1)     # invalid
    print_two(4, 1, 1)    # invalid
    print_two(4, a=1)     # invalid 
    print_two(a=4, 1)     # invalid 
    print_two(41)         # invalid 
    print_two(4, 1)       # valid
    print_two()           # invalid 
    """
    print("Arguments: {0} and {1}".format(a, b))


def keyword_args(a, b=1, c='X', d=None):
    """
    bar(5)               # valid
    bar(a=5)             # valid
    bar(5, 8)            # valid
    bar(5, 2, c=4)       # valid
    bar(5, 0, 1)         # valid
    bar(5, 2, d=8, c=4)  # valid
    bar(5, 2, 0, 1, "")  # invalid 
    bar(c=7, 1)          # invalid 
    bar(c=7, a=1)        # valid
    bar(5, 2, [], 5)     # valid
    bar(1, 7, e=6)       # invalid 
    bar(1, c=7)          # valid
    bar(5, 2, b=4)       # invalid 
    """
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


def variadic(*args, **kwargs):
    """
    baz(2, 3, 5, 7) # valid
        Positional: (2, 3, 5, 7)
        Keyword: {}
    baz(1, 1, n=1)  # valid
        Positional: (1, 1)
        Keyword: {'n': 1}
    baz(n=1, 2, 3)  # invalid
    baz() # valid
    baz(cs="Computer Science", pd="Product Design") # valid
    baz(cs="Computer Science", cs="CompSci", cs="CS") # invalid 
    baz(5, 8, k=1, swap=2) # valid
    baz(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'}) # invalid
    baz(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'}) # valid
    baz(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'}) # invalid 
    baz({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'}) # valid
        Positional: ({'b': 'x', 'a': 5}, 'b', 'a')
        Keyword: {'b': 'x', 'a': 5}
    """
    print("Positional:", args)
    print("Keyword:", kwargs)


def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    """Skipping the optional part"""
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)


def speak_excitedly(message, num_exclamations=1, enthusiasm=False):
    message += '!' * num_exclamations
    if not enthusiasm:
        return message
    return message.upper()

def test_speak_excitedly():
    """ Sample function calls illustrating the `speak_excitedly` function. """
    print(speak_excitedly("I love Python"))

    print(speak_excitedly("Keyword arguments are great", num_exclamations=4))

    print(speak_excitedly("I guess Java is okay...", num_exclamations=0))

    print(speak_excitedly("Let's go Stanford", num_exclamations=2, enthusiasm=True))

def average(*nums):
    if not nums: return None
    return sum(nums) / len(nums)

def test_average():
    nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    avg = average(*nums)
    print("Average of first 10 primes is {}".format(avg))

def make_table(key_justify='left', value_justify='right', **kwargs):
    
    justification = {
        'left': '<',
        'right': '>',
        'center': '^'
    }
    if key_justify not in justification or value_justify not in justification:
        print("Error! Invalid justification specifier.")
        return None

    key_alignment_specifier = justification[key_justify]
    value_alignment_specifier = justification[value_justify]

    max_key_length = max(map(len, kwargs.keys()))
    max_value_length = max(map(len, kwargs.values()))

    total_length = 2 + max_key_length + 3 + max_value_length + 2
    print('=' * total_length)
    for key, value in kwargs.items():
        print('| {:{key_align}{key_pad}} | {:{value_align}{value_pad}} |'.format(key, value,
            key_align=key_alignment_specifier, key_pad=max_key_length,
            value_align=value_alignment_specifier, value_pad=max_value_length
        ))
    print('=' * total_length)

def test_make_table():
    make_table(
        first_name="Sam",
        last_name="Redmond",
        shirt_color="pink"
    )

    make_table(
        key_justify="right",
        value_justify="center",
        song="Style",
        artist_fullname="Taylor $wift",
        album="1989"
    )

def nuance_return():
    def say_hello():
        print("Hello!")

    print(say_hello())  # None

    def echo(arg=None):
        print("arg:", arg)
        return arg

    print(echo())        # None
    print(echo(5))       # 5
    print(echo("Hello")) # Hello

    def drive(has_car):
        if not has_car:
            return
        return 100  # mil

    drive(False)  # None
    drive(True)   # 100
    
def parametersAndObject():
    def reassign(arr):
        arr = [4, 1]
        print("Inside reassign: arr = {}".format(arr))

    def append_one(arr):
        arr.append(1) 
        print("Inside append_one: arr = {}".format(arr))

    l = [4]
    print("Before reassign: arr={}".format(l))  # => [4]
    reassign(l)
    print("After reassign: arr={}".format(l))  # => [4]

    l = [4]
    print("Before append_one: arr={}".format(l))  # => [4]
    append_one(l)
    print("After append_one: arr={}".format(l))  # => [4,1]
    
def scope():
    # Case 1
    x = 10

    def foo():
        print("(inside foo) x:", x) # x=10
        y = 5
        print('value:', x * y)      # value=50

    print("(outside foo) x:", x)    # x=10
    foo()
    print("(after foo) x:", x)      # x=10
    
    # Case 2
    x = 10

    def foo():
        x = 8  # Only added this line - everything else is the same
        print("(inside foo) x:", x) # x=8
        y = 5
        print('value:', x * y)      # value=40

    print("(outside foo) x:", x)    # x=10
    foo()
    print("(after foo) x:", x)      # x=10

def unboundLocalError():
    x = 10

    def foo():
        print("(inside foo) x:", x)  # We swapped this line
        x = 8                        # with this one
        y = 5
        print('value:', x * y)

    print("(outside foo) x:", x)
    foo()
    print("(after foo) x:", x)
    # funkcja próbuje użyć zmiennej która nie istnieje
    
    lst = [1,2,3]
    def foo():
        lst = lst + [4] #w tym miejscu próbujemy stworzyć wewnątrz funkcji zmienną lst wykorzystując ją samą
    foo()

def mutableArgs():
    def append_twice(a, lst=[]):
        lst.append(a)
        lst.append(a)
        return lst
    
    # Works well when the keyword is provided
    append_twice(1, lst=[4])  # => [4, 1, 1]
    append_twice(11, lst=[2, 3, 5, 7])  # => [2, 3, 5, 7, 11, 11]

    # But what happens here?
    print(append_twice(1))
    print(append_twice(2))
    print(append_twice(3))
    # Kolejne wywołania funkcji przekazują sobie wartości listy lst
    
    
    
if __name__ == '__main__':
    test_speak_excitedly()
    test_average()
    test_make_table()
