#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  CherryTree class
"""
__author__ = 'kall.micke@gmail.com'

import time
import os
import re

try:
    from librecon.configuration import *
    from librecon.utils import *
except:
    from configuration import *
    from utils import *


class CherryTree:

    '''
    A bit ugly implementation compared to use sqlite3. However this simplified templating a lot so I use this method for now.
    '''

    database_template = '''<node custom_icon_id="10" foreground="" is_bold="True" name="<<<XX.XX.XX.XX>>>" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1496953072.48" unique_id="2">
		<rich_text>
			
		</rich_text>
		<node custom_icon_id="21" foreground="" is_bold="False" name="Enumeration" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1492949452.72" unique_id="17">
			<rich_text>
				
			</rich_text>
			<node custom_icon_id="18" foreground="" is_bold="False" name="TCP" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1492949819.41" ts_lastsave="1500473593.05" unique_id="26">
				<rich_text>
					
				</rich_text>
			</node>
			<node custom_icon_id="18" foreground="" is_bold="False" name="UDP" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1492949826.2" ts_lastsave="1500473597.2" unique_id="27">
				<rich_text>
					
				</rich_text>
			</node>
			<node custom_icon_id="17" foreground="" is_bold="False" name="Web Services" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1492949605.23" unique_id="18">
				<rich_text>
					
				</rich_text>
				<node custom_icon_id="18" foreground="" is_bold="False" name="Nikto" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1492949545.74" ts_lastsave="1492949578.65" unique_id="24">
					<rich_text>
						
					</rich_text>
				</node>
				<node custom_icon_id="18" foreground="" is_bold="False" name="GoBuster" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1492949554.24" ts_lastsave="1500473690.91" unique_id="25">
					<rich_text>
						
					</rich_text>
				</node>
				<node custom_icon_id="18" foreground="" is_bold="False" name="WebDav" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1500473692.93" ts_lastsave="1500473698.92" unique_id="33">
					<rich_text>
						
					</rich_text>
				</node>
				<node custom_icon_id="18" foreground="" is_bold="False" name="CMS" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1500473700.65" ts_lastsave="1500473703.84" unique_id="34">
					<rich_text>
						
					</rich_text>
				</node>
				<node custom_icon_id="18" foreground="" is_bold="False" name="SSLYZE" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1500473700.65" ts_lastsave="1500473703.84" unique_id="35">
					<rich_text>
						
					</rich_text>
				</node>				
			</node>
			<node custom_icon_id="44" foreground="" is_bold="False" name="Other Services" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1500473607.17" unique_id="20">
				<rich_text>
					
				</rich_text>
				<node custom_icon_id="0" foreground="" is_bold="False" name="SMB" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1500473455.56" ts_lastsave="1500473619.73" unique_id="21">
					<rich_text>
						
					</rich_text>
				</node>
				<node custom_icon_id="0" foreground="" is_bold="False" name="SNMP" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1500473619.73" ts_lastsave="1500473631.55" unique_id="29">
					<rich_text>
						
					</rich_text>
				</node>
				<node custom_icon_id="0" foreground="" is_bold="False" name="DB" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1500473622.74" ts_lastsave="1500473677.59" unique_id="31">
					<rich_text>
						
					</rich_text>
				</node>
				<node custom_icon_id="0" foreground="" is_bold="False" name="Other" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1500473623.25" ts_lastsave="1500473681.55" unique_id="32">
					<rich_text>
						
					</rich_text>
				</node>
			</node>
		</node>
		<node custom_icon_id="22" foreground="" is_bold="False" name="Exploitation" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1500474629.1" unique_id="22">
			<rich_text weight="heavy">
Service Exploited:  
Vulnerability Type:
Exploit POC:
</rich_text>
<rich_text>


</rich_text>
<rich_text weight="heavy">
Description
</rich_text>
<rich_text>





</rich_text>
<rich_text underline="single" weight="heavy">
Discovery of Vulnerability
</rich_text>
<rich_text>








</rich_text>
<rich_text underline="single" weight="heavy">
Exploit Code Used
</rich_text>
<rich_text>









</rich_text>
<rich_text underline="single" weight="heavy">
Proof\Local.txt File
</rich_text>
<rich_text>


   ☐ Screenshot with ifconfig\ipconfig
   ☐ Submit too OSCP Exam Panel







			</rich_text>
		</node>
		<node custom_icon_id="21" foreground="" is_bold="False" name="Post Exploitation" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1495714301.41" unique_id="7">
			<rich_text>
				
			</rich_text>
			<node custom_icon_id="44" foreground="" is_bold="False" name="Script Results" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1495714301.41" ts_lastsave="1495714310.34" unique_id="4">
				<rich_text>
					
				</rich_text>
			</node>
			<node custom_icon_id="18" foreground="" is_bold="False" name="Host Information" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1500474204.83" unique_id="15">
<rich_text underline="single" weight="heavy">
Operating System
</rich_text>
<rich_text>




</rich_text>
<rich_text underline="single" weight="heavy">
Architecture
</rich_text>
<rich_text>





</rich_text>
<rich_text underline="single" weight="heavy">
Domain
</rich_text>
<rich_text>




</rich_text>
<rich_text underline="single" weight="heavy">
Installed Updates
</rich_text>
<rich_text>


</rich_text>
			</node>
			<node custom_icon_id="18" foreground="" is_bold="False" name="File System" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1500474208.8" unique_id="14">
<rich_text underline="single" weight="heavy">
Writeable Files\Directories
</rich_text>
<rich_text>





</rich_text>
<rich_text underline="single" weight="heavy">
Directory List
</rich_text>
<rich_text>






				</rich_text>
			</node>
			<node custom_icon_id="18" foreground="" is_bold="False" name="Running Processes" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1495714268.27" unique_id="8">
<rich_text underline="single" weight="heavy">
Process List
</rich_text>
			</node>
			<node custom_icon_id="18" foreground="" is_bold="False" name="Installed Applications" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1495714509.19" unique_id="10">
<rich_text underline="single" weight="heavy">
Installed Applications
</rich_text>
			</node>
			<node custom_icon_id="18" foreground="" is_bold="False" name="Users &amp; Groups" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1500474213.69" unique_id="11">
<rich_text underline="single" weight="heavy">
Users
</rich_text>
<rich_text>





</rich_text>
<rich_text underline="single" weight="heavy">
Groups
</rich_text>
</node>
<node custom_icon_id="18" foreground="" is_bold="False" name="Network" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1500474223.91" unique_id="13">
<rich_text underline="single" weight="heavy">
IPConfig\IFConfig

</rich_text>
<rich_text>





</rich_text>
<rich_text>
Network Processes
</rich_text>
<rich_text>





</rich_text>
<rich_text underline="single" weight="heavy">
ARP
</rich_text>
<rich_text>





</rich_text>
<rich_text underline="single" weight="heavy">
DNS
</rich_text>
<rich_text>






</rich_text>
<rich_text underline="single" weight="heavy">
Route
</rich_text>
</node>
<node custom_icon_id="18" foreground="" is_bold="False" name="Scheduled Jobs" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1496953428.46" unique_id="16">
<rich_text underline="single" weight="heavy">
Scheduled Tasks
</rich_text>
</node>
</node>
<node custom_icon_id="10" foreground="" is_bold="False" name="Priv Escalation" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1500474606.33" unique_id="12">
<rich_text weight="heavy">
Service Exploited:  
Vulnerability Type:
Exploit POC:
</rich_text>
<rich_text>

</rich_text>
<rich_text weight="heavy">
Description
</rich_text>
<rich_text>



</rich_text>
<rich_text underline="single" weight="heavy">
Discovery of Vulnerability
</rich_text>
<rich_text>








</rich_text>
<rich_text underline="single" weight="heavy">
Exploit Code Used
</rich_text>
<rich_text>








</rich_text>
<rich_text underline="single" weight="heavy">
Proof\Local.txt File
</rich_text>
<rich_text>

   ☐ Screenshot with ifconfig\ipconfig
   ☐ Submit too OSCP Exam Panel


</rich_text>
		</node>
		<node custom_icon_id="43" foreground="" is_bold="False" name="Goodies" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1492949508.15" unique_id="3">
			<rich_text>
				
			</rich_text>
			<node custom_icon_id="18" foreground="" is_bold="False" name="Hashes" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1492949998.88" unique_id="9">
				<rich_text>
					
				</rich_text>
			</node>
			<node custom_icon_id="18" foreground="" is_bold="False" name="Passwords" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1492950150.97" unique_id="5">
				<rich_text>
					
				</rich_text>
			</node>
			<node custom_icon_id="18" foreground="" is_bold="False" name="Proof\Flags\Other" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1496953479.65" unique_id="6">
				<rich_text>
					
				</rich_text>
			</node>
		</node>
		<node custom_icon_id="12" foreground="" is_bold="False" name="Software Versions" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1496953122.23" unique_id="19">
<rich_text underline="single" weight="heavy">
Software Versions

</rich_text>
<rich_text>







</rich_text>
<rich_text underline="single" weight="heavy">
Potential Exploits
</rich_text>
</node>
<node custom_icon_id="13" foreground="" is_bold="True" name="Methodology" prog_lang="custom-colors" readonly="False" tags="" ts_creation="1496953072.48" ts_lastsave="1500474082.49" unique_id="28">
<rich_text underline="single" weight="heavy">
Network Scanning
</rich_text>
<rich_text>


   ☐  nmap -sn 10.11.1.*
   ☐  nmap -sL 10.11.1.*
   ☐  nbtscan -r 10.11.1.0/24
 
   
</rich_text>
<rich_text link="node 47">
smbtree
</rich_text>
<rich_text>



</rich_text>
<rich_text underline="single" weight="heavy">
Individual Host Scanning
</rich_text>
<rich_text>


   ☐  nmap  --top-ports 20 --open -iL iplist.txt
   ☐  nmap -sS -A -sV -O -p- ipaddress
   ☐  nmap -sU ipaddress


</rich_text>
<rich_text underline="single" weight="heavy">
Service Scanning
</rich_text>
<rich_text>


    
</rich_text>
<rich_text weight="heavy">
WebApp
</rich_text>

<rich_text>

      ☐	  Nikto
	  ☐	  wpscan
      ☐   dirbuster
      ☐   dotdotpwn
      ☐   view source 
      ☐   davtest\cadevar
      ☐   droopscan
      ☐   joomscan
      ☐   LFI\RFI Test
      
    
</rich_text>
<rich_text weight="heavy">
Linux\Windows
</rich_text>
<rich_text>
      ☐   snmpwalk -c public -v1 
</rich_text>
<rich_text style="italic">
ipaddress
</rich_text>
<rich_text>

      ☐   smbclient -L //ipaddress
      ☐   showmount -e ipaddress port
      ☐   rpcinfo
      ☐   Enum4Linux
    
    
</rich_text>
<rich_text weight="heavy">
Anything Else
</rich_text>
<rich_text>

	  ☐	  hydra
	  ☐	  nmap scripts
	  ☐	  (locate *nse* | grep servicename)
	  ☐	  hydra
      ☐   MSF Aux Modules
      ☐   Download the softward

</rich_text>
<rich_text underline="single" weight="heavy">
Exploitation
</rich_text>
<rich_text>

   ☐   Gather Version Numbes
   ☐   Searchsploit
   ☐   Default Creds
   ☐   Creds Previously Gathered
   ☐   Download the software


</rich_text>
<rich_text underline="single" weight="heavy">
Post Exploitation
</rich_text>
<rich_text>


    
</rich_text>
<rich_text weight="heavy">
Linux
</rich_text>
<rich_text>

      ☐   linux-local-enum.sh
      ☐   linuxprivchecker.py
      ☐   linux-exploit-suggestor.sh
      ☐   unix-privesc-check.py

   
</rich_text>
<rich_text weight="heavy">
Windows
</rich_text>
<rich_text>

      ☐   wpc.exe
      ☐   windows-exploit-suggestor.py
         
</rich_text>
<rich_text link="webs https://github.com/pentestmonkey/windows-privesc-check/blob/master/windows_privesc_check.py">
      ☐   windows_privesc_check.py
</rich_text>
<rich_text>
      ☐  	windows-privesc-check2.exe
</rich_text>
<rich_text underline="single" weight="heavy">
      ☐     Priv Escalation
</rich_text>
<rich_text>

   
</rich_text>
<rich_text link="node 36">
acesss internal services (portfwd)
</rich_text>
<rich_text>

   ☐  add account


</rich_text>
<rich_text weight="heavy">
Windows
</rich_text>
<rich_text>

   ☐  List of exploits


</rich_text>
<rich_text weight="heavy">
Linux
</rich_text>
<rich_text>

   ☐  sudo su 
   ☐  KernelDB
   ☐  Searchsploit


</rich_text>
<rich_text underline="single" weight="heavy">
Final
</rich_text>
<rich_text>

   ☐  Screenshot of IPConfig\WhoamI
   ☐  Copy proof.txt
   ☐  Dump hashes 
   ☐  Dump SSH Keys
   ☐  Delete files
   
</rich_text>
</node>
<node custom_icon_id="20" foreground="" is_bold="True" name="Log Book" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1495714168.37" unique_id="1">
<rich_text>

</rich_text>
</node>
</node>
'''

    def __init__(self, address=''):

        if len(address) == 0:
            return

        self.address = address
        self.database_data = ''

        # Load configuration
        cfg = Configuration()

        if cfg.config.get('massrecon', 'cherrytree_log') != 'True':
            utils.puts('info', 'CherryTree module is disabled')
            return

        self.db_file = '%s/massrecon.ctd' % cfg.config_dir

        if os.path.exists(self.db_file) is False:
            utils.puts('info', 'CherryTree database not found. Created it.')
            self.setup_database()

        # Append host to database.
        self.add_address()

    def setup_database(self):

        with open(self.db_file, 'w') as file:
            file.write('<?xml version="1.0" ?>\n<cherrytree>')
            file.write(self.database_template.replace('<<<XX.XX.XX.XX>>>', self.address))
            file.write('</cherrytree>')


    def check_if_address_exists(self):

        with open(self.db_file, 'r') as file:
            for row in file.read().split('\n'):

                rgxp = re.compile('.*<node custom_icon_id="10" foreground="" is_bold="True" name="%s" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1496953072.48" unique_id="\d+">.*' % self.address)
                if len(rgxp.findall(row)) == 1:
                    return True

        return False


    def add_address(self):

        if self.check_if_address_exists() is False:

            with open(self.db_file, 'r') as file:
                for row in file.read().split('\n'):

                    if '</cherrytree>' in row:

                        self.database_data += self.database_template.replace('<<<XX.XX.XX.XX>>>', self.address)
                        self.database_data += '</cherrytree>\n'
                        break

                    self.database_data += row + '\n'

            with open(self.db_file, 'w') as file:
                file.write(self.database_data)


    def append_data(self, node_name, message):

        # Cleanup message
        message = message.replace('<', '&lt;')
        message = message.replace('>', '&gt;')
        message = message.replace('"', '&quot;')
        message = message.replace("'", '&apos;')
        message = message.replace("&", '&amp;')

        node_found = False
        append_found = False
        self.database_data = ''
        with open(self.db_file, 'r') as file:
            for row in file.read().split('\n'):

                if node_found is False:
                    rgxp = re.compile('.*<node custom_icon_id="10" foreground="" is_bold="True" name="%s" prog_lang="custom-colors" readonly="False" tags="" ts_creation="0.0" ts_lastsave="1496953072.48" unique_id="\d+">.*' % self.address)
                    if len(rgxp.findall(row)) == 1:
                        node_found = True

                if node_found is True:
                    regexp = '''.*<node custom_icon_id="18" foreground="" is_bold="False" name="%s" prog_lang="custom-colors" readonly="False" tags="" ts_creation="[0-9.]+" ts_lastsave="[0-9.]+" unique_id="\d+">.*''' % node_name
                    rgxp = re.compile(regexp)

                    if len(rgxp.findall(row)) == 1:
                        append_found = True
                    else:
                        if append_found is True:
                            if '<rich_text>' in row:
                                pass

                            if '</rich_text>' in row:
                                self.database_data += '%s' % message + "\n</rich_text>\n"
                                append_found = False
                                continue

                self.database_data += row + '\n'

        with open(self.db_file, 'w') as file:
            file.write(self.database_data)

if __name__ == '__main__':
    pass

