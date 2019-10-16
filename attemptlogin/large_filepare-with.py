#!usr/bin/env python3
loginfail = 0
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            print(line)
            print("Please check IP Address: ",line.split(" ")[-1])
            loginfail += 1
print("The number of failed log in the attempts is", loginfail)
