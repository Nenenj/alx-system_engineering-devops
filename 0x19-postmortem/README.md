## Postmortem

- Upon the release of `ALX School’s System Engineering & Dev Ops project 0x19`, an outage occurred on an isolated `Ubuntu 14.04` container running an Apache web server. GET requests on the server led to 500 Internal Server Error's, when the expected response was an HTML file defining a simple Holberton WordPress site .

## Debugging Process
- 1 : Process Verification: I initiated the debugging process by examining the running processes using the ps aux command. It was evident that both apache2 processes, with root and www-data privileges, were functioning correctly. 2 : Looked in the sites-available folder of the /etc/apache2/ directory. Determined that the web server was serving content located in /var/www/html/.

- 2 Apache Configuration Inspection: I investigated the /etc/apache2/sites-available/ directory to understand the server's configuration. This inquiry confirmed that the web server was set up to serve content from the /var/www/html/ directory.

- 3 Strace Analysis for Root Process: Attempting to identify the issue, I utilized strace on the PID of the root Apache process while concurrently sending a GET request using curl. Regrettably, this yielded no actionable insights.

- 4 Strace Analysis for www-data Process: Replicating the process, I performed strace on the www-data process's PID. This time, the outcome was productive. The strace results indicated an -1 ENOENT (No such file or directory) error tied to an attempt to access the file /var/www/html/wp-includes/class-wp-locale.phpp.
- 5 : Looked through files in the /var/www/html/ directory one-by-one, using Vim pattern matching to try and locate the erroneous .phpp file extension. Located it in the wp-settings.php file. (Line 137, require_once( ABSPATH . WPINC . '/class-wp-locale.php' );).

- 6 : Removed the trailing p from the line.

- 7 : Tested another curl on the server. 200 A-ok!

- 8 : Wrote a Puppet manifest to automate fixing of the error.

	* Summation
- In essence, the issue stemmed from a typo within the WordPress application. The error manifested when the application attempted to load the file class-wp-locale.phpp instead of the correct file class-wp-locale.php, precipitating a critical error in wp-settings.php. 
- The resolution involved rectifying the typo by eliminating the extraneous 'p'.

	* Prevention
- This outage was not a web server error, but an application error. To prevent such outages moving forward, please keep the following in mind.

- Test the application before deploying. This error would have arisen and could have been addressed earlier had the app been tested.

- Note that in response to this error, I wrote a Puppet manifest [0x17-web_stack_debugging_3](0-strace_is_your_friend.pp) to automate fixing of any such identitical errors should they occur in the future. The manifest replaces any phpp extensions in the file /var/www/html/wp-settings.php with php.
