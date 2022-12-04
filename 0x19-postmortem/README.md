<p align="center">
	<img src="https://github.com/eleccrazy/alx-system_engineering-devops/blob/main/0x19-postmortem/postmortem.png"/>
</p>

#### Issue Summary
On February 16th 2022 from 10:00AM to 10:10AM EAT the company's website was down. 100% of the users were experiencing Error 500 caused by mispelled filename in the configuration file of the server.

#### Timeline
* 10:00AM - Server error occurs and outage is detected
* 10:02AM - On-call devOps team checks the error logs
* 10:03AM - Updates error configuration
* 10:04AM - Filename error caught on the configuration file
* 10:06AM - Writes a puppet manifest file to correct the error
* 10:08AM - puppet manifest file is executed across all company servers
* 10:10AM - Website is fully restored and working perfectly.


#### Root Cause and Resolution
The outage of the website began, we checked the 'error.log' file for the cause but surprisingly no errors were listed. We modified the 'php.ini' file by changing the line 'display_errors=off' to 'display_errors=on'. This allowed more erorr logging on the error file. With the help of `strace`, it appeared that there was a mispelling of a filename that triggered an error whenever a request was sent to the website. The server was trying to locate the file as normal procedure but failed to find the file ending in ".phpp" when it should be looking for ".php". After changing this line in the '/var/www/html/wp-settings.php' file line 137, the site was back working perfectly 100%. A puppet manifest was written and executed across all company servers immediately after to restore service.

#### Corrective and Preventative Measures
After this error fixing we decided on the corrective and preventive measures that we should take to avoid future failures like this.
* To run as many tests as possible on the site before deploying so that mulfunctions can be detected and corrected.
* To thoroughly check the configuration files before deploying for any typo.
* Keep the error display on for any possible errors.

#### [Reference](https://github.com/Janengethe/alx-system_engineering-devops/blob/main/0x17-web_stack_debugging_3/README.md)
