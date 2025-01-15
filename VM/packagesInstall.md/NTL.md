Given the `CMakeLists.txt` file you provided, you need to install the **NTL (Number Theory Library)** and configure it to work with your project. Here’s how to do it:

---

### Step 1: Install GMP
First, install GMP, which is a dependency of NTL:
```bash
sudo apt update
sudo apt install libgmp-dev -y
```

---

### Step 2: Download and Build NTL
Download and build NTL from source:

1. **Download NTL:**
   ```bash
   wget https://libntl.org/ntl-11.5.1.tar.gz
   tar -xvzf ntl-11.5.1.tar.gz
   cd ntl-11.5.1/src
   ```

2. **Configure NTL:**
   ```bash
   ./configure NTL_GMP_LIP=on PREFIX=$HOME/local
   ```
   - `PREFIX=$HOME/local` sets the installation path for NTL to a local directory (`$HOME/local`).

3. **Build and Install NTL:**
   ```bash
   make
   make install
   ```

4. **Verify Installation:**
   Check that the NTL library and headers are installed:
   ```bash
   ls $HOME/local/lib/libntl.a
   ls $HOME/local/include/NTL
   ```

---

### Step 3: Configure Your CMake Project
Your `CMakeLists.txt` file should work as-is, as it already specifies:
- The location of the NTL library at `${LOCAL_PREFIX}/lib/libntl.a`.
- The headers in `${LOCAL_PREFIX}/include`.

Make sure `LOCAL_PREFIX` matches the installation path (`$HOME/local`).

---

### Step 4: Build Your Project
Run the following commands to build your project:
```bash
mkdir build
cd build
cmake ..
make
```

---

### Step 5: Troubleshooting
If you encounter issues:
1. **Library Not Found:** Ensure `libntl.a` is in `$HOME/local/lib`.
2. **Include Path Errors:** Verify NTL headers are in `$HOME/local/include/NTL`.
3. **Environment Variables:** Add the library path to `LD_LIBRARY_PATH`:
   ```bash
   export LD_LIBRARY_PATH=$HOME/local/lib:$LD_LIBRARY_PATH
   ```
   To make this change permanent, add it to `~/.bashrc` or `~/.zshrc`.

After these steps, the NTL library should be properly installed, and your project should compile successfully.