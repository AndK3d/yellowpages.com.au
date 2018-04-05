# yellowpages.com.au
Scrapping e-mails from from specified categories on the yellowpages.com.au

The site yellowpages.com.au at the beginning of the work requires you to get google captcha. 
I could not solve this programmatically, this should be entered manually in your browser, for example in Firefox.
After that, the cookie appears, which contains the session ID. This session identifier must be manually assigned to the variable JSESSIONID in the code by the usual method of copy/paste.
The script will work correctly until the session time ends, after which the actions with the variable JSESSIONID will need to be repeated.
