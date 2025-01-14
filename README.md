<h1 align="center"> Automating Binary Exploitation</h1>
<h4 align="center">Learn how to use Python to overflow a buffer, corrupting the Saved Return Pointer.</h4>

<p align="center">
  <a href="#Tools">Tools</a> •
  <a href="#Requirements">Requirements</a> •
  <a href="#Steps">Steps</a> •
  <a href="#Credits">Credits</a>
</p>

___

<h4>Do you want to learn how to automate your buffer overflows?</h4>
<p>
If you are preparing for the OSCP exam or simply want to learn more about buffer overflows, this repo is for you! 
It follows the 7 steps by "The Cyber Mentor" with links to his videos and the modified code I wrote. 
</p>

## Tools
* A <strong>Windows 10</strong> desktop. Download a virtual machine [here](https://www.microsoft.com/en-us/software-download/windows10ISO)
* A vulnerable software: <strong>Vulnserver</strong>. Download the [repo](https://github.com/stephenbradshaw/vulnserver) into a new folder.
* <strong>Kali Linux</strong> or any other OS for offensive work. Download Kali's virtual image [here](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/)
* A debugger: <strong> Immunity Debugger</strong>. Download it [here](https://debugger.immunityinc.com/ID_register.py). (You will need to register in the link, so be creative.)


## Requirements

Before we start learning. You will need to do the following:

1. <strong> Temporarily </strong>disable Windows Defender Real-time protection. Confused? Info [here](https://www.windowscentral.com/how-disable-real-time-protection-microsoft-defender-antivirus)
2. Go to the saved Vulnserver folder and run the exe as admin.
3. Run Immunity as admin. 

## Steps
<p>
Follow each of the 7 steps by first clicking the link to watch the "The Cyber Mentor" tutorial and then use the modified code I wrote on your network:
</p>

|Folder Name|Video Link|
|------|--------|
|Spiking|[Video](https://www.youtube.com/watch?v=3x2KT4cRP9o&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=2)||
|Fuzzing|[Video](https://www.youtube.com/watch?v=FCIfWTAtPr0&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=3)||
|Find_EIP|[Video](https://www.youtube.com/watch?v=GqwyonqLYdQ&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=4)||
|Overwrite_EIP|[Video](https://www.youtube.com/watch?v=Wh9wRKBzajo&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=5)||
|Bad_chars|[Video](https://www.youtube.com/watch?v=uIFYNVqpZ0k&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=6)||
|Right_Module|[Video](https://www.youtube.com/watch?v=k9D9RuFT02I&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=7)||
|Exploit|[Video](https://www.youtube.com/watch?v=qSjxR8tfokg&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G&index=8)||



<h5>Please note the scripts were modified to work with Python 3 and some of them were enhanced to fix common bugs.</h5>

<br />


## Credits


This repo was created while watching the "Buffer Overflows Made Easy" Masterclass by "The Cyber Mentor". 
I want to thank him for putting out these videos. You can watch them in [video](https://www.youtube.com/watch?v=qSnPayW6F7U&list=PLLKT__MCUeix3O0DPbmuaRuR_4Hxo4m3G) or read them as [doc](https://tcm-sec.com/buffer-overflows-made-easy). 

To learn more about the changes in the code, I highly recommend to read Justin Steven's [dostackbufferoverflowgood](https://github.com/justinsteven/dostackbufferoverflowgood) I also want to thank him for putting this amazing tutorial out there, and for answering some questions.


## License

The code is licensed under the MIT License.
