ip_mac_table = {}

def process_arp_packet(ip, mac):
    if ip in ip_mac_table and ip_mac_table[ip] != mac:
        print(f'🚨 [ALERT] Possible ARP Poisoning Detected for {ip}!')
        print(f'    Original MAC: {ip_mac_table[ip]} | Spoofed MAC: {mac}')
    else:
        ip_mac_table[ip] = mac

if __name__ == '__main__':
    process_arp_packet('192.168.1.1', '00:11:22:33:44:55')
    process_arp_packet('192.168.1.1', 'AA:BB:CC:DD:EE:FF')
