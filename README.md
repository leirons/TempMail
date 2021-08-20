# Temp-Mail Api Wrapepr
Python API wrapper for 1secmail.com/api/. Temp mail lets you use anonymous emails for free
## Requirements
- requests
## Installation
- pip install temp-email

## Usage
Get list of active domains
```
from tempmail import TempMail
email = TempMail() # you can youse your login
print(email.get_list_of_active_domain())
```
Generate random email address

```
from tempmail import TempMail
email = TempMail() # you can youse your login
email.generate_random_email_address()
```
Get your login and domain
```
from tempmail import TempMail
email = TempMail()
get.login()
get.domain()
```
Download single file from MailBox
```
from tempmail import TempMail()
email = TempMail(login='login')
email.download_attachments_by_id(id=12312,attachemnts='file.jpg')
```

Download all files from MailBox
```
from tempmail import TempMail()
email = TempMail(login='login')
email.download_all_files()
```


Get list of emails
```
from tempmail import TempMail()
email = TempMail(login='login')
email.get_list_of_emails()
```
