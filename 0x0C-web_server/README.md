Background Context


In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)
For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:
```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```
As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

A good Software Engineer is a lazy Software Engineer. 

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

- start a Ubuntu 16.04 sandbox
- run your script on it
- see how it behaves
**Resources**
Read or watch:

- [How the web works](https://intranet.alxswe.com/rltoken/6TI3HiyFdwrbXWKVF24Gxw)
- [Nginx](https://intranet.alxswe.com/rltoken/vkVMGlaf39j2DWAQWzo6EA)
- [How to Configure Nginx](https://intranet.alxswe.com/rltoken/zKrpVxWuUHVdW4URAjdFbw)
- [Child process concept page](https://intranet.alxswe.com/rltoken/Ar18u5sRis1fkvkVgzdcqg)
- [Root and sub domain](https://intranet.alxswe.com/rltoken/xi3peVqYl02PfpHHHlCtxQ)
- [HTTP requests](https://intranet.alxswe.com/rltoken/sBrrP4EAmI3NoYjIgZrUhw)
- [HTTP redirection](https://intranet.alxswe.com/rltoken/Eaa4ZuKvye941hTkP8VlBQ)
- [Not found HTTP response code](https://intranet.alxswe.com/rltoken/eJSp2QFTY6jqqNtz8OVDEw)
- [Logs files on Linux](https://intranet.alxswe.com/rltoken/7WMNY5CWD-CBrxmQrdmfPg)
- [How to transfer files between hosts in linux](https://www.geeksforgeeks.org/scp-command-in-linux-with-examples/)
For reference:

- RFC 7231 (HTTP/1.1)
- RFC 7540 (HTTP/2)
man or help:

`scp`

`curl`

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests
- DNS
- What DNS stands for
- What is DNS main role
**DNS Record Types**
- A
- CNAME
- TXT
- MX
0. Transfer a file to your server
mandatory
Write a Bash script that transfers a file from our client to a server:

Requirements:

- Accepts 4 parameters
	- The path to the file to be transferred
	- The IP of the server we want to transfer the file to
	- The username scp connects with
	- The path to the SSH private key that scp uses
- Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
- scp must transfer the file to the user home directory ~/
- Strict host key checking must be disabled when using scp
Example: 
```
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```
In this example, I:

- remotely execute the ls ~/ command via ssh to see what ~/ contains
- create a file named some_page.html
- execute my 0-transfer_file script
- remotely execute the ls ~/ command via ssh to see that the file some_page.html has been successfully transferred
That is one way of publishing your website pages to your server.
2. Setup a domain name
mandatory
.TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

YOU can have a free .tech domain for 1 year by following these steps:
(ONLY FOR ALX STUDENTS, steps were shown)

Access the tools space
Unlock the GitHub student pack: WARNING - this invitation link is unique to you and can’t be reclaimed! If you have any issue, please contact GitHub education support


When registered, access your benefits:


And scroll to .Tech domain:


Start to register your domain and checkout
At the Checkout step, please click on “Login with GitHub”:
 

- The cost of the domain should be now at $0
- You can finalize it by creating an account in .Tech domains
- And manage your domain there!
-Provide the domain name in your answer file.

Requirement:

- provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)
- configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)
- go to your profile and enter your domain in the Project website url field
Example:
```
sylvain@ubuntu$ cat 2-setup_a_domain_name
myschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig myschool.tech

; <<>> DiG 9.10.6 <<>> myschool.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;myschool.tech.     IN  A

;; ANSWER SECTION:
myschool.tech.  7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
```
When your domain name is setup, please verify the Registrar here: https://whois.whoisxmlapi.com/ and you must see in the JSON response: "registrarName": "Dotserve Inc"
file: `2-setup_a_domain_name`

3. Redirection
mandatory
Readme:

- [Replace a line with multiple lines with sed](https://intranet.alxswe.com/rltoken/RRP9hX3MlQdABaKZD-Y_cA)
Configure your Nginx server so that /redirect_me is redirecting to another page.

Requirements:

- The redirection must be a “301 Moved Permanently”
- You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
- Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task
Example:
```
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
```
File: `3-redirection`
