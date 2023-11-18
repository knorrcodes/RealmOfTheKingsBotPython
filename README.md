How to get up in running with docker
1. get you aws creds
2. place those creds in a file called "keys.env" in the projects root dir
3. navigate to the projects root directory
4. in the cli, use the following command:
    "docker build -t rotk_python && docker run --env-file keys.env -d rotk_python"
5. to get the logs, run the following commands
    "docker ps" -> this will get you the container ID
    "docker logs -f <container id>