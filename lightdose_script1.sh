# Specifying the shell to be used
#!/bin/bash


# LIGHT DOSE - SCRIPT 1

# Creating a new directory
mkdir rover_mission

# Changing current directory to this new directory
cd rover_mission

# creating 3 empty text files
touch log1.txt 
touch log2.txt
touch log3.txt

# renaming log1.txt to mission_log.txt
mv log1.txt mission_log.txt

# Find all files with .log extension
find . -type f -name "*.log"

# Writing some text in mission_log.txt
echo -e "Neele neele ambar par ERROR\nchand jab aye \nPyar barsae ERROR\nHumko tarsae" >> mission_log.txt

# Displaying the contents of mission_log.txt
cat mission_log.txt

# Find and display all lines containing "ERROR"
grep "ERROR" mission_log.txt

# Counting the number of lines
wc -l mission_log.txt

# showing the system's current date and time
date

# Display CPU usage in real-time
top -n 1

# Scheduling shutdown in 10 minutes
sudo shutdown -h +10

