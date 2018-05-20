# massrecon.py

This is still in develop it will be in develop branch until I have a ready release. 

## Summary

This is reconissance tool specific written for OSCP engagements.
For boot2root, hackthebox.eu or OSCP in general I start mostly with the same reconissance
procedure and document it in KeepNote or CherryTree. The intention with this tool
is to automate this procedure by start all reconissance tools and enumeration
and automaticly import the results to CherryTree so you can focus on exploitation instead
of look for the weakest link.

## Install

Install package and you will have /usr/bin/massrecon.py ready for usage.

```sh
sudo python setup.py install
```

## Prerequisites

For development you need to install these dependencies. Do this or use virtualenv

```sh
sudo pip install -r requirements.txt
Requirement already satisfied: halo==0.0.12 in /usr/lib/python3.6/site-packages (from -r requirements.txt (line 1)) (0.0.12)
Requirement already satisfied: configparser==3.5.0 in /usr/lib/python3.6/site-packages (from -r requirements.txt (line 2)) (3.5.0)
Requirement already satisfied: backports.shutil_get_terminal_size==1.0.0 in /usr/lib/python3.6/site-packages (from halo==0.0.12->-r requirements.txt (line 1)) (1.0.0)
Requirement already satisfied: log_symbols==0.0.11 in /usr/lib/python3.6/site-packages (from halo==0.0.12->-r requirements.txt (line 1)) (0.0.11)
Requirement already satisfied: spinners==0.0.19 in /usr/lib/python3.6/site-packages (from halo==0.0.12->-r requirements.txt (line 1)) (0.0.19)
Requirement already satisfied: cursor==1.2.0 in /usr/lib/python3.6/site-packages (from halo==0.0.12->-r requirements.txt (line 1)) (1.2.0)
Requirement already satisfied: termcolor==1.1.0 in /usr/lib/python3.6/site-packages (from halo==0.0.12->-r requirements.txt (line 1)) (1.1.0)
Requirement already satisfied: colorama==0.3.9 in /usr/lib/python3.6/site-packages (from halo==0.0.12->-r requirements.txt (line 1)) (0.3.9)
Collecting six==1.11.0 (from halo==0.0.12->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
Requirement already satisfied: enum34==1.1.6 in /usr/lib/python3.6/site-packages (from log_symbols==0.0.11->halo==0.0.12->-r requirements.txt (line 1)) (1.1.6)
zapcli 0.9.0 has requirement six==1.10.0, but you'll have six 1.11.0 which is incompatible.
Installing collected packages: six
  Found existing installation: six 1.10.0
    Uninstalling six-1.10.0:
      Successfully uninstalled six-1.10.0
Successfully installed six-1.11.0
Cache entry deserialization failed, entry ignored
```

## Usage

```sh
███╗   ███╗ █████╗ ███████╗███████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
████╗ ████║██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██╔████╔██║███████║███████╗███████╗██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║╚██╔╝██║██╔══██║╚════██║╚════██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║███████║███████║██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
[nighter@nighter.se] [Scans and updates CherryTree]

Usage: massrecon [OPTIONS]

General Options

   recon <ip>		Start recon target
   nmap  <ip>		Run nmap module only
   dirb  <ip>		Run dirb module only
 ```

## Start scanning

```sh
$ ./massrecon.py recon 10.10.10.88
==========================================================================================
 NMAP_STAGE_1: 10.10.10.88
==========================================================================================
   ✔ 80/tcp open
------------------------------------------------------------------------------------------
⠹ NMAP STAGE[2]

==========================================================================================
 NMAP_STAGE_2: 10.10.10.88
==========================================================================================
Starting Nmap 7.70 ( https://nmap.org ) at 2018-05-20 15:58 CEST
Nmap scan report for 10.10.10.88
Host is up (0.059s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Landing Page

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.09 seconds
------------------------------------------------------------------------------------------


   ✔ http://10.10.10.88/robots.txt
   ➜ Spider: http://10.10.10.88/webservices/tar/tar/source/
   ➜ Spider: http://10.10.10.88/webservices/monstra-3.0.4/
 ```

## Cherrytree

For view Cherrytree results database file can be found in this location.

~/.massrecon/massrecon.ctb
