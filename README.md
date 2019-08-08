# massrecon.py

[![Python 3.2|3.6](https://img.shields.io/badge/python-3.2|3.6-green.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPL3-_red.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![Build Status](https://travis-ci.org/mikaelkall/massrecon.svg?branch=master)](https://travis-ci.org/mikaelkall/massrecon) [![Twitter](https://img.shields.io/badge/twitter-@massrecon-blue.svg)](https://twitter.com/MickeKall)


<p align="center">
   <img src="https://i.imgur.com/sClMjCk.jpg" alt="massrecon logo" width="900" height="400" />
</p>


## Summary

A reconnaissance tool made for the OSCP engagements to automate information gathering and service enumeration whilst creating a directory structure to store  results, findings and exploits used for each host, recommended commands to execute and directory structures for storing loot and flags.
Also document the information in CherryTree so you can focus on the exploitation instead of reconnaissance.

## Install

Install package and you will have /usr/bin/massrecon.py ready for usage.

```sh
sudo python3 setup.py install
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

## Example

[![asciicast](https://asciinema.org/a/NHxrjuT5jkIe4ukqfixyIzFix.svg)](https://asciinema.org/a/NHxrjuT5jkIe4ukqfixyIzFix)

## Cherrytree

For view in Cherrytree. Database file can be found in this location.

**~/.massrecon/massrecon.ctd**

![](https://i.imgur.com/6R3npOW.png)
