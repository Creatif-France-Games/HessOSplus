# HessOS

![](https://raw.githubusercontent.com/bowser-2077/HessOS/refs/heads/main/github/V2.png)

HessOS is a lightweight, custom command-line operating system simulator written in Python.  
Designed for learning, tinkering, and fun, HessOS offers a simple shell with essential commands, boot animation, dependency management, and more.

---

## Features

- **Custom Shell Interface** with command prompt and dynamic command handling
- **Boot Sequence** with centered logo and loading animation  
- **First Boot Dependency Installation** with automatic package setup  
- **Command Modules** for easy extensibility (commands live in `cmds/` folder)  
- Common Unix-like commands:  
  - `ls`, `cd`, `mkdir`, `rmdir`, `rm`, `touch`, `cat`, `head`  
  - `clear`, `help`, `ping`, `ssh`, `download`  
- **Logging and Configuration Management** through `logs/` and `config/` folders  
- Shutdown command with fake service loading animation  
- Modular codebase structured with `cmds/`, `startup/`, `utils/`, `config/`, and `logs/`

---

## Getting Started

### Requirements

- Python 3.8 or higher  
- Internet connection for first-time dependency installation

### Installation

Clone the repository:

```bash
git clone https://github.com/bowser-2077/HessOS.git
cd hessos
```

# Run the OS:
```
python main.py
```

On the first run, you will need to install required dependencies by using the ````py install-deps.py``` command into HessOS.
## Usage
### Basic Commands

    help — Show available commands

    ls — List files in current directory

    cd <folder> — Change directory

    mkdir <folder> — Create a new directory

    rmdir <folder> — Remove a directory

    rm <file> — Delete a file

    touch <file> — Create a new empty file

    cat <file> — Display file content

    head <file> — Show first 10 lines of a file

    clear — Clear the screen

    ping <host> — Ping a host to check network connectivity

    ssh <user>@<host> — Connect to a remote host via SSH

    download <url> — Download a file from a URL into downloads/ folder

    showlogs — Display recent logs

    shutdown — Shutdown the OS with animated loading of services

    package — Install package (only git for now)

    update — Update the os (Very Unstable for now!)

## Exiting

    Use forceexit command to quit hessos OR use the *shutdown* command.

## Project Structure

hessos/

├── cmds/          # Command implementations  
├── config/        # Configuration files and flags  
├── logs/          # Log files  
├── startup/       # Boot scripts and animations  
├── utils/         # Utility modules (logger, helpers)  
├── main.py        # Entry point

## SSH Client

HessOS come with an integrated ssh client
## Updates system
The update command will not work with HessOS V1, please install the V2 of HessOS to be able to use the update command
# Contributing

Feel free to open issues or pull requests! Add commands, improve UX, or optimize code.
License

MIT License © 2025 Gaetan LERLEY
## Contact

Hostinfire — hostinfire@gmail.com
GitHub: https://github.com/bowser-2077

# Happy HessIng! 🚀

