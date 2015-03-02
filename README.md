# NOTICE: THIS WILL DELETE EVERY PUBLIC MESSAGE IN EVERY CHANNEL. THIS CANNOT BE UNDONE.

This will *not* delete DMs or messages in private groups. This only affects public conversations.

# burnnotice
Destroy the entire public history of your Slack group. This includes messages beyond the 10,000 limit that you cannot see in a free tier group.

# Requirements

Must be run by an admin.

python

# Howto

1. git clone https://github.com/rawdigits/burnnotice.git
2. Get a web api token here [https://api.slack.com/web](https://api.slack.com/web)
3. Run an export here [https://[yourdomain].slack.com/services/export?started=1](https://creednation.slack.com/services/export?started=1)
4. Download the resulting file in #3 to the burnnotice directory
5. MAKE DAMN SURE YOU WANT TO DO THIS
6. python burnnotice.py [api token from #2] [filename from #4]
