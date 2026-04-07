# RSA Cryptography Simulator

An end-to-end Python implementation of the RSA public-key cryptosystem. This simulator was built to demonstrate the core mathematical primitives behind asymmetric encryption, key generation, and secure data transmission.

## Why Python over C/C++?
In embedded systems, C and C++ are the industry standards. However, native C/C++ integer types max out at 64 bits (unsigned `long long`). Real-world RSA requires manipulating prime numbers and their product that are hundreds or thousands of bits long. 

Implementing this in C would require building or integrating a complex multi-precision arithmetic library (like GMP). Python 3 natively supports arbitrarily large integers (BigInts) under the hood. Using Python allows this project to focus purely on the **cryptographic logic and mathematical algorithms** without getting impeded by buffer overflows and memory management of large numbers.

## Prerequisites & Tools
To run this simulator locally, you will need:
* **Python 3.8+**
* **VS Code** (Recommended IDE)
* **Python Extension for VS Code** (for linting and environment management)

## How to Run the Script
This project is designed to run in an isolated virtual environment.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mateist04/rsa-simulator.git](https://github.com/mateist04/rsa-simulator.git)
   
   cd rsa-simulator
   ```

2. **Create and activate the virtual environment:**
   * **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Execute the simulator:**
   ```bash
   python rsa_simulator.py
   ```

## The Mathematics of RSA
RSA is an asymmetric cryptographic algorithm relying on a "trapdoor function"—a math operation that is easy to perform in one direction but virtually impossible to reverse without a special piece of information.

1. **Key Generation:** We select two distinct prime numbers, $p$ and $q$, and calculate their product $n = p \times q$. This $n$ becomes the modulus for both keys.
2. **Euler's Totient:** We calculate $\phi(n) = (p-1)(q-1)$. This represents the count of integers up to $n$ that are relatively prime to $n$.
3. **Public Key ($e$):** Chosen such that $1 < e < \phi(n)$ and $e$ is coprime with $\phi(n)$.
4. **Private Key ($d$):** Calculated as the modular multiplicative inverse of $e$ modulo $\phi(n)$ ($(e \times d) \pmod{\phi(n)} = 1$).

**Encryption** relies on the public key: $C \equiv M^e \pmod{n}$  
**Decryption** relies on the private key: $M \equiv C^d \pmod{n}$

## Algorithms used

### 1. Greatest Common Divisor (GCD)
To ensure the public exponent $e$ is coprime with $\phi(n)$, their GCD must be $1$. This simulator implements the **Euclidean Algorithm**, which efficiently finds the GCD by repeatedly replacing the larger number with the remainder of dividing the larger by the smaller until the remainder is zero.

### 2. The Extended Euclidean Algorithm (Modular Inverse)
Calculating the private key $d$ is the most complex step. We must find a number $d$ such that $(e \times d) \pmod{\phi(n)} = 1$.

A brute-force search is computationally impossible for large numbers. Instead, the simulator implements the **Extended Euclidean Algorithm (EEA)**. While finding the GCD, the EEA simultaneously tracks the coefficients of Bézout's identity, effectively working backward through the division steps to isolate $d$.

## Bibliography

* [RSA Algorithm - Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) - A comprehensive overview of the mathematical foundations of RSA.
* [The Extended Euclidean Algorithm](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/) - Practical explanation and implementation details for the EEA.
