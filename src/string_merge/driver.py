from utils import merge_the_tools
def main():
    string = input("Enter the string: ").strip()
    k = int(input("Enter the length of each substring: "))
    merge_the_tools(string, k)

if __name__ == "__main__":
    main()
