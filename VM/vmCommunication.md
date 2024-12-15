## Two Goals
- **Direct VM-to-VM communication** on a shared network (for easy socket connections between the VMs).
- **Port forwarding from the outside world** (your local machine) through the host to the VMs, so that external clients (or your local workstation) can reach services running inside the VMs.

## Option 1: Use a linux Bridge for VM-VM Communication and the Host's Firewall for Port Forwarding

1. **Set Up a Linux Bridge**
    Create a Linux bridge `bro` on the host. Connect both VMs to the bridge via tap interfaces. This puts both VMs on the same L2 network and allows direct communication.
    ```bash
    # On the host:
    sudo ip link add name br0 type bridge
    sudo ip link set br0 up

    # Add TAP interfaces
    sudo ip tuntap add dev tap0 mode tap user $(whoami)
    sudo ip link set tap0 master br0
    sudo ip link set tap0 up

    sudo ip tuntap add dev tap1 mode tap user $(whoami)
    sudo ip link set tap1 master br0
    sudo ip link set tap1 up
    ```
    Launch each VM using `-netdev tap` and `-device virtio-net-pci` attached to `tap0` and `tap1` respectively.
2. **Assign IP Addresses to VMs**  
   Within the VMs, assign static IPs on the interface connected to `br0`. For example:
   - VM1: `192.168.100.2/24`
   - VM2: `192.168.100.3/24`

   Both can ping each other now.

3. **Port Forwarding from the Outside**  
   If you have control over the host machine’s firewall (using `iptables` or `nftables`), you can forward external requests to a particular VM service. For instance, suppose the host is accessible at `<HOST_PUBLIC_IP>` and you want to forward TCP port 8080 to VM1’s IP (192.168.100.2 port 8080):
   ```bash
   # Assuming iptables
   sudo iptables -t nat -A PREROUTING -p tcp -d <HOST_PUBLIC_IP> --dport 8080 -j DNAT --to-destination 192.168.100.2:8080
   sudo iptables -A FORWARD -p tcp -d 192.168.100.2 --dport 8080 -j ACCEPT
   ```

   This way, a connection from your local machine to `<HOST_PUBLIC_IP>:8080` would be forwarded by the host’s firewall to VM1.

   You can repeat this for any services running on any VM. This gives you flexibility and full VM-to-VM communication on the internal bridge.
