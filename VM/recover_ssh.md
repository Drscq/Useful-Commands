When you executed `sudo ip addr flush dev enp225s0f0`, it removed the IP address from the `enp225s0f0` interface, which terminated your SSH session. SSH relies on the IP address of the network interface to establish and maintain the connection. Since the IP address was removed, the server became unreachable over the network.

### To Recover Access:
1. **Re-establish the IP Address:**
   If you have physical access or an out-of-band management interface (like IPMI or iDRAC), log in to the server and manually restore the IP address to `enp225s0f0`:
   ```bash
   sudo ip addr add 198.82.162.130/24 dev enp225s0f0
   sudo ip link set enp225s0f0 up
   ```

2. **Reconnect via SSH:**
   Once the IP is restored, attempt to reconnect using SSH:
   ```bash
   ssh <your_user>@198.82.162.130
   ```

3. **Temporarily Bind the Bridge to the IP:**
   If you intended to use `br0` as the main interface, you must assign the IP address to it **before flushing the original interface**.

---

### Safe Steps to Prevent Disconnection:
1. **Assign the IP to the Bridge First:**
   ```bash
   sudo ip addr add 198.82.162.130/24 dev br0
   sudo ip link set br0 up
   ```

2. **Move `enp225s0f0` to the Bridge:**
   ```bash
   sudo ip link set enp225s0f0 master br0
   ```

3. **Flush the Original Interface:**
   Only flush the IP after verifying that the bridge is active and reachable:
   ```bash
   sudo ip addr flush dev enp225s0f0
   ```

4. **Test Connectivity:**
   Verify that you can still ping the server from another device before closing your SSH session:
   ```bash
   ping 198.82.162.130
   ```

By following these steps, you can safely migrate your network configuration without losing access.