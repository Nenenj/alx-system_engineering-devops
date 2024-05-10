
## Postmortem: ALX School's System Engineering & Dev Ops Project Outage

## Issue Summary:
During the release of ALX School’s System Engineering & Dev Ops project 0x19, I encountered an outage on an isolated Ubuntu 14.04 container hosting an Apache web server. GET requests to the server resulted in 500 Internal Server Error responses instead of the expected HTML file for a Holberton WordPress site.

## Debugging Process:
1. Process Verification: I verified running processes using the ps aux command, confirming both apache2 processes were functioning.
2. Apache Configuration Inspection: Reviewing the /etc/apache2/sites-available/ directory, I found the correct configuration to serve content from /var/www/html/.
3. Strace Analysis for Root Process: Employing strace on the root Apache process PID while sending a GET request, I found no actionable insights.
4. Strace Analysis for www-data Process: Further analysis using strace on the www-data process PID revealed an -1 ENOENT (No such file or directory) error attempting to access /var/www/html/wp-includes/class-wp-locale.phpp.
Identification of the Issue: I discovered a typo with a .phpp file extension instead of .php in the wp-settings.php file, causing the critical error.

## Resolution: Correcting the typo by removing the extraneous 'p' from the file path.
Validation Testing: Confirming resolution with a successful curl test returning a 200 status response.
Automation: Developing a Puppet manifest to automate the correction process and mitigate similar issues in the future.

## Summation:
The root cause of the outage was a typo within the WordPress application, which I identified, leading to the erroneous loading of a file with a .phpp extension instead of the correct .php extension. Rectifying the typo by removing the extraneous 'p' from the file path resolved the issue.

## Prevention:
Thoroughly testing applications before deployment to catch errors early in the development cycle.
Implementing automated testing and continuous integration to prevent similar issues from reaching production.
Developing automation scripts, like the Puppet manifest created, to automatically correct common errors and enhance system reliability.
By adhering to these practices, I aim to prevent similar outages in the future and improve the overall robustness of our systems.
