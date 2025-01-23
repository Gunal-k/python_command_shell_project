import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()

        if command.startswith("exit"):
            sys.exit(0)
        elif command.startswith("invalid"):
            sys.stdout.write(f"{command}: command not found\n")
        elif command.startswith("echo"):
            value = command[5:]
            sys.stdout.write(f"{value}\n")

if __name__ == "__main__":
    main()
