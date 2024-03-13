import logging
logging.basicConfig(level= logging.INFO, format = '%(message)s')
def merge_the_tools():
    s = input().strip()
    k = int(input())
    ans = ''
    substrings = [s[i:i+k] for i in range(0, len(s), k)]
    for substring in substrings:
        unique_chars = []
        for char in substring:
            if char not in unique_chars:
                unique_chars.append(char)
                ans += char
        # logging.info(''.join(unique_chars))
        ans += '\n'
    return ans


