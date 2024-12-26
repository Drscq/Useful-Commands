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
    2.0 Enable QEMU Emulation
    If you haven’t already, set up QEMU to emulate the arm64 architecture:
    ```bash
    docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
    ```
    2.1 Handle Platform Mismatch
    If the platform mismatch issue persists, you can specify the platform explicitly:
    ```bash
    docker run --platform linux/arm64 --entrypoint /bin/bash -p 2000:2000 -it -d triconverge-oram
    ```
    ```bash
    docker run --platform linux/arm64 --entrypoint /bin/bash -p 5000:5000 -it -d triconverge-oram
    ```
3. Access the Container with an Interactive Shell
Use the docker exec command to open an interactive shell inside the running container:
```bash
docker exec -it <container_id_or_name> /bin/bash
```
4. Detach from the Container
To exit the interactive shell without stopping the 
```bash
exit
```


Ah, got it! If a Docker container has exited and you want to restart it, here’s how you can do it:

### Steps to Restart an Exited Docker Container

1. **List All Containers (Including Exited Ones)**:
   - Use the `docker ps -a` command to see all containers, including those that have exited:
     ```bash
     docker ps -a
     ```
   - Look for your exited container in the list. Note its **Container ID** or **Name**.

2. **Restart the Container**:
   - Use the `docker restart` command followed by the Container ID or Name:
     ```bash
     docker restart <container-id-or-name>
     ```
   - Example:
     ```bash
     docker restart my_exited_container
     ```

3. **Attach to the Restarted Container** (Optional):
   - If the container was interactive and you want to reattach to it, use:
     ```bash
     docker start -ai <container-id-or-name>
     ```
   - Example:
     ```bash
     docker start -ai my_exited_container
     ```

4. **Verify the Container is Running**:
   - Use `docker ps` to check if the container has restarted successfully:
     ```bash
     docker ps
     ```

---

### Important Notes
- If the container exits immediately after restarting, it could be because the container’s main process finishes quickly. You can check the logs for more details:
  ```bash
  docker logs <container-id-or-name>
  ```

- If you need to make changes (e.g., update the command or configuration), you might need to remove the container and create a new one:
  ```bash
  docker rm <container-id-or-name>
  docker run <new-options>
  ``` 
