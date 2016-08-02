def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_column():
    print '+----+----+'

def print_row():
    print '|    |    |'

def print_rows():
    do_four(print_row)

def block_one():
    print_column()
    print_rows()

def print_block():
    do_twice(block_one)
    print_column()

print_block()

