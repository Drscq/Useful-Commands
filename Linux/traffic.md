# Traffic Shaping with Linux `tc`

On Linux (including WSL2), use `tc` with **HTB** (Hierarchical Token Bucket) queuing discipline to the loopback device.

## Limit all traffic on `lo` to 60mbit

### Add a bandwidth limit to `lo` (loopback) device
```bash
sudo tc qdisc add dev lo root handle 1: htb default 10
sudo tc class add dev lo parent 1: classid 1:10 htb rate 60mbit ceil 60mbit
```

The following one for the 80Mbps limit without the "Warning: sch_htb: quantum of class 10010 is big. Consider r2q change."
```bash
sudo tc qdisc add dev lo root handle 1: htb default 10 r2q 100
sudo tc class add dev lo parent 1: classid 1:10 htb rate 80mbit ceil 80mbit
``` 


### Verify
```bash
tc qdisc show dev lo
tc class show dev lo
```

### Remove the limit when done
```bash
sudo tc qdisc del dev lo root
```

## Alternative: Limit Only iperf Traffic (Cleaner for experiments)
Instead of shaping all `lo`, you can target only port 5201.

```bash
sudo tc qdisc add dev lo root handle 1: htb
sudo tc class add dev lo parent 1: classid 1:1 htb rate 60mbit
sudo tc filter add dev lo protocol ip parent 1:0 prio 1 u32 match ip dport 5201 0xffff flowid 1:1
```



