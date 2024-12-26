## iperf3 to do the bandwidth test
### **Server (Remote Machine)**
Start the server:
```bash
iperf3 -s
```

Or specify a custom port:
```bash
iperf3 -s -p <port>
```

---

### **Client (Local Machine)**
Run the client:
```bash
iperf3 -c <server_ip>
```

With a custom port:
```bash
iperf3 -c <server_ip> -p <port>
```

For a longer test (e.g., 20 seconds):
```bash
iperf3 -c <server_ip> -t 20
```

For multiple parallel streams (e.g., 4 streams):
```bash
iperf3 -c <server_ip> -P 4
```

For a UDP test:
```bash
iperf3 -c <server_ip> -u
```

## Potential Troubleshooting

### Firewall Rules:
```bash
sudo ufw allow 5201
```