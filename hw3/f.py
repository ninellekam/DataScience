def brackets(n):
    open_bracket_counter = 0
    close_bracket_counter = 0
    my_list = []

    def generate(open_bracket_counter, close_bracket_counter, my_list, n):
        if (open_bracket_counter + close_bracket_counter < 2 * n):
            if (open_bracket_counter < n):
                my_list.append('(')
                yield from generate(open_bracket_counter + 1, close_bracket_counter, my_list, n)
                my_list.pop()
            if (open_bracket_counter - close_bracket_counter > 0):
                my_list.append(')')
                yield from generate(open_bracket_counter, close_bracket_counter + 1, my_list, n)
                my_list.pop()
        else:
            none_str = ''
            yield none_str.join(map(str, my_list))
    yield from generate(open_bracket_counter, close_bracket_counter, my_list, n)


if __name__ == "__main__":
    n = int(input())
    for i in brackets(n):
        print(i)
