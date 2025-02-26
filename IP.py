class IPaddress:
    """
    defines an IP address objects, and basic operations on them
    """
    def __init__(self, ipAddress, netmask=-1):
        if isinstance(ipAddress, str):
            if ipAddress.count('.') != 3:
                raise ValueError('Invalid IP address: it must be a string with 3 dots')
        else:
            raise ValueError('Invalid IP address: it must be a string with 3 dots')
        
        self.ip = ipAddress
        self.ipBin = int(self.toBin()[2:], 2)
        self.netmask = netmask

    def toBin(self):
        """
        prende un indirizzo IP sottoforma di stringa puntuata e lo restituisce come numero binario a 32 bit
        """
        ipPieces = self.ip.split('.')
        ipBin = '0b'
        for word in ipPieces:
            ipBin += self.__padding(bin(int(word)).split('b')[1])

        return ipBin

    def __padding(self, partialIP):
        l = len(partialIP)
        return ('0' * (8-l)) + partialIP

    def __str__(self):
        binary_str = self.toBin()[2:]

        # Pad the binary string with zeros at the beginning if it's less than 32 bits
        binary_str = binary_str.zfill(32)

        # Format the binary string to add a dot every 8 characters
        formatted_binary_str = '.'.join(binary_str[i:i+8] for i in range(0, 32, 8))

        return f"IP: {self.ip}\nBinary IP: {formatted_binary_str}"