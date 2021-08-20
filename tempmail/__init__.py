import requests
import random


class TempMail():
    """
    Api wraooer provides temporary email address
    :param login: (optimal) login for email address
    :param domain:(optimal) domain for email address
    Default domain 1secmail.com
    """

    def __init__(self, login=None, domain='1secmail.com'):
        self.login = login
        self.domain = domain

    def generate_random_email_address(self) -> None:
        """Generates random email"""
        r = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=10')
        get_random = f'{random.choice(r.json())}'
        self.login, self.domain = get_random.split('@')

    @property
    def get_list_of_active_domains(self):
        """Return active domains for email address"""
        return requests.get('https://www.1secmail.com/api/v1/?action=getDomainList').json()

    def get_list_of_emails(self):
        """checks the mailbox for messages and returns them"""
        if self.login is None or self.domain is None:
            self.generate_random_email_address()
        r = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={self.login}&domain={self.domain}')
        return r.json()

    def get_login(self):
        """Get currently login"""
        return self.login

    def get_domain(self):
        """Get currently domain"""
        return self.domain

    def download_attachment_by_id(self, attachment: str, id: str):
        """
        Downloads attachment from email
        :param attachment:Name of file, example: file1.jpg or file1.png or file1.pdf
        :param id:Id of messages
        """
        if self.login is None or self.domain is None:
            return 'You cant download anything, your login or domain is None.'

        r = requests.get(f"https://www.1secmail.com/api/v1/?action=download&login="
                         f"{self.login}&domain={self.domain}&id={id}&file={attachment}")
        print(r.text)

        if 'Message not found' in r.text:
            return 'The file could not be found, please check the correctness of the entered data'

        with open(attachment, 'wb') as file:
            file.write(r.content)

    def download_all_files(self):
        """Download all files from mailbox"""
        emails = self.get_list_of_emails()
        lst_with_files = []
        for i in emails:
            r = requests.get(
                f'https://www.1secmail.com/api/v1/?action=readMessage&login={self.login}&domain={self.domain}&id={i["id"]}').json()
            lst_with_files.append(
                {
                    'filename': f"{r['attachments'][0]['filename']}",
                    'id': f"{i['id']}"
                }
            )
        for i in lst_with_files:
            self.download_attachments_by_id(i['filename'], i['id'])



