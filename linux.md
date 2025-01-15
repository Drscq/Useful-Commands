1. Check the OS distribution on your linux machine
```bash
cat /etc/os-release
```
2. Ensure a service is running on port 8183 on the host
    * Use netstat to confirm that port 8183 is in a LISTEN state
    ```bash
    sudo netstat -tuln | grep 8183
    ```
3. Add the New User
    ```bash
    sudo adduser username
    ```
    3.1 Add the User to the sudo Group
    ```bash
    sudo usermod -aG sudo username
    ```