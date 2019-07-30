# udpy
UDP Script written in Python to initialize a DDoS attack.
This is for educational purposes only.

Usage: `python ud.py <ip> -p <port> -t <time> -s <size>`  
- Only the IP is required.  
- If no port is specified, it will send packets on random ports.  
- If no time is specified, it will take forever. The time is in seconds.  
- Size defaults to 1024 bytes. The maximum value is 65530.
