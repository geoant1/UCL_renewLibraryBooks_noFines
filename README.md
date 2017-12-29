# UCL_renewLibraryBooks_noFines
Here's a script with Selenium API to automatically renew library loans not to be exasperated by fines. Make this script run with OSX/whatever reboot.

### Requirments:
* Selenium - can be installed via pip or miniconda (or anaconda) by running
```
sudo pip2 install selenium
```
  or
```
conda install -c conda-forge selenium 
```
* Chromedriver (or geckodriver) in PATH - allows the script to control a browser. Can be installed via normal package manager like homebrew. apt-get or yum, then moved to /usr/bin/
```
sudo apt-get install chromedriver
```
Then check where it has been installed and move it to bin
```
sudo mv <location of your chromedriver> /usr/local/bin/
```
### Usage
Run the script using this command (while in directory of the script):
```
python ./Renew_library.py -u <your barcode> -p <your password>
```
This script can be put in cron to run daily or in autostart to run from the start

### Cron
Put the script into a crontab to execute periodically (e.g. once a week)
* Create a crontab by typing
```
EDITOR=nano crontab -e
```
* Enter the job to be executed in the desired format, then ctrl+o, ctrl+x. Done.
* You can list the crontabs by typing
```
crontab -l
```
