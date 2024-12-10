1. Load a .tar file into a docker image
```bash
docker load -i <path to tar file>
```
2. run a container based on a image
```bash
docker run -it -p 8183:8183 your_image_name /bin/bash
```    
* -it: interactive mode 
* -p 8183:8183: Maps port 8183 in the container to port 8183 on the host machine.
* /bin/bash: Starts the container with a Bash shell

    2.1 Handle Platform Mismatch
    If the platform mismatch issue persists, you can specify the platform explicitly:
    ```bash
    docker run --platform linux/arm64 --entrypoint /bin/bash -p 8188:8188 -it triconverge-oram
    ```


