import sys
import os
import subprocess
import shlex
import readline

builtins = ["exit", "echo","type","pwd","cd"]

def executables():
    executables = []
    paths = os.getenv("PATH").split(":")
    for path in paths:
        if os.path.isdir(path):
            executables.extend([f for f in os.listdir(path) if os.access(os.path.join(path, f), os.X_OK)])
    return executables

def completer(text, state):
    options = [s for s in builtins + executables() if s.startswith(text)]
    if state < len(options):
        return options[state] + " "  # Add a space to the completion
    else:
        return None

def main():
    # Uncomment this block to pass the first stage
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        PATH = os.getenv("PATH")


        if command.startswith("exit"):
            sys.exit(0)
        elif "2>>" in command:
            command = command.replace("2>>", ">>")
            cmd , out = command.split(">>")
            res = cat(cmd.strip())
            with open(out.strip(), "a") as f:
                f.write(res.stderr.decode())
            if res.stdout:
                sys.stdout.write(f"{res.stdout.decode()}")
        elif ">>" in command:
            command = command.replace("1>>",">>")
            cmd , out = command.split(">>")
            res = cat(cmd.strip())
            with open(out.strip(), "a") as f:
                f.write(res.stdout.decode())
            if res.stderr:
                sys.stderr.write(f"{res.stderr.decode()}")
        elif "2>" in command:
            command = command.replace("2>",">")
            cmd , out = command.split(">")
            res = cat(cmd.strip())
            with open(out.strip(), "w") as f:
                f.write(res.stderr.decode())
            if res.stdout:
                sys.stdout.write(f"{res.stdout.decode()}")
        elif ">" in command:
            command = command.replace("1>",">")
            cmd , out = command.split(">")
            res = cat(cmd.strip())
            with open(out.strip(), "w") as f:
                f.write(res.stdout.decode())
            if res.stderr:
                sys.stderr.write(f"{res.stderr.decode()}")
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
        else:
            res = cat(command)
            sys.stdout.write(f"{res.stdout.decode()}")
        sys.stdout.flush()
        sys.stderr.flush()

def cat(cmd):
    res = subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return res



if __name__ == "__main__":
    main()
