#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

  Tries to automate the OSCP report writing from CherryTree data.

"""
__author__ = 'kall.micke@gmail.com'

import time
import os
import re

from shutil import copyfile

try:
    from librecon.configuration import *
    from librecon.utils import *
except:
    from configuration import *
    from utils import *


class OSCP:

    report_template = '''

![logo](img/logo.jpg)
<font size='6px'><b>Offensive Security Penetration Test Report for Internal Lab and Exam</b></font>
<hr/>

<font size='3px'> ||REPORT_USER_EMAIL|| </font><br/>
<font size='3px'>OSID: ||REPORT_USER_OSID|| </font><br/>

<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

![logo](img/offensive.jpg)

---


![logo](img/logo.jpg)

<div style='float:left'><font color='blue' size='6px'><b>Table of Contents</b></font></div><br/><br/>
<div style='float:left'><font size='6px'><b>1.0 Offensive-Security Lab and Exam Peneteration Test Report</b></font></div><div style='float:right'><font size='3px'><b>1</b></font></div><br/><br/>
<div style='float:left'>&nbsp;&nbsp;<font size='2px'>1.1 Introduction</font></div><div style='float:right'><font size='3px'>2</font></div><br/><br/>
<div style='float:left'>&nbsp;&nbsp;<font size='2px'>1.2 Objectives</font></div><div style='float:right'><font size='3px'>2</font></div><br/><br/>
<div style='float:left'>&nbsp;&nbsp;<font size='2px'>1.3 Requirements</font></div><div style='float:right'><font size='3px'>2</font></div><br/><br/>

<div style='float:left'><font size='6px'><b>2.0 High-Level Summary</b></font></div><div style='float:right'><font size='3px'><b>3</b></font></div><br/><br/>
<div style='float:left'>&nbsp;&nbsp;<font size='2px'>2.1 Sample Report - Recommendations</font></div><div style='float:right'><font size='3px'>3</font></div><br/><br/>


<div style='float:left'><font size='6px'><b>3.0 Methodologies</b></font></div><div style='float:right'><font size='3px'><b>3</b></font></div><br/><br/>
<div style='float:left'>&nbsp;&nbsp;<font size='2px'>3.1 Information Gathering</font></div><div style='float:right'><font size='3px'>6</font></div><br/><br/>
<div style='float:left'>&nbsp;&nbsp;<font size='2px'>3.2 Penetration</font></div><div style='float:right'><font size='3px'>12</font></div><br/><br/>
<div style='float:left'>&nbsp;&nbsp;<font size='2px'>3.4 Maintaining Access</font></div><div style='float:right'><font size='3px'>13</font></div><br/><br/>
<div style='float:left'>&nbsp;&nbsp;<font size='2px'>3.5 House Cleaning</font></div><div style='float:right'><font size='3px'>15</font></div><br/><br/>

<div style='float:left'><font size='6px'><b>4.0 Additional Items</b></font></div><div style='float:right'><font size='3px'><b>28</b></font></div><br/><br/>

<br/><br/>
<br/><br/>
<br/><br/>

![logo](img/logo.jpg)

<font color='blue' size='6px'><b>1.0 Offensive-Security Lab and Exam Penetration Test Report</b></font></div><br/><br/>

<font color='blue' size='6px'><b>1.1 Introduction</b></font>

The Offensive Security Lab and Exam penetration test report contains all efforts that were conducted in order to pass the Offensive Security course. This report
should contain all lab data in the report template format as well as all items that were used to pass the overall exam. This report will be graded from a standpoint
of correctness and fullness to all aspects of the lab and exam. The purpose of this report is to ensure that the student has a full understanding of penetration
testing methodologies as well as the technical knowledge to pass the qualifications for the Offensive Security Certified Professional.

<font color='blue' size='6px'><b>1.2 Objective</b></font>

The objective of this assessment is to perform an internal penetration test against the Offensive Security Lab and Exam network. The student is tasked with following methodical 
approach in obtaining access to the objective goals. This test should simulate an actual penetration test and how you would start from beginning to end, including the overall report. 
An example page has already been created for you at the latter portions of this document that should give you ample information on what is expected to pass this course. Use the sample report as a guideline to get you through the reporting.

<font color='blue' size='6px'><b>1.3 Requirements</b></font>

The student will be required to fill out this penetration testing report and include the following sections: <br/>
 
  <li> Overall High-Level Summary and Recommendations (non-technical)</li>
  <li> Methodology walkthrough and detailed outline of steps taken</li>
  <li> Each finding with included screenshots, walkthrough, sample code, and proof.txt if applicable.</li>
  <li> Any additional items that were not included</li>


<br/><br/>
<br/><br/>
<br/><br/>

![cat](img/logo.jpg)

<font color='blue' size='6px'><b>2.0 High Level Summary</b></font></div><br/><br/>

I was tasked with performing an internal penetration test towards Offensive Security Exam. An internal penetration test is a dedicated attack against internally connected systems. 
The focus of this test is to perform attacks, similar to those of a hacker and attempt to infiltrate Offensive Security’s internal exam systems – the THINC.local domain. 
My overall objective was to evaluate the network, identify systems, and exploit flaws while reporting the findings back to Offensive Security.<br/>

When performing the internal penetration test, there were several alarming vulnerabilities that were identified on Offensive Security’s network. 
When performing the attacks, I was able to gain access to multiple machines, primarily due to outdated patches and poor security configurations.  
During the testing, I had administrative level access to multiple systems. All systems were successfully exploited and access granted. 
These systems as well as a brief description on how access was obtained are listed below:

<li>192.168.xx.xx (hostname) - Name of initial exploit</li>
<li>192.168.xx.xx (hostname) - Name of initial exploit</li>
<li>192.168.xx.xx (hostname) - Name of initial exploit</li>
<li>192.168.xx.xx (hostname) - Name of initial exploit</li>
<li>192.168.xx.xx (hostname) - BOF</li>


![cat](img/logo.jpg)

<font color='blue' size='6px'><b>2.1 Recommendations</b></font></div><br/><br/>

I recommend patching the vulnerabilities identified during the testing to ensure that an attacker cannot exploit these systems in the future. One thing to remember is that these systems require frequent 
patching and once patched, should remain on a regular patch program to protect additional vulnerabilities that are discovered at a later date.

<br/><br/>
<br/><br/>
<br/><br/>

![logo](img/logo.jpg)

<font color='blue' size='6px'><b>3.0 Methodologies</b></font></div><br/><br/>

I utilized a widely adopted approach to performing penetration testing that is effective in testing how well the Offensive Security Exam environments is secured. 
Below is a breakout of how I was able to identify and exploit the variety of systems and includes all individual vulnerabilities found.

<font color='blue' size='6px'><b>3.1 Information Gathering</b></font></div><br/><br/>

The information gathering portion of a penetration test focuses on identifying the scope of the penetration test. During this penetration test, 
I was tasked with exploiting the exam network. The specific IP addresses were:

<font color='blue' size='6px'><b>Lab Network</b></font>

<li>10.11.1.1</li>
<li>10.11.1.2</li>
<li>10.11.1.3</li>
<li>10.11.1.4</li>

<font color='blue' size='6px'><b>Exam Network</b></font>

<li>192.168.xx.xx</li>
<li>192.168.xx.xx</li>
<li>192.168.xx.xx</li>
<li>192.168.xx.xx</li>
<li>192.168.xx.xx</li>


![cat](img/logo.jpg)

<font color='blue' size='6px'><b>3.2 Penetration</b></font></div><br/><br/>

The penetration testing portions of the assessment focus heavily on gaining access to a variety of systems. During this penetration test, I was able to successfully gain access to X out of the X systems.

<br/>

<font color='blue' size='6px'><b>System IP: 192.168.xx.xxx</b></font>

<b>Service Enumeration</b>

The service enumeration portion of a penetration test focuses on gathering information about what services are alive on a system or systems. This is valuable for an attacker as it provides detailed information on potential attack vectors into a system. 
Understanding what applications are running on the system gives an attacker needed information before performing the actual penetration test.  In some cases, some ports may not be listed.

<table style="width:100%">
  <tr>
    <th bgcolor="#5D7B9D"><font color="#fff">Server IP Address</th>
    <th bgcolor="#5D7B9D"><font color="#fff">Ports Open</th>
  </tr>
  <tr>
    <td>192.169.xx.xxx</td>
    <td>TCP: 21</td>
    <td>UDP: 21</td>
  </tr>
</table>

<b>Nmap Scan Results:</b>

<b>Initial Shell Vulnerability Exploited</b>

<b>Additional info about where the initial shell was acquired from</b>

<b>Vulnerability Explanation:</b> 

<b>Vulnerability Fix:</b>

<b>Severity:</b>

<b>Proof of Concept Code Here:</b>
 
<b>Local.txt Proof Screenshot:</b>


<b>Privilege Escalation</b>

<b>Additional Priv Esc info</b>

<b>Vulnerability Exploited:</b>

<b>Vulnerability Explanation: </b>

<b>Vulnerability Fix:</b> 

<b> Exploit Code:</b>
<b> Proof Screenshot Here: </b>
<b> Proof.txt Contents: </b>

<br/><br/>
<br/><br/>
<br/><br/>

![cat](img/logo.jpg)

<font color='blue' size='6px'><b>3.4 Maintaining Access</b></font></div><br/><br/>

Maintaining access to a system is important to us as attackers, ensuring that we can get back into a system after it has been exploited is invaluable. The maintaining access phase of the penetration test focuses on ensuring that once the focused attack has occurred (i.e. a buffer overflow), 
we have administrative access over the system again. Many exploits may only be exploitable once and we may never be able to get back into a system after we have already performed the exploit. 


<font color='blue' size='6px'><b>3.5 House Cleaning</b></font></div><br/><br/>
The house cleaning portions of the assessment ensures that remnants of the penetration test are removed. Often fragments of tools or user accounts are left on an organization's computer which can cause security issues down the road. Ensuring that we are meticulous and no remnants of our penetration test are left over is important.

After collecting trophies from the exam network was completed, the student removed all user accounts and passwords as well as the Meterpreter services installed on the system. Offensive Security should not have to remove any user accounts or services from the system.

<font color='blue' size='6px'><b>4.0 Additional Items</b></font></div><br/><br/>

<b>Appendix 1 - Proof and Local Contents:</b>

<table style="width:100%">
  <tr>
    <th bgcolor="#5D7B9D"><font color="#fff">IP (Hostname)</th>
    <th bgcolor="#5D7B9D"><font color="#fff">Local.txt Contents</th>
    <th bgcolor="#5D7B9D"><font color="#fff">Proof.txt Contents</th>
  </tr>
  <tr>
    <td>192.168.xx.xx</td>
    <td>Local.txt</td>
    <td>Proof.txt</td>
  </tr>
</table>

<b>Appendix 2 - Metasploit/Meterpreter Usage</b>

 For the exam, I used my Metasploit/Meterpreter allowance on the following machine:
    <li> 192.168.XX.XX</li>


<b>Appendix 3 - Completed Buffer Overflow Code</b>

'''

    def __init__(self):

        if os.path.isfile('/usr/bin/md2pdf') is False:
            utils.puts('info', 'md2pdf is not installed')
            os._exit(0)

        # Load configuration
        self.cfg = Configuration()
        self.report_file = '%s/report/report.md' % self.cfg.config_dir

    def generate_report(self):

        home = str(Path.home())

        self.report_dir = '%s/.massrecon/report' % home

        if os.path.isdir(self.report_dir) is False:
            os.makedirs(self.report_dir, exist_ok=True)

        if os.path.isdir(self.report_dir + '/img') is False:
            os.makedirs(self.report_dir + '/img', exist_ok=True)

        if os.path.isfile(self.report_dir + '/img/logo.jpg') is False:
            copyfile('oscp/img/logo.jpg', self.report_dir + '/img/logo.jpg')

        if os.path.isfile(self.report_dir + '/img/offensive.jpg') is False:
            copyfile('oscp/img/offensive.jpg', self.report_dir + '/img/offensive.jpg')

        if os.path.isfile(self.report_dir + '/style.css') is False:
            copyfile('oscp/style.css', self.report_dir + '/style.css')

        report_user_email = self.cfg.config.get('oscp', 'report_user_email')
        report_user_osid = self.cfg.config.get('oscp', 'report_user_osid')

        self.report_template = self.report_template.replace('||REPORT_USER_EMAIL||', report_user_email.strip())
        self.report_template = self.report_template.replace('||REPORT_USER_OSID||', report_user_osid.strip())

        with open(self.report_file, 'w') as template:
            template.write(self.report_template)

        cwd = os.getcwd()
        os.chdir(self.report_dir)

        # Generate pdf
        utils.puts('info', 'Generating: %s/report.pdf' % self.report_dir)
        os.system("/usr/bin/md2pdf --css %s/style.css %s/report.md %s/report.pdf" % (self.report_dir, self.report_dir, self.report_dir))
        os.chdir(cwd)

if __name__ == '__main__':
    pass

