## Password-less SSH Login Setup

### Step 1: Generate SSH Key Pair (on your local machine)

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Press Enter to accept the defaults.

This creates:
- A private key: `~/.ssh/id_rsa`
- A public key: `~/.ssh/id_rsa.pub`

### Step 2: Copy the Public Key to the Remote Linux Server
```bash
ssh-copy-id user@remote_host
```
This command copies the public key to the remote server's `~/.ssh/authorized_keys` file.