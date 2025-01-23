import sys
import os
import subprocess
import shlex

def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        builtins = ["exit", "echo","type"]
        PATH = os.getenv("PATH")

        if command.startswith("exit"):
            sys.exit(0)
        elif command.startswith("invalid"):
            sys.stdout.write(f"{command}: command not found\n")
        elif command.startswith("echo"):
            value = command[5:]
            sys.stdout.write(f"{value}\n")
        elif command.startswith("type"):
            value = command[5:]
            cmd_path = None
            paths = PATH.split(":")
            for path in paths:
                if os.path.exists(f"{path}/{value}"):
                    cmd_path = f"{path}/{value}"    
            if value in builtins:
                sys.stdout.write(f"{value} is a shell builtin\n")
            elif cmd_path:
                sys.stdout.write(f"{value} is {cmd_path}\n")
            else:
                sys.stdout.write(f"{value}: not found\n")
        else:
            res = subprocess.run(command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            sys.stdout.write(f"{res.stdout.decode()}")
if __name__ == "__main__":
    main()
