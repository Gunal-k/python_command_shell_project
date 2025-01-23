import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        builtins = ["exit", "echo"]

        if command.startswith("exit"):
            sys.exit(0)
        elif command.startswith("invalid"):
            sys.stdout.write(f"{command}: command not found\n")
        elif command.startswith("echo"):
            value = command[5:]
            sys.stdout.write(f"{value}\n")
        elif command.startswith("type"):
            value = command[5:]
            if value in builtins:
                sys.stdout.write(f"{value} is a shell builtin\n")
            else:
                sys.stdout.write(f"{value}: command not found\n")

if __name__ == "__main__":
    main()
