# Google_Agents
Selected Google API's gathered in one place - ready for use in your projects.

#### Included agents: Gmail, Calendar, Keep
Gmail & Calendar with official Google API's and Keep with [gkeepapi](https://github.com/kiwiz/gkeepapi).

#### Notes:
1. Must download credentials.json file from Google API Console for login to Gmail & Calender.
2. Must login before using agents functions.


## Usage examples:
```
gmail = google_agents.GmailAgent()
gmail.login()
gmail.create_message(sender=sender, to=to, subject='tests', message_text='tests)
gmail.send_message(message=msg)
```

```
calendar = google_agents.GoogleCalendarAgent()
calendar.login()
calendar.add_events(
            start_date='date',
            end_date='date',
            summary='tests',
            description='tests',
            location='tests')
```

```
keep = google_agents.GoogleKeepAgent()
keep.login(email_address=email_address, password=keep_password, token=token)
keep.create_note(title='tests', text='tests')
```
