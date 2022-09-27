
alphabet = 'BJRMOFPV'
spots = 4

combinations = []


def create_combinations(prefix, remaining_spots):
    for l in alphabet:
        if remaining_spots == 1:
            combinations.append(prefix + l)
        else:
            create_combinations(prefix + l, remaining_spots - 1)

create_combinations('', spots)


def compare(a, b):
    if len(a) != spots or len(b) != spots:
        raise BaseException("Wrong size")

    m = 0
    o = {}
    for l in a:
        if l in o:
            o[l] += 1
        else:
            o[l] = 1

    for l in b:
        if l not in o:
            o[l] = 0

        if o[l] > 0:
            m += 1

        o[l] -= 1

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
    test = ""

    try:
        test = input(f"I try {the_try}, what is the result: ")
        test = tuple(map(int, test.split(',')))
        if len(test) != 2 or int(test[0]) < 0 or int(test[0]) > spots or int(test[1]) < 0 or int(test[1]) > spots:
            assert False
    except:
        test = ask_input(the_try)

    return test


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





def interactive_play():
    global combinations

    print(f"Alphabet: {alphabet}")
    input("To make your life simpler you can input your code here I won't look :) --> ")
    print("============================================================")

    the_try = (alphabet[0] * int(spots / 2)) + (alphabet[1] * int(spots / 2))

    show_remaining_possibilities()
    test = ask_input(the_try)
    combinations = remove_combinations(the_try, test)
    show_remaining_possibilities()

    while len(combinations) > 1:
        the_try = combinations[0]
        the_score = len(alphabet) ** spots + 1
        _s = the_score

        for t in combinations:
            _s = score_try(t)
            if _s < the_score:
                the_score = _s
                the_try = t

        test = ask_input(the_try)
        combinations = remove_combinations(the_try, test)
        show_remaining_possibilities()

    if len(combinations) == 1:
        print("FOUND THE COMBINATION")
        print(combinations[0])
    else:
        print("YOU MESSED UP!")





interactive_play()










