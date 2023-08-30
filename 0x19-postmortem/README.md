## Postmortem

## Issue Summary:
Upon the release of ALX School’s System Engineering & Dev Ops project 0x19, an outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the server led to 500 Internal Server Error responses, whereas the expected response was an HTML file defining a simple Holberton WordPress site.

## Debugging Process
- 1 Process Verification: To begin the debugging process, I inspected the running processes using the ps aux command. Both apache2 processes, with root and www-data privileges, were found to be functioning correctly.

- 2 Apache Configuration Inspection: A review of the /etc/apache2/sites-available/ directory revealed that the web server was configured to serve content located in '/var/www/html/'.
- 3 Strace Analysis for Root Process: I employed strace on the PID of the root Apache process while simultaneously sending a GET request using curl. Unfortunately, this step did not yield actionable insights.

- 4 Strace Analysis for www-data Process: Repeating the process, I performed strace on the PID of the www-data process. This time, the results were fruitful. The strace output pointed to an -1 ENOENT (No such file or directory) error associated with an attempt to access the file /var/www/html/wp-includes/class-wp-locale.phpp.
- 5 Identification of the Issue: A thorough search of the files in the /var/www/html/ directory using Vim's pattern matching unveiled the erroneous .phpp file extension. The culprit was located in the wp-settings.php file (Line 137: require_once( ABSPATH . WPINC . '/class-wp-locale.php' );).

- 6 Resolution: By simply removing the extraneous 'p' from the line, the issue was resolved.

- 7 Validation Testing: A test using curl on the server confirmed the resolution with a successful 200 status response.
- 8 Automation: To mitigate similar issues in the future, a Puppet manifest was developed to automate the correction process.

## Summation:
The root cause of the issue was a typo within the WordPress application. The typo led the application to erroneously attempt loading the file class-wp-locale.phpp instead of the correct class-wp-locale.php, causing a critical error in wp-settings.php. The resolution entailed rectifying the typo by removing the extraneous 'p'.

## Prevention:

Test the application thoroughly before deployment to catch errors like this early in the development cycle.
Consider automated testing and continuous integration to prevent such issues from reaching production.

In response to this incident, a Puppet manifest was created to automatically correct similar errors in the future by replacing any phpp extensions in the wp-settings.php file with php.
By following these practices, we aim to enhance the robustness and reliability of our systems, preventing similar outages and improving our overall development and deployment processes.
