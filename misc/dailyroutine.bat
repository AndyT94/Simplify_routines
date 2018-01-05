@ECHO OFF
SET BROWSER=firefox.exe
SET WAIT_TIME=2
START %BROWSER% -new-tab "www.facebook.com"
@ping 127.0.0.1 -n %WAIT_TIME% -w 1000 > nul
START %BROWSER% -new-tab "www.youtube.com/feed/subscriptions"
START %BROWSER% -new-tab "mail.google.com/mail/u/0/#inbox"
START %BROWSER% -new-tab "mail.google.com/mail/u/1/#inbox"
START %BROWSER% -new-tab "mail.google.com/mail/u/2/#inbox"
