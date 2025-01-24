# Python Command Shell Project

This repository contains a custom command-line shell implemented in Python as part of the **Codecrafters course**. The shell mimics the behavior of popular Unix shells, with features such as:

- **Tab Completion**: Autocompletes commands and executables with intelligent handling of multiple matches.
- **Builtin Commands**: Implements common shell commands like `cd`, `pwd`, `echo`, and `type`.
- **Redirection**: Supports input/output redirection (`>`, `>>`, `2>`, `2>>`).
- **Process Execution**: Executes external programs using the system's `PATH`.

### Features
- Command parsing with `shlex` for safety and reliability.
- Custom tab completion logic that adapts to multiple or single matches.
- Handles file/directory navigation and error messages gracefully.

### How It Works
This shell reads user input, interprets commands, and executes them by leveraging Python's `subprocess` module. It also manages stateful features like tab completion using Python's `readline` library.

### Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/Gunal-k/python_command_shell_project.git
   cd python_command_shell_project
   ```
2. Run the shell:
   ```bash
   python shell.py
   ```

### Credits
- Developed while completing the **Build Your Own Shell** project on [Codecrafters.io](https://codecrafters.io/).
