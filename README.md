<div align="center">

#  Proxy Tool

### *Advanced Proxy Checker & Scraper*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat&logo=python)](https://www.python.org)
[![Async](https://img.shields.io/badge/Async-aiohttp-cyan.svg?style=flat)](https://docs.aiohttp.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](LICENSE)
[![Rich](https://img.shields.io/badge/UI-Rich-magenta.svg?style=flat)](https://rich.readthedocs.io)

Modern proxy collection and validation tool with beautiful CLI interface



---

</div>

##  Features

<table>
<tr>
<td>

-  **Beautiful Interface**
-  **Async Checking**
-  **4 Protocols** - SOCKS5, SOCKS4, HTTP, HTTPS
-  **Live Statistics**

</td>
<td>

-  **Organized Output**
-  **Auto Detection**
-  **Configurable**
-  **Auto Save**

</td>
</tr>
</table>

---

##  Installation

### Prerequisites

The current version of the software is developed and tested using Python 3.14.2.

---

###  Quick Setup

```bash
# Clone or Download the Repository

git clone https://github.com/kranoley/Proxy-Scraper-Parser-And-Checker.git

cd Proxy-Scraper-Parser-And-Checker

pip install -r requirements.txt

python main.py
```


---


## ⚙️ Configuration

### The program-settings.config file

The behaviour of the program is controlled from a single file named "program-settings.config". 

To add custom sources simply paste them using your favourite text editor into their respective sections. The export path, and other program settings can also be configured here.

If you want to comment out a line, simply inset a hashtag at the start of the line.

You don't need sources for every proxy type, but naturally, at least one should have an entry.

Increasing "Concurrent Checks" will improve the speed of the program, at the cost of higher CPU utilisation. The default value of 1000 is a sensible, but if you have a more (or less) powerful system you might want to change it.

### Example program-settings.config

```
[socks5]
https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/socks5_proxies.txt

[socks4]
https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/socks4_proxies.txt

[http]
https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/http_proxies.txt

[https]
https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/https/data.txt

[test-urls]
http://httpbin.org/ip

[export-path]
# Leave as 'proxies' to export files to the same directory the program runs from.
proxies

[options]
Timeout: 5
Fetch Timeout: 5
Concurrent Checks: 1000
```





##  UI Preview

<div align="center">
<img width="1105" height="383" alt="mg1" src="https://github.com/user-attachments/assets/0ef8077f-263a-4f45-90fc-3051fc40cf96" />
<img width="1136" height="239" alt="mg2" src="https://github.com/user-attachments/assets/ef7c327b-6c4a-4f71-b607-636105220dd0" />
<img width="1308" height="138" alt="mg3" src="https://github.com/user-attachments/assets/a55d8a2f-ec73-4960-8774-4e05f340ba4d" />



</div>
