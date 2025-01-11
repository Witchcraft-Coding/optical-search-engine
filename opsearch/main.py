from sys import argv, exit

def main(args: list[str]) -> int:
    print(args)
    return 0

def app():
    gives = main(argv[1:])
    exit(gives)
    
if __name__ == '__main__':
    app()