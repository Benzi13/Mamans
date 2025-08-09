# 📚 Maman 11 – C++ Programs  

This repository contains my solutions to **Maman 11**, organized so each question is in its own folder.  

---

## 📂 Folder Structure & Compilation Details  

### **1️⃣ Question 1**  
- **Content:** Single PDF file with the solution.  

---

### **2️⃣ Question 2**  
- **Files:**  
  - `my_vec.h` – Header file  
  - `my_vec.cpp` – Implementation file  
  - `2.exe` – Compiled executable  
- **Compile Command:**  
  ```bash
  g++ my_vec.cpp -o 2.exe
  ```

---

### **3️⃣ Question 3**  
- **Files:**  
  - `all_vecs.h` and `my_vec.h` – Header files  
  - `all_vecs.cpp` and `named_vector.cpp` – Implementation files  
  - `3.exe` – Compiled executable  
- **Note:** Question 3 depends on the solution from Question 2.  
- **Compile Command:**  
  ```bash
  g++ 3/all_vecs.cpp 2/my_vec.cpp 3/named_vector.cpp -o 3.exe
  ```

---

### **4️⃣ Question 4**  
- **Files:**  
  - `read_csv.cpp` – Implementation file  
  - `4.exe` – Compiled executable  
  - `examples/` – Folder containing example input/output  
- **Note:** No header file was created, since this solution wasn’t written as a reusable class.  
- **Compile Command:**  
  ```bash
  g++ read_csv.cpp -o 4.exe
  ```

---

✅ **Tip:** Make sure to navigate into the correct folder before compiling each solution.  
