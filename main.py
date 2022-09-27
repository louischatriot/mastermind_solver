import time

alphabet = 'BJRMOFPV'
spots = 4

combinations = []
combinations_repartition = {}


def letters_from_combination(c):
    o = {}
    for l in alphabet:
        o[l] = 0

    for l in c:
        o[l] += 1

    letters = []
    for l in alphabet:
        letters.append(o[l])

    return letters



def create_combinations(prefix, remaining_spots):
    for l in alphabet:
        if remaining_spots == 1:
            c = prefix + l
            combinations.append(c)
            combinations_repartition[c] = letters_from_combination(c)
        else:
            create_combinations(prefix + l, remaining_spots - 1)



start_time = time.time()

create_combinations('', spots)

print(f"Timed creating combinations: {time.time() - start_time}")



def compare(a, b):
    if len(a) != spots or len(b) != spots:
        raise BaseException("Wrong size")

    # Counting letters on the spot
    # m = 0
    # o = {}
    # for l in a:
        # if l in o:
            # o[l] += 1
        # else:
            # o[l] = 1

    # for l in b:
        # if l not in o:
            # o[l] = 0

        # if o[l] > 0:
            # m += 1

        # o[l] -= 1

    # Letters having been counted before is slower
    al = combinations_repartition[a]
    bl = combinations_repartition[b]
    m = 0
    # for i in range(0, len(al)):
        # m += min(al[i], bl[i])

    for i, j in zip(al, bl):
        m += min(i, j)
    # m = sum([min(al[i], bl[i]) for i in range(0, len(al))])

    # Sorting then counting
    # m = 0
    # a = sorted(a)
    # b = sorted(b)
    # i = 0
    # while l < len(a):
        # xxx



    e = 0
    for i in range(0, spots):
        if a[i] == b[i]:
            e += 1

    return e, m - e


if spots % 2 != 0:
    raise BaseException("spots needs to be divisible by 2")

if len(alphabet) <= 1:
    raise BaseException("alphabet needs to be at least 2 long")

_s = sorted(alphabet)
for i in range (1, len(_s)):
    if _s[i - 1] == _s[i]:
        raise BaseException("alphabet must contain only different letters")


def remove_combinations(the_try, pair):
    _c = []

    for s in combinations:
        if compare(the_try, s) == pair:
            _c.append(s)

    return _c


def score_try(the_try):
    score = len(combinations)
    for e in range(0, spots):
        for m in range(0, spots - e + 1):
            score = min(score, len(remove_combinations(the_try, (e, m))))


    return score


def show_remaining_possibilities():
    print(f"Still {len(combinations)} possibilities. ", end = "")


def ask_input(the_try):
    pair = ""

    try:
        pair = input(f"I try {the_try}, what is the result: ")
        pair = tuple(map(int, pair.split(',')))
        if len(pair) != 2 or int(pair[0]) < 0 or int(pair[0]) > spots or int(pair[1]) < 0 or int(pair[1]) > spots:
            assert False
    except:
        pair = ask_input(the_try)

    return pair


def autoplay():
    global combinations

    print(f"Alphabet: {alphabet}")
    solution = input("What do you want me to find --> ")

    if len(solution) != spots:
        raise BaseException("Wrong solution size")
    else:
        for l in solution:
            if l not in alphabet:
                raise BaseException("Use only the alphabet")

    print("============================================================")

    the_try = (alphabet[0] * int(spots / 2)) + (alphabet[1] * int(spots / 2))
    pair = compare(the_try, solution)
    print(f"Still {len(combinations)} possibilities, trying {the_try}, resulting in answer {pair}")
    combinations = remove_combinations(the_try, pair)

    while len(combinations) > 1:
        the_try = combinations[0]
        the_score = len(alphabet) ** spots + 1
        _s = the_score

        for t in combinations:
            _s = score_try(t)
            if _s < the_score:
                the_score = _s
                the_try = t

        pair = compare(the_try, solution)
        print(f"Still {len(combinations)} possibilities, trying {the_try}, resulting in answer {pair}")
        combinations = remove_combinations(the_try, pair)

    print("DONE")
    print(combinations)




start_time = time.time()

def interactive_play():
    global combinations
    global start_time

    print(f"Alphabet: {alphabet}")
    input("To make your life simpler you can input your code here I won't look :) --> ")
    print("============================================================")

    the_try = (alphabet[0] * int(spots / 2)) + (alphabet[1] * int(spots / 2))

    show_remaining_possibilities()
    pair = ask_input(the_try)


    start_time = time.time()

    combinations = remove_combinations(the_try, pair)

    print(f"Timed remove combinations: {time.time() - start_time}")

    show_remaining_possibilities()


    while len(combinations) > 1:
        start_time = time.time()

        the_try = combinations[0]
        the_score = len(alphabet) ** spots + 1
        _s = the_score

        for t in combinations:
            _s = score_try(t)
            if _s < the_score:
                the_score = _s
                the_try = t

        print(f"Timed finding best minimax try: {time.time() - start_time}")

        pair = ask_input(the_try)
        combinations = remove_combinations(the_try, pair)
        show_remaining_possibilities()

    if len(combinations) == 1:
        print("FOUND THE COMBINATION")
        print(combinations[0])
    else:
        print("YOU MESSED UP!")





interactive_play()


print("LAUNCH")

remove_combinations("BBJJ", (2,0))









