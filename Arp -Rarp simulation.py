import ipaddress
import re

# Simulated ARP Table
ARP_TABLE = {
    "192.168.1.1": "00:0a:95:9d:68:16",
    "192.168.1.2": "00:0a:95:9d:68:17",
    "192.168.1.3": "00:0a:95:9d:68:18",
}

# Simple pattern checking for XX:XX:XX:XX:XX:XX format
MAC_PATTERN = r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"

def lookup_ip(ip_address):
    # Validates and normalizes the IP format (e.g., removing leading zeros)
    clean_ip = str(ipaddress.IPv4Address(ip_address))
    return ARP_TABLE.get(clean_ip)

def lookup_mac(mac_address):
    # Validates the MAC format using regex
    if not re.match(MAC_PATTERN, mac_address):
        print("Error: Invalid MAC format. Use 00:11:22:33:44:55")
        return None
        
    # Standard loop to search for the value
    for ip, mac in ARP_TABLE.items():
        if mac.lower() == mac_address.lower():
            return ip
    return None

def main():
    while True:
        mode = input("\nChoose mode (arp / rarp / quit): ").strip().lower()
        
        if mode in ("quit", "q"):
            break
            
        elif mode == "arp":
            ip = input("Enter IPv4 Address: ").strip()
            try:
                mac = lookup_ip(ip)
                print(f"ARP Reply: {mac}" if mac else "Not found.")
            except ValueError:
                print("Error: Invalid IPv4 address format.")
                
        elif mode == "rarp":
            mac = input("Enter MAC Address: ").strip()
            ip = lookup_mac(mac)
            if ip:
                print(f"RARP Reply: {ip}")
            elif ip is False: # Handled bad regex format already
                continue
            else:
                print("Not found.")

if __name__ == "__main__":
    main()
