import struct

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        return struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

# 실행 테스트
if __name__ == "__main__":
    udp = Udphdr(5555, 80, 1000, 0xFFFF)
    packed = udp.pack_Udphdr()
    print(packed)  # b'...' 형태로 출력됨

    unpacked = unpack_Udphdr(packed)
    print(unpacked)
    print("Source Port:{} Destination Port:{} Length:{} Checksum:{}".format(
        getSrcPort(unpacked), getDstPort(unpacked), getLength(unpacked), getChecksum(unpacked)
    ))
