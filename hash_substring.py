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
        file_name = input()
        with open(file_name, 'r') as f:
    # read two lines 
    # first line is pattern
            pattern =  f.readline().rstrip()
    # second line is text in which to look for pattern 
            text = f.readline().rstrip()
    # return both lines in one return
    # this is the sample return, notice the rstrip function
            return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    output.sort()
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    # this function should find the occurances using Rabin Karp alghoritm
    B = 13
    Q = 256
    pattern_hash = 0
    text_hash = 0

    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * B + ord(text[i])) % Q
    
    
    for i in range(len(pattern)):
        text_hash = (text_hash * B + ord(text[i])) % Q

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + len(pattern)]:
                occurrences.append(i)

        if i < len(text) - len(pattern):
            text_hash = ((text_hash - ord(text[i]) * pow(B, len(pattern) - 1, Q)) * B + ord(text[i + len(pattern)])) % Q
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))