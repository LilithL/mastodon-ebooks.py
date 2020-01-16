#!/usr/bin/python3

# interactive script for generating persistent
# clientcred and usercred files for mastodon.py

from mastodon import Mastodon
from getpass import getpass
import sys
import json

if __name__ == "__main__":
    app = input('app name (shows in web): ')
    url = input('instance url: ')
    email = input('account email: ')
    password = getpass('account password: ')
    password2 = getpass('repeat password: ')
    if password2 != password:
        sys.exit('passwords did not match')

    Mastodon.create_app(
        app,
        api_base_url=url,
        to_file='clientcred.secret'
    )

    mastodon = Mastodon(
        client_id='clientcred.secret',
        api_base_url=url
    )

    usercred = {'url': url,
                'token': mastodon.log_in( email, password)
                }

    with open('usercred.secret', 'w') as f:
        json.dump(usercred, f)

