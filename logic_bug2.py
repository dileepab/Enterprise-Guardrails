import os
import logging
import subprocess

# 1. SAST-001: Hardcoded Secret (modified to catch length >=3)
password = "123"
api_key = "abcdef123456"

# 8. STYLE-002: Bad Class Name (should be CapWords)
class badClassName:
    def __init__(self):
        # 5. LOG-002: Logger check
        self.logger = logging.getLogger("test")

    def dangerous_actions(self, user_input):
        # 4. LOG-001: Avoid print
        print("Starting dangerous actions...")

        # 2. SAST-002: Eval
        eval("2 + 2")

        # 3. SAST-003: Exec
        exec("import sys")

        # 6. SAST-004: SQL Injection (concatenation)
        query = "SELECT * FROM users WHERE name = '" + user_input + "'"

        # 7. SAST-005: System Command
        os.system("rm -rf /tmp/*")
        subprocess.call(["ls", "-la"])

        try:
            val = 1 / 0
        # 9. ERR-001: Bare Except
        except:
            print("Something went wrong")

# 10. LIC-001: Restricted License Heade
# This software is released under the GNU General Public License v3.0.0

def calculate_average(numbers):
    total = 0
    # BUG: Off-by-one error in loop range, misses the last element
    for i in range(len(numbers) - 1):
        total += numbers[i]

    # BUG: Potential division by zero if list is empty
    return total / len(numbers)

def find_item(items, target):
    i = 0
    # BUG: Infinite loop if target is not in items
    while i < len(items):
        if items[i] == target:
            return i
        # Forgot to increment i implies infinite loop
    return -1


