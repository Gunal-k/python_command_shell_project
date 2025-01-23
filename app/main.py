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
        builtins = ["exit", "echo","type","pwd","cd"]
        PATH = os.getenv("PATH")

        if command.startswith("exit"):
            sys.exit(0)
        elif ">" in command:
            cmnd = command.split()[0]
            command= command.split()[1].replace("1>", ">")
            cmd = command.split(">")
            cmd_args = shlex.split(cmd[0])
            for path in cmd_args:
                if os.path.exists(path):
                   args = path
                else:
                    errors = f"{cmnd}: {path}: No such file directory\n"
            with open(cmd[1], "w") as f:
                with open(args, "r") as f2:
                    f.write(f2.read())
            if errors:
                sys.stdout.write(errors)
        elif command.startswith("invalid"):
            sys.stdout.write(f"{command}: command not found\n")
        elif command.startswith("echo"):
            value = command[5:].strip()
            value = " ".join(shlex.split(value))
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
        elif command.startswith("pwd"):
            sys.stdout.write(f"{os.getcwd()}\n")
        elif command.startswith("cd"):
            try:
                path = command[3:]
                if command[3:] == "~":
                    path = os.getenv("HOME")
                os.chdir(path)
            except FileNotFoundError:
                sys.stdout.write(f"cd: {command[3:]}: No such file or directory\n")
        elif command.startswith("cat"):
            cmd = command.split(maxsplit=1)[1]
            res = subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            sys.stdout.write(f"{res.stdout.decode()}")
        else:
            res = subprocess.run(command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            sys.stdout.write(f"{res.stdout.decode()}")
        sys.stdout.flush()
if __name__ == "__main__":
    main()
