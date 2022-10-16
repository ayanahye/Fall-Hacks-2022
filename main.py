# a program that blocks apps that pull you away from what youre supposed to be doing.
from datetime import datetime 

d = datetime.now()
d = int(d.strftime("%d"))

end_time = datetime(2022, 10, d+1, 20)

# must run the program as an administrator
from flask import Flask, request, redirect, url_for, render_template
# host is an os file that maps hostnames to ip addresses, 
app = Flask(__name__)

@app.route("/home")
@app.route("/index.html")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html", methods = ['POST', 'GET'])
@app.route('/', methods = ['POST', 'GET'])

def home():
    if request.method == 'POST':
        website = request.form.get("website")
        button = request.form['submit']
        if button == "Block":
            try:
                question(website, "blocker")
                success = "Successful"
            except:
                success = "Unsuccessful"
        elif button == "Unblock":
            try:
                question(website, "unblock")
                success = "Successful"
            except:
                success = "Unsuccessful"

        return render_template("index.html", success=success, website=website)


# path of our host file

# if operating system is linux use this as the host path:
#Linux_host = '/etc/hosts'

# if os is windows
host_path = "C:\Windows\System32\drivers\etc\hosts"

# ip address used by localhost
redirect = "127.0.0.1"

#website_list = ["www.twitter.com", "twitter.com"]


def blocker(website):

    website = str(website)
    website_list = []
    website_list.append(website)

    if datetime.now() < end_time:
    
        print("Blocking..")
        print(website)
        # opens file and automatically closes it
        # +r means for reading and writing
        with open(host_path, 'r+') as host_file:
            file_content = host_file.read()
            for website in website_list:
                # if it is already blocked
                if website in file_content:
                    pass
                else:
                    # else it will block that website
                    host_file.write(redirect + " " + website + '\n')
                print("Blocked")

    elif datetime.now() > end_time:
        print('Unblock sites')
        with open(host_path, 'r+') as host_file:
            lines = host_file.readlines()
            host_file.seek(0)
            for line in lines:
                if not any(website in line for website in website_list):
                    host_file.write(line)
            host_file.truncate()

def unblock(website):
    host_path = "C:\Windows\System32\drivers\etc\hosts"

    # ip address used by localhost
    redirect = "127.0.0.1"
    
    print("working")
    website_list = []
    website = str(website)
    website_list.append(website)

    # type website then click the button
    print(website)

    with open(host_path, 'r+') as host_file:
        content = host_file.readlines()
        host_file.seek(0)
        print(website)
        for line in content:
            if not any(website in line for website in website_list):
                host_file.write(line)
        host_file.truncate()
        print("Unblocked.")
    website_list = []

def question(website, button):
    if button == "unblock":
        unblock(website)
    else:
        blocker(website)



if __name__ == '__main__':
    app.run(debug=True)
