## Device Info

Below is a **concise, Linux-native toolkit** to extract precisely the information (e.g., model, CPU, RAM, Disk).

### Machine model (server idenity)

```bash
sudo dmidecode -s system-manufacturer
sudo dmidecode -s system-product-name
```

### CPU model, cores, threads

```bash
lscpu
```

Minimal extraction:
```bash
lscpu | egrep 'Model name|Socket|Core|Thread|CPU\(s\)|MHz'
```

Or ultra-precise:
```bash
cat /proc/cpuinfo | grep "model name" | uniq
```


### Total system RAM
```bash
free -h
```

### Disk type, size, and device
```bash
lsblk -o NAME,MODEL,SIZE,TYPE,MOUNTPOINT
```
Filesystem-level view:

```bash
df -h
```

### Network adapters (useful for bandwidth claims)
```bash
lspci | grep -i ethernet
```
## One-shot “paper snapshot” command

If you want a single reproducible log for artifacts or appendix:

```bash
echo "=== SYSTEM ==="
hostnamectl
echo "=== CPU ==="
lscpu
echo "=== MEMORY ==="
free -h
echo "=== DISK ==="
lsblk -o NAME,MODEL,SIZE,TYPE
echo "=== NETWORK ==="
lspci | grep -i ethernet
```


