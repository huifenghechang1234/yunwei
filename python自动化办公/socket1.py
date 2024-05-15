"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/22'
code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""
"""
端口扫描程序

这个自动化脚本会将网站 URL 作为输入，并检查该网站是否存在任何开放端口。无论你是作为 "红队 "的一员在执行任务，
还是在 "蓝队 "中坚守阵地，这个脚本都能为你提供有用的便利工具
"""

import socket
from prettytable import PrettyTable

# Dictionary mapping common ports to vulnerabilities (Top 15)
vulnerabilities = {
    80: "HTTP (Hypertext Transfer Protocol) - Used for unencrypted web traffic",
    443: "HTTPS (HTTP Secure) - Used for encrypted web traffic",
    22: "SSH (Secure Shell) - Used for secure remote access",
    21: "FTP (File Transfer Protocol) - Used for file transfers",
    25: "SMTP (Simple Mail Transfer Protocol) - Used for email transmission",
    23: "Telnet - Used for remote terminal access",
    53: "DNS (Domain Name System) - Used for domain name resolution",
    110: "POP3 (Post Office Protocol version 3) - Used for email retrieval",
    143: "IMAP (Internet Message Access Protocol) - Used for email retrieval",
    3306: "MySQL - Used for MySQL database access",
    3389: "RDP (Remote Desktop Protocol) - Used for remote desktop connections (Windows)",
    8080: "HTTP Alternate - Commonly used as a secondary HTTP port",
    8000: "HTTP Alternate - Commonly used as a secondary HTTP port",
    8443: "HTTPS Alternate - Commonly used as a secondary HTTPS port",
    5900: "VNC (Virtual Network Computing) - Used for remote desktop access",
    # Add more ports and vulnerabilities as needed
}

def display_table(open_ports):
    table = PrettyTable(["Open Port", "Vulnerability"])
    for port in open_ports:
        vulnerability = vulnerabilities.get(port, "No known vulnerabilities associated with common services")
        table.add_row([port, vulnerability])
    print(table)

def scan_top_ports(target):
    open_ports = []
    top_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 5900, 8000, 8080, 8443]  # Top 15 ports
    for port in top_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Adjust timeout as needed
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            sys.exit()
        except socket.error:
            pass
    return open_ports

def main():
    target = input("Enter the website URL or IP address to scan for open ports: ")
    open_ports = scan_top_ports(target)
    if not open_ports:
        print("No open ports found on the target.")
    else:
        print("Open ports and associated vulnerabilities:")
        display_table(open_ports)

if __name__ == "__main__":
    main()

