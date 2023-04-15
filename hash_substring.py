# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern
    pattern =  input().rstrip()
    # second line is text in which to look for pattern 
    text = input().rstrip()
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    output.sort()
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurr = []
    # this function should find the occurances using Rabin Karp alghoritm
    a = 256
    m = 10**9+7
    
    result1 = 0
    for i in range(len(pattern)):
        result1 = (result1 * a + ord(pattern[i])) % m 
    
    result2 = 0
    for i in range(len(pattern)):
        result2 = (result2 * a + ord(text[i])) % m

    for i in range(len(text) - len(pattern) + 1):
        if result1 == result2:
            if pattern == text[i:i+len(pattern)]:
                occurr.append(i)
        if i < len(text) - len(pattern):
            result2 = ((result2 - ord(text[i]) * pow(a, len(pattern)-1, m)) * a + ord(text[i+len(pattern)])) % m

    # and return an iterable variable
    return occurr


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

