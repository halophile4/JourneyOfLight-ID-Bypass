<p align="center">
  <img src="ToolIcon.png" alt="Tool Icon" width="167"/><br>
  <b>Journey of Light ID Verify Bypass</b><br>
</p>

# DISCLAIMER!!!!!!!!!!!
This repository is provided FOR EDUCATIONAL PURPOSES ONLY.

- This code is intended for learning, testing, and personal experimentation **only**.
- Do **not** use this repository to bypass laws, age restrictions, or authentication/ID verification systems in your country.
- I am **not responsible** for any misuse of this code.
- Always comply with the laws and regulations of your country when using network analysis tools.

By using this repository, you acknowledge that it is your responsibility to use it legally and ethically.


## Prerequisites:
Python 3 https://www.python.org/downloads/<br>
Git https://git-scm.com/

## Setup:

1. Download source via git

- Open your terminal or command prompt and run: <br>`git clone https://github.com/halophile4/JourneyOfLight-Auth-Bypass.git`
- Once downloading is finished, type this and press enter: `cd JourneyOfLight-Auth-Bypass`
- You will now be in the project directory

2. Install dependencies

- This project uses `mitmproxy`. Install it using `pip`:<br>`pip install mitmproxy`

3. Run project

- To start the proxy:<br>`python3 runner.py`<br>A terminal should open with the message<br>`Loading script modify.py`<br>`HTTP(S) proxy listening at *:8080.`

4. Find local IP

- On Windows, run this in a new command prompt: `ipconfig`<br>The line under your network adapter that says IPv4 Address is your local IP address. Take note of this.
- On Linux, run this in a new terminal/command prompt: `ifconfig`<br>Look for your active network interface (usually en0 or wlan0) and the line inet. Take note of it, as it's your IP.
- On Mac, run this in a new Terminal: `ipconfig getifaddr en0`<br>Take note what your terminal outputs, it's your IP.
- Example of a local IP: `192.168.1.42`
<br>
5. Configure your device to use proxy<br>Note: Before enabling your proxy, open the app and let it show the login page, then FULLY close the app. This ensures the game is fully updated, as updates do not download when connected to a proxy.

- iOS:<br>Open Settings -> Wi-Fi -> [i] next to your current connection -> HTTP Proxy: Configure Proxy -> Manual
- Android:<br>Settings -> Network & internet -> Wi-Fi, select your connected network, scroll to Advanced options, tap Proxy, choose Manual
<br><br>
- Host: The IP you noted in step 4.
- Port: 8080

6. Download mitmproxy certificate
- Visit http://mitm.itin a browser on the same device to install the mitmproxy certificate.
- iOS:<br>Open the certificate file, and the installation should trigger. Then, go to Settings > General > About > Certificate Trust Settings and enable full trust for the `mitmproxy` certificate.
- Android:<br>Open Settings, go to Security > Encryption & credentials, tap Install a certificate, select the file type and your certificate file, and press OK. If you're asked for a name, simply enter `mitmproxy`
7. Done
- Open the app once you fill out your proxy settings, and you should see the terminal start reporting connections.
- Once at the login page, you can input anything into the Name and ID fields and submit it, and the menu should close and let you play. Enjoy!

### Tips
If you get a notice saying you're a minor and can't play for more than an hour a day, do not tap OK and just wait until the game finishes loading. From my experience, this limit does not apply when using this.<br><br>
Only connect to the proxy when you are playing the game. Disconnect it as soon as you're finished, as a lot of online functionality in other apps do not work when connected to a proxy<br><br>
If you don't see anything in the terminal happening when you open the game even *after* it says the proxy is listening, you likely got something wrong from step 4-7 (usually 4).<br><br>If you use Android and one of the Android steps don't align with what you see, just google "how to [blank] on [phone manufacturer]". Some phones have their menus set up different from everyone elses.

<h3>If you have any issues, please do not hesitate to add me on Discord. I'm always happy to help!</h3>https://discordapp.com/users/520780595090030606