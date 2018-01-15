# UCL_renewLibraryBooks_noFines
Here's a script with Selenium API to automatically renew library loans not to be exasperated by fines.

### Requirments:
* macOS 10.13 (or higher)
* Python 2.7
* Anaconda
* Selenium
* ChromeDriver

### Installations:
* Anaconda can be installed by following the instructions on https://conda.io/docs/user-guide/install/index.html

* To install Selenium, type in the terminal:
```
conda install -c conda-forge selenium 
```
* Chromedriver can be installed via normal package manager like homebrew or downloaded from: https://sites.google.com/a/chromium.org/chromedriver/downloads

* Then check where it has been installed and move to bin:
```
sudo mv <location of your chromedriver> /Users/'your user name'/anaconda2/bin
```
### Usage:
* Don't forget to change the path for the logout file in the record() method of Renew_library.py

* Make the script executable:
```
chmod +x <full path to Renew_library.py>
```

* Run the script using this command in the terminal:
```
<full path to the script> -u <your barcode> -p <your password>
```
* Check the logout file for an update

## Cron
This script can be put in cron or launchd to run daily or upon the reboot. **NB: cron will execute the script only at the specified time.** If your are on a laptop and not sure that it will always be turned on at that time, skip to the launchd section.

* Create a cronjob by typing in the terminal:
```
EDITOR=nano crontab -e
```
* Enter the job to be executed in the desired format. To renew every Tuesday, type:
```
* * * * 2 <path to the file to be executed> -u <your username> -p <your password>
```
* Don't forget to replace the first two stars with minutes and hour, respectively
* Then hit ctrl+O, enter, and ctrl+X. Done.
* You can list the crontabs by typing:
```
crontab -l
```
## Launchd
* Download the com.renew_library.plist file and move it to ~/Library/LaunchAgents
* Change the paths within the file. You can open and edit this file with Sublime or with the terminal:
```
nano -e ~/Library/LaunchAgents/com.renew_library.plist
```
* Then in the terminal, type:
```
launchctl load -w ~/Library/LaunchAgents/com.renew_library.plist
launchctl start -w ~/Library/LaunchAgents/com.renew_library.plist
```
* You can check if it's been loaded:
```
launchctl list | grep renew
```
Now it should work for you!

* To remove the agent, type:
```
launchctl unload -w ~/Library/LaunchAgents/com.renew_library.plist
launchctl remove renew_library
```
