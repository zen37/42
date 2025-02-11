# Secrets

When dealing with sensitive information like API keys in a Python project, it's crucial to store them securely to prevent unauthorized access. Here are some best practices for storing API keys locally:

### 1. **Environment Variables**
   - **Why?** Environment variables are a common and secure way to store sensitive information. They keep the keys out of your source code, reducing the risk of accidentally exposing them.
   - **How?**
     - Create a `.env` file in your project directory:
       ```plaintext
       API_KEY=your_api_key_here
       ```
     - Use the `python-dotenv` package to load the environment variables from the `.env` file:
       ```bash
       pip install python-dotenv
       ```
       ```python
       from dotenv import load_dotenv
       import os

       load_dotenv()  # Load environment variables from .env file
       api_key = os.getenv('API_KEY')
       ```
     - Add `.env` to your `.gitignore` file to ensure it doesn't get committed to version control:
       ```plaintext
       .env
       ```

### 2. **Configuration Files**
   - **Why?** Configuration files can be used to store sensitive information, but they should be kept out of version control.
   - **How?**
     - Create a `config.py` file:
       ```python
       API_KEY = 'your_api_key_here'
       ```
     - Import the configuration in your main script:
       ```python
       from config import API_KEY
       ```
     - Add `config.py` to your `.gitignore` file:
       ```plaintext
       config.py
       ```

### 3. **Keyring (Platform-Specific Key Storage)**
   - **Why?** The `keyring` library provides a secure way to store and retrieve passwords and keys using the system's keychain.
   - **How?**
     - Install the `keyring` package:
       ```bash
       pip install keyring
       ```
     - Store the API key:
       ```python
       import keyring

       keyring.set_password('my_app', 'api_key', 'your_api_key_here')
       ```
     - Retrieve the API key:
       ```python
       api_key = keyring.get_password('my_app', 'api_key')
       ```

### 4. **Encrypted Files**
   - **Why?** Encrypting the API key adds an extra layer of security, making it harder for unauthorized users to access the key even if they gain access to the file.
   - **How?**
     - Use a library like `cryptography` to encrypt and decrypt the API key:
       ```bash
       pip install cryptography
       ```
     - Encrypt the API key and store it in a file:
       ```python
       from cryptography.fernet import Fernet

       key = Fernet.generate_key()
       cipher_suite = Fernet(key)
       encrypted_api_key = cipher_suite.encrypt(b'your_api_key_here')

       with open('encrypted_key.txt', 'wb') as file:
           file.write(encrypted_api_key)
       ```
     - Decrypt the API key when needed:
       ```python
       with open('encrypted_key.txt', 'rb') as file:
           encrypted_api_key = file.read()

       decrypted_api_key = cipher_suite.decrypt(encrypted_api_key).decode()
       ```

### 5. **Secrets Management Services (for Advanced Use Cases)**
   - **Why?** For more complex applications, especially in cloud environments, you might want to use a secrets management service like AWS Secrets Manager, Azure Key Vault, or HashiCorp Vault.
   - **How?**
     - These services provide APIs to securely store and retrieve secrets, and they often integrate well with cloud environments.

### Summary
- **For most local development:** Use environment variables with a `.env` file and `python-dotenv`.
- **For added security:** Consider using the `keyring` library or encrypting the API key.
- **For production or cloud environments:** Use a secrets management service.

Always ensure that any file containing sensitive information is excluded from version control by adding it to your `.gitignore` file.

---

### **What Are Environment Variables?**
- Environment variables are key-value pairs stored in the operating system's memory.
- They are accessible to all processes running in that environment.
- Examples include `PATH`, `HOME`, or custom variables like `API_KEY`.
- They are typically set in the shell or system configuration files (e.g., `.bashrc`, `.zshrc`, or system settings).

---

### **Why Use a `.env` File?**
- **Convenience during development:** Instead of manually setting environment variables in the shell every time you run your application, you can use a `.env` file to store them in one place.
- **Portability:** A `.env` file makes it easy to share configuration settings across different environments (e.g., development, testing, production) without hardcoding values into your code.
- **Security:** By keeping sensitive data like API keys in a `.env` file (and adding it to `.gitignore`), you avoid accidentally committing secrets to version control.

---

### **How `.env` Files Relate to Environment Variables**
- A `.env` file is **not** the same as an environment variable. It is simply a text file that contains key-value pairs.
- Tools like `python-dotenv` read the `.env` file and load its contents into the **actual environment variables** of the running process.
- For example:
  ```plaintext
  # .env file
  API_KEY=your_api_key_here
  ```
  When you use `python-dotenv`:
  ```python
  from dotenv import load_dotenv
  import os

  load_dotenv()  # Loads the .env file into environment variables
  api_key = os.getenv('API_KEY')  # Accesses the environment variable
  ```
  Here, `load_dotenv()` reads the `.env` file and sets the `API_KEY` as an actual environment variable in memory.

---

### **Why Not Just Use Environment Variables Directly?**
- **Manual setup:** You would need to manually set environment variables in your shell or system configuration, which can be tedious and error-prone.
  ```bash
  export API_KEY=your_api_key_here
  ```
- **Inconsistency:** If you forget to set the variable, your application might fail or behave unexpectedly.
- **Cross-platform issues:** Different operating systems handle environment variables differently (e.g., `export` in Unix-like systems vs. `set` in Windows).

---

### **When to Use Actual Environment Variables (Not `.env`)**
- **Production environments:** In production, you should avoid using `.env` files and instead set environment variables directly in the system or container (e.g., using Docker, Kubernetes, or cloud platforms).
- **Security:** Environment variables are more secure than `.env` files because they are stored in memory and not written to disk (unless explicitly saved in a file).

---

### **Summary**
- **Environment variables** are stored in memory and are part of the operating system's environment.
- **`.env` files** are a development convenience to simulate environment variables by loading them into memory at runtime.
- In production, you should rely on actual environment variables set in the system or container, not `.env` files.

If you're working on a local development environment, using a `.env` file is perfectly fine and widely adopted. Just make sure to exclude it from version control (e.g., by adding it to `.gitignore`). For production, always use actual environment variables or a secrets management service.