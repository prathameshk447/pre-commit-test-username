#!/usr/bin/env python3

import subprocess

expectedUsername = "prathamesh"

username = subprocess.run(["git", "config", "user.username"], capture_output=True, text=True).stdout.strip()

if username == expectedUsername:
            print("You are using username as per configuration, proceeding to commit")
            exit(0)
else:

            print(f"Configured username is not as per config. It should be {expectedUsername}")
            exit(1)

