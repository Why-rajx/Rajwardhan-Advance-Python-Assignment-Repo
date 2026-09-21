import re

data = """
Please contact us at john@example.com or support@gmail.com.
You can also email admin@college.edu.in for further information.
"""

regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

email_list = re.findall(regex, data)

print("Email addresses found:")

for email in email_list:
    print(email)