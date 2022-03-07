0-hello_world file Tscript here prints 	Prints "Hello, World", followed by a new line to the standard output
1-confused_smiley echo "\"(Ôo)'" prints a confused simely
cat /etc/passwd commands displays the content of the /etc/passwd
cat /etc/passwd /etc/hosts/ Display the content of /etc/passwd and /etc/hosts
tail -n 10 /etc/passwd displays the last ten lines of the file specified
head -n 10 /etc/passwd displays the first 10 lines of the file speciffied
head -n 3 iacta | tail -n 1 displays the third line of the specified file
echo "Best School" > \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) this creates a file named (specified above)
ls -la > ls_cwd_content writes into the file ls_cwd_content the result of the command ls -la
tail -n 1 iacta >> iacta  duplicates the last line of the file iacta
find . -type f -name "*.js" -delete  deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
find . -type d -not -name '.' | wc -l counts the number of directories and sub-directories in the current directory.
ls -t1 | head -n 10 displays the 10 newest files in the current directory.
sort | uniq -u takes a list of words as input and prints only words that appear exactly once.
grep -i "root" /etc/passwd Display lines containing the pattern “root” from the file /etc/passwd
grep -c -i "bin" /etc/passwd Display the number of lines that contain the pattern “bin” in the file /etc/passwd
grep -i "root" -A 3 /etc/passwd Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
grep -i -v "bin" /etc/passwd Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
grep -i "^[a-z]" /etc/ssh/sshd_config Display all lines of the file /etc/ssh/sshd_config starting with a letter.
tr "A" "Z" | tr "c" "e" Replace all characters A and c from input to Z and e respectively
tr -d "cC" removes all letters c and C from input.
rev reverse its input.
cut -d ':' -f 1,6 /etc/passwd | sort displays all users and their home directories, sorted by users
find . -empty | rev | cut -d '/' -f 1 | rev finds all empty files and directories in the current directory and all sub-directories.
find -type f -name "*.gif" | rev | cut -d "/" -f 1 | cut -d '.' -f 2- | rev | LC_ALL=C sort -f lists all the files with a .gif extension in the current directory and all its sub-directories.
cut -c 1 | paste -s -d ''  a script that decodes acrostics that use the first letter of each line.
tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
