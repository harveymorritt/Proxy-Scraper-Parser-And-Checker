from pathlib import Path

PROXY_SOURCES = {
    'socks5': [
        'https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/socks5_proxies.txt',
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks5/data.txt',
        'https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/refs/heads/main/socks5/raw/all.txt',
        'https://raw.githubusercontent.com/databay-labs/free-proxy-list/refs/heads/master/socks5.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Socks5.txt',
        'https://raw.githubusercontent.com/zloi-user/hideip.me/refs/heads/master/socks5.txt',
        'https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/refs/heads/main/socks5.txt',

    ],
    
    'socks4': [
        'https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/socks4_proxies.txt',
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks4/data.txt',
        'https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/refs/heads/main/socks4/raw/all.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Socks4.txt',
        'https://raw.githubusercontent.com/zloi-user/hideip.me/refs/heads/master/socks4.txt',
        'https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/refs/heads/main/socks4.txt',

    ],
    
    'http': [
        'https://raw.githubusercontent.com/dpangestuw/Free-Proxy/refs/heads/main/http_proxies.txt',
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/http/data.txt',
        'https://raw.githubusercontent.com/ClearProxy/checked-proxy-list/refs/heads/main/http/raw/all.txt',
        'https://raw.githubusercontent.com/databay-labs/free-proxy-list/refs/heads/master/http.txt',
        'https://raw.githubusercontent.com/zloi-user/hideip.me/refs/heads/master/http.txt',
        'https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/refs/heads/main/http.txt',

    ],
    
    'https': [
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/https/data.txt',
        'https://raw.githubusercontent.com/databay-labs/free-proxy-list/refs/heads/master/https.txt',
        'https://raw.githubusercontent.com/r00tee/Proxy-List/refs/heads/main/Https.txt',
        'https://raw.githubusercontent.com/zloi-user/hideip.me/refs/heads/master/https.txt',
        'https://raw.githubusercontent.com/vmheaven/VMHeaven-Free-Proxy-Updated/refs/heads/main/https.txt',

    ],
}


TEST_URLS = [
    'http://httpbin.org/ip',
]


TIMEOUT = 5
FETCH_TIMEOUT = 30
CONCURRENT_CHECKS = 1000


OUTPUT_DIR = Path('proxies')
OUTPUT_DIR.mkdir(exist_ok=True)