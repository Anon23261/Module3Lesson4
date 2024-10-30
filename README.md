# Module3Lesson4
Assignment

Email Extraction with Python Regex
Objective
This project extracts email addresses from a text while excluding those from a specific domain (exclude.com).

Features
Extracts valid email addresses.
Excludes emails from the specified domain.
How to Run
Make sure you have Python 3 installed.
Download the script.
Open your terminal and navigate to the folder with the script.
Run the script using:
bash
Copy code
python script_name.py
Sample Input
The script uses the following sample text:

python
Copy code
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
Expected Output
The output will be:

python
Copy code
['user1@domain.com', 'user3@domain.com']
This shows the emails that are not from exclude.com.

Code Explanation
The code uses a regular expression to find email addresses and a negative lookahead to exclude any that are from exclude.com.
