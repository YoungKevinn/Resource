from pwn import *

# Tạo shellcode
shellcode = shellcraft.execve('/bin/bash')

# In ra mã hex
print(asm(shellcode))
