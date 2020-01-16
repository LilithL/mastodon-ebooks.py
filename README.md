# mastodon-ebooks.py

Simple ebooks-style bot for mastodon.py

Inspired by original work by Jess: https://github.com/Jess3Jane/mastodon-ebooks


## Improvements over other ebooks bots

* Scrapes only new toots, not entire list of statuses
* Separates corpus by account, making a multi-account ebooks easier to manage
* Does not require Heroku or Ruby
* "Smart" replies
* Cronjob friendly

## Usage

1. Create a Mastodon account to be the ebooks bot
2. Follow the account(s) to be used as source material from bot
3. You can use a script [like this](https://gist.github.com/Lana-chan/b0d937968d22eca6dcd79a0524449f1d) to generate user secrets to be used by the ebooks script
4. Scrape the users by running: `./mastodon-ebooks.py -s`
5. Verify the markov works by running locally to console: `./mastodon-ebooks.py -p`
6. Toot a markovified status! `./mastodon-ebooks.py -t`

Alternatively, you can loop indefinitely (reply every 10 seconds, toot and scrape toots every 30 minutes) `./mastodon-ebooks.py -l`

Optionally, you can also run `./mastodon-ebooks.py -r` regularly to check on notifications and reply to mentions.