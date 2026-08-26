# Linux File, Directory, and User Management

## Overview

This lab documents Linux command-line skills practiced while completing the Google Cybersecurity Professional Certificate.

## Skills

The exercises focused on navigating the Linux file system, managing files and directories, modifying file permissions, and performing administrative tasks involving users and groups.

```bash

# Navigate to logs directory
cd /home/analyst/logs

# Use grep to search a file and return the lines with the word coffee
grep coffee server_logs.txt

# Pipe character to pass output of the ls command as input to the grep command
ls | grep muffin

# Create and remove a directory. Make sure you are in the correct place.
cd /home/analyst
ls /home/analyst
mkdir logs
rmdir temp

# Create a new file and open using the nano application
touch newEmployee.txt
nano newEmployee.txt

# The command that shows where you are.
pwd

# View permission of a file including those hidden. Change permissions of the user to delete write but add read.
ls -la
chmod u-w,u=r statement_m.txt

# Use sudo to execute administrative commands with elevated privileges.
sudo usermod -g lab_team scientist1
cd /home/scientist/projects
ls /home/scientist/projects
sudo chown scientist1 /home/scientist/projects/project_11.txt
sudo userdel scientist1

## Decrypt a Cipher Using a Translation Command

Use the `tr` command to translate characters and decrypt the contents of a file.

```bash
cat .hiddenFile3 | tr "d-za-cD-ZA-D" "a-zA-Z"
```

The `cat` command displays the contents of the hidden file, while `tr` translates the specified characters to reveal the decrypted text.

---

## Generate Hashes to Compare Two Files

View the contents of each file:

```bash
cat file1.txt
cat file2.txt
```

Generate a SHA-256 hash for each file:

```bash
sha256sum file1.txt
sha256sum file2.txt
```

The `sha256sum` command generates a SHA-256 hash based on the contents of each file.

- If the hashes are identical, the files contain the same data.
- If the hashes are different, the files contain different data.
```
