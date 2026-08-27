# Linux File, Directory, and User Management
**Google Cybersecurity Professional Certificate — Linux Lab**
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

# The command that shows where you are
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

# Decrypt a cipher using a translation command
cat .hiddenFile3 | tr "d-za-cD-ZA-D" "a-zA-Z"

# Generate hashes of two files to determine if they are different
cat file1.txt
cat file2.txt
sha256sum file1.txt
sha256sum file2.txt

# Use tcpdump to capture and analyze live network traffic
sudo ifconfig
sudo tcpdump -D
sudo tcpdump -i eth0 -v -c 5

# Capture packet data and save it to a file
sudo tcpdump -i eth0 -nn -c 9 port 80 -w capture.pcap &
```
