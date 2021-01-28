# cat-command
Python implementation of Linux cat command.

## Platform
The app currently works only on Linux.

## Download
To download the project files, type `git clone https://github.com/aw0s/cat-command.git` in folder which you want the program to be placed in. You can also download ZIP file and then unpack it.  
If You want to use cat app instead of original cat, type `alias cat='python path/to/cat/cat.py'`. To remove alias, type `unalias cat`.

## Running the program
Type `cd cat-command` and then `python cat.py`. If names of folders and files have been printed, the app works appropriately. If something went wrong, report the bug in `Issues` on the project's Github. Make sure you've installed Python package.

## Usage
You can use cat by passing a file as an argument, f.e. `python cat.py file.txt`. It prints file content. You can also tell the program to display another amount of files. F.e. ```
Input: python cat.py file1.txt file2.txt file3.txt.
Output:
file1.txt content
file2.txt content
file3.txt content```

## Flags
