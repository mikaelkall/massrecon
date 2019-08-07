# massrecon.py

[![Python 3.2|3.6](https://img.shields.io/badge/python-3.2|3.6-green.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPL3-_red.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![Build Status](https://travis-ci.org/mikaelkall/massrecon.svg?branch=master)](https://travis-ci.org/mikaelkall/massrecon) [![Twitter](https://img.shields.io/badge/twitter-@massrecon-blue.svg)](https://twitter.com/MickeKall)

## Summary

A reconnaissance tool made for the OSCP engagements to automate information gathering and service enumeration whilst creating a directory structure to store  results, findings and exploits used for each host, recommended commands to execute and directory structures for storing loot and flags.
Also document the information in CherryTree so you can focus on the exploitation instead of reconnaissance.

## Install

Install package and you will have /usr/bin/massrecon.py ready for usage.

```sh
sudo python3 setup.py install
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
./massrecon.py

███╗   ███╗ █████╗ ███████╗███████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
████╗ ████║██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██╔████╔██║███████║███████╗███████╗██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║╚██╔╝██║██╔══██║╚════██║╚════██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║███████║███████║██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
[Scans and updates CherryTree]

Usage: massrecon [OPTIONS]

General Options

       recon  <ip>      Start recon target

   [Plugins]

        nmap  <ip>      Run nmap module only
        dirb  <ip>      Run dirb module only
       nikto  <ip>      Run nikto module only
         ftp  <ip>      Run ftp module only
      sslyze  <ip>      Run sslyze module only
   quickscan  <ip>      Run quick portscan on all ports.

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

For view in Cherrytree. Database file can be found in this location.

~/.massrecon/massrecon.ctb

![](https://raw.githubusercontent.com/mikaelkall/massrecon/develop/chr.gif)
