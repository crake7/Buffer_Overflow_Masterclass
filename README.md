<h1 align="center"> Automating Binary Exploitation</h1>
<h4 align="center">7 folders for the 7 videos that explain how to overflow a buffer corrupting the Saved Return Pointer.</h4>

<p align="center">
  <a href="#Requirements">How to</a> •
  <a href="#Steps">Modules</a> •
  <a href="#Important">Important!</a>
</p>

___

<h5>Do you want to learn how to automate your buffer overflows?</h5>
If yes, this repo is for you! It follows the 7 steps by "The Cyber Mentor" with links to his videos and the modified code I wrote. 

## Requirements

1. A <strong>Windows 10</strong> desktop. Download a virtual machine [here] (https://www.microsoft.com/en-us/software-download/windows10ISO)
2. A vulnerable software: <strong>Vulnserver</strong>. Download from its repo [here] (https://github.com/stephenbradshaw/vulnserver)
3. <strong>Kali Linux</strong> or any other OS you use for offensive work. Download a virtual image [here] (https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/)
4. A debugger: <strong> Immunity Debugger</strong>. Download it [here] (https://debugger.immunityinc.com/ID_register.py) You will need to register in the link, so be creative. 


The scripts were created while taking the "Buffer Overflows Made Easy" Masterclass by "The Cyber Mentor":
video: https://www.youtube.com/watch?v=qSnPayW6F7U&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G or doc: https://tcm-sec.com/buffer-overflows-made-easy/

## Steps

<table>
<thead>
<tr>
<th>Folder Name</th>
<th>Functionality</th>
</tr>
</thead>
<tbody>
<tr>
<td>Spiking</td>
<td>Retrieves a list of folders & files in the target's current directory</td>
</tr>
<tr>
<td>Environment</td>
<td>Retrieves a list of the target's environmental variables. </td>
</tr>
<tr>
<td>Key Logger</td>
<td>Prints out PID, process name, window name and keystrokes of target.</td>
</tr>
<tr>  
<td>Screenshooter</td>
<td>Takes a screenshot of target's desktop. </td>
</tr>
<tr>  
<td>Shellcode</td>
<td>Connects to your remote web server and executes your shellcode directly into the target's memory.</td>
</tr>
</tbody>
</table>

– Spiking: https://www.youtube.com/watch?v=3x2KT4cRP9o&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=2 

– Fuzzing: https://www.youtube.com/watch?v=FCIfWTAtPr0&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=3

– Find_EIP: https://www.youtube.com/watch?v=GqwyonqLYdQ&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=4

– Overwrite_EIP: https://www.youtube.com/watch?v=Wh9wRKBzajo&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=5 

– Bad_chars: https://www.youtube.com/watch?v=uIFYNVqpZ0k&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=6

– Right_Module: https://www.youtube.com/watch?v=k9D9RuFT02I&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=7

– Exploit: https://www.youtube.com/watch?v=qSjxR8tfokg&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=8


The scripts were modified to work with Python 3 and some of them were enhanced to fix common bugs. 
