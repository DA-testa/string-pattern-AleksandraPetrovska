# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    # after input type choice
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
        return(pattern, text)
    if input_type == 'F':
        with open ("tests/06", 'r') as f:
    # read two lines 
    # first line is pattern
            pattern =  f.readline().rstrip()
    # second line is text in which to look for pattern 
            text = f.readline().rstrip()
    # return both lines in one return
            return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    # this function should find the occurances using Rabin Karp alghoritm
    B = 13
    Q = 256
    pattern_hash = 0
    text_hash = 0

    p = len(pattern)
    t = len(text)

    for i in range(p):
        pattern_hash = (pattern_hash * B + ord(pattern[i])) % Q
    
    
    for i in range(p):
        text_hash = (text_hash * B + ord(text[i])) % Q

    for i in range(t - p + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + p]:
                occurrences.append(i)

        if i < t - p:
            text_hash = ((text_hash - ord(text[i]) * pow(B, p - 1, Q)) * B + ord(text[i + p])) % Q
    
    
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    occurrences = get_occurrences(*read_input())
    print_occurrences(occurrences)