Linux File, Directory, and User Management
Overview

This lab documents Linux command-line skills practiced while completing the Google Cybersecurity Professional Certificate.

Skills

The exercises focused on navigating the Linux file system, managing files and directories, modifying file permissions, performing administrative tasks involving users and groups, decrypting a cipher, and comparing file integrity using SHA-256 hashes.

# Navigate to the logs directory
cd /home/analyst/logs

# Use grep to search a file and return lines containing the word "coffee"
grep coffee server_logs.txt

# Use a pipe to pass the output of ls to grep
ls | grep muffin

# Create and remove a directory
cd /home/analyst
ls /home/analyst
mkdir logs
rmdir temp

# Create a new file and open it using nano
touch newEmployee.txt
nano newEmployee.txt

# Display the current working directory
pwd

# View file permissions, including hidden files, and modify user permissions
ls -la
chmod u-w,u=r statement_m.txt

# Use sudo to execute administrative commands with elevated privileges
sudo usermod -g lab_team scientist1
cd /home/scientist/projects
ls /home/scientist/projects
sudo chown scientist1 /home/scientist/projects/project_11.txt
sudo userdel scientist1

# Decrypt a cipher using character translation
cat .hiddenFile3 | tr "d-za-cD-ZA-D" "a-zA-Z"

# View two files before comparing their hashes
cat file1.txt
cat file2.txt

# Generate SHA-256 hashes to compare file contents
sha256sum file1.txt
sha256sum file2.txt
