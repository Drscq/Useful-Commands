To install **GMP** locally in `/root/local/lib/libgmp.a`, follow these steps:

---

### **Step 1: Download GMP Source Code**
Download the source code for GMP (GNU Multiple Precision Arithmetic Library):
```bash
wget https://gmplib.org/download/gmp/gmp-6.2.1.tar.xz
```
*(Replace `6.2.1` with the latest version available from the [GMP website](https://gmplib.org).)*

---

### **Step 2: Extract the Archive**
Extract the downloaded tarball:
```bash
tar -xvf gmp-6.2.1.tar.xz
cd gmp-6.2.1
```

---

### **Step 3: Configure the Build**
Configure the GMP library to install locally under `/root/local`:
```bash
./configure --prefix=/root/local --enable-cxx
```
- `--prefix=/root/local` specifies the installation path.
- `--enable-cxx` enables C++ support for GMP.

---

### **Step 4: Build GMP**
Compile GMP using `make`:
```bash
make -j$(nproc)
```
- `-j$(nproc)` speeds up compilation by using all available CPU cores.

---

### **Step 5: Install GMP**
Install GMP to the specified local directory:
```bash
make install
```

---

### **Step 6: Verify Installation**
Check if GMP has been installed to `/root/local/lib`:
```bash
ls /root/local/lib/libgmp.a
```
You should see the `libgmp.a` static library and possibly `libgmp.so` for shared library use.

---

### **Step 7: Update Environment Variables (Optional)**
To make the locally installed GMP accessible globally:
1. Add `/root/local/lib` to `LD_LIBRARY_PATH`:
   ```bash
   export LD_LIBRARY_PATH=/root/local/lib:$LD_LIBRARY_PATH
   ```
2. Add `/root/local/include` to `CPLUS_INCLUDE_PATH` (for headers):
   ```bash
   export CPLUS_INCLUDE_PATH=/root/local/include:$CPLUS_INCLUDE_PATH
   ```

You can append these lines to `/root/.bashrc` to make them permanent.

---

### **Step 8: Link GMP in Your Project**
Ensure your `CMakeLists.txt` links to the local GMP installation:
```cmake
target_link_libraries(crtgamal
    /root/local/lib/libgmp.a
    ...
)
```

---

Once GMP is installed locally, you can proceed to rebuild your project using `make`. Let me know if you encounter any issues!