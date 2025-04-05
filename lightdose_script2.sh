#!/bin/bash

# LIGHT DOSE - SCRIPT 2


# Generating random battery percent b/w 0 and 100
bat_per=$(shuf -i 0-100 -n 1)

# Displaying the battery status
echo "Battery percentage: $bat_per%"

# Checking if battery is below 20%
if [ $bat_per -lt 20 ]; then
  echo "Battery low! Return to base!"
  exit 1  # Exit the script
fi

# Checking network connectivity by testing Firefox's access to a website
curl -s --head https://www.mozilla.org | head -n 1

# Check if the ping command was successful
if [ $? -ne 0 ]; then
  echo "Communication failure!"
  exit 1  # Exit the script
fi

# If both checks pass, display the message that all systems are operational
echo "All systems operational!"

# We could have used 0 after exit instead of 1, it won't have any impact on our output. 1 is tell system that there was some error, this would be helpful when there are multiple programs and their working depends on each other.
