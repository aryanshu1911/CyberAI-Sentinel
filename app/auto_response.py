import platform
import subprocess

def block_ip(ip: str):
    """
    Blocks the given IP address.
    Works on Linux using iptables. On Windows, prints a message.
    """
    system = platform.system()
    if system == "Linux":
        try:
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
            print(f"🛑 IP blocked: {ip}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to block IP: {ip}")
    else:
        # Simulate blocking on Windows
        print(f"🛑 [SIMULATION] IP blocked: {ip}")