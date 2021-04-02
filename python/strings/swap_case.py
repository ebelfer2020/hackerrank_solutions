def swap_case(s):
    # Swaps upper/lower-case letters to lower/upper-case letters
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
