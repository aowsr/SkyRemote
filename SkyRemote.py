import socket

s = socket.socket()        
host = '192.168.0.12' # place your Sky Q IP Here
port = 49160


class Command:
    power =  0
    select = 1
    backup = 2
    dismiss = 2
    channelup = 6
    channeldown = 7
    interactive = 8
    sidebar = 8
    help = 9
    services = 10
    search = 10
    tvguide = 11
    home = 11
    i = 14
    text = 15 
    up = 16
    down = 17
    left = 18
    right = 19
    red = 32
    green = 33
    yellow = 34
    blue = 35
    zero = 48
    one = 49
    two = 50
    three = 51
    four = 52
    five = 53
    six = 54
    seven = 55
    eight = 56
    nine = 57
    play = 64
    pause = 65
    stop = 66
    record = 67
    fastforward = 69
    rewind = 71
    boxoffice = 240
    sky = 241

c = Command()
code = c.power # change this whatever command you want to send
hex = bytearray([4,1,0,0,0,0, 224 + code // 16, code % 16])
s.connect((host, port))
l = 12
check = True

while check :

    call = s.recv(0)
    receivedText = s.recv(24)
    receivedTextLen = len(receivedText)
    
    if receivedTextLen < 24:
        s.send(bytes(receivedText[0:l]))
        l = 1
    else:
        print('Writing Data')
        s.send(hex)
        hex[1] = 0
        s.send(hex)
        s.close() 
        check = False

s.close()






