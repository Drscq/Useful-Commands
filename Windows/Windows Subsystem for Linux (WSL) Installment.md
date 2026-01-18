## Step 1: Enable WSL feature
Open PowerShell as Administrator:
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```
👉 If you want WSL2 (recommended if supported):
```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
## Step 2:REBOOT the server (important)
You must restart before continuing.
```powershell
shutdown /r /t 0
```
⏳ After reboot, log back in as Administrator.

## Step 3: Install WSL (Windows Server way)
Since Windows Server has no Microsoft Store, do it manually.
**Download Ubuntu 22.04**
```powershell
wsl.exe --install
```

## Step 4: Verify WSL is working
```powershell
uname -a
```

## Step 5: Launch WSL in a new directory
### Step 1: Go to the directory in Windows
```powershell
cd C:\Users\username\Documents
```
### Step 2: Launch WSL here
Type the following in the directory:
```powershell
wsl
```





