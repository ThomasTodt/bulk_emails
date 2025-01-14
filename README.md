# Send emails individually to a list

#### This script is useful for sending HTML emails to a list of emails from a .csv file, where:

- column 0 - name of receiver (Optional)
- column 1 - receiver email

emails are sent with an interval of 2 seconds each (respecting Outlook's 30 mails per minute limit)

#### How to use:

- email_body.html: the content of the email body
- email_list.csv: the list of emails
- email_subject.txt: the subject of your emails

##### autodear
- this is an additional feature. It replaces 'Dear' with 'Dear [name of receiver]' in the email body content
- (you need to press 'y' and ENTER when prompted to activate this feature. 'n' + ENTER or simply ENTER will ignore it)