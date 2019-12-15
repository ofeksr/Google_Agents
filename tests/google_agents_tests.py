import unittest
from datetime import datetime

import google_agents
from tests.database.login_info import *


class TestGmailAgent(unittest.TestCase):

    def setUp(self) -> None:
        self.gmail = google_agents.GmailAgent()

    def tearDown(self) -> None:
        self.gmail = None

    def test_login(self):
        self.assertTrue(self.gmail.login(),
                        msg='Failed to log in to Google Account')

    def test_list_inbox(self):
        self.gmail.login()
        self.assertIsInstance(self.gmail.list_messages_from_inbox(),
                              list,
                              msg='Failed to get message')

    def test_get_message(self):
        self.gmail.login()
        messages = self.gmail.list_messages_from_inbox()

        self.assertIsInstance(self.gmail.get_message(message_id=messages[0]['id']),
                              str,
                              msg='Failed to get message')

    def test_create_message(self):
        self.assertIsInstance(self.gmail.create_message(sender=sender, to=to,
                                                        subject='tests', message_text='tests'),
                              dict,
                              msg='Failed to create message')

    def test_send_message(self):
        self.gmail.login()
        msg = self.gmail.create_message(sender=sender, to=to,
                                        subject='tests', message_text='tests')

        self.assertTrue(self.gmail.send_message(message=msg),
                        msg='Failed to send message')

    def test_delete_message(self):
        self.gmail.login()
        messages = self.gmail.list_messages_from_inbox()

        self.assertTrue(self.gmail.delete_message(message_id=messages[0]['id']),
                        msg='Failed to trash message')


global event_id


class TestGoogleCalendarAgent(unittest.TestCase):

    def setUp(self) -> None:
        self.calendar = google_agents.GoogleCalendarAgent()

    def tearDown(self) -> None:
        self.calendar = None

    def test_login(self):
        self.assertTrue(self.calendar.login(),
                        msg='Failed to log in to Google Account')

    def test_add_event_calendar_and_delete(self):
        self.calendar.login()
        date = datetime.today().strftime('%Y-%m-%d')

        self.assertIsNotNone(self.calendar.add_events(
            start_date=date,
            end_date=date,
            summary='tests',
            description='tests',
            location='tests',
            delete=True),
            msg='Failed to insert new event')


class TestGoogleKeepAgent(unittest.TestCase):

    def setUp(self) -> None:
        self.keep = google_agents.GoogleKeepAgent()

    def tearDown(self) -> None:
        self.keep = None

    def test_login(self):
        self.assertTrue(self.keep.login(email_address=email_address, password=keep_password, token=token),
                        msg='Failed to log in to Google Account')

    def test_create_note(self):
        self.keep.login(email_address=email_address, password=keep_password, token=token)
        self.assertIsInstance(self.keep.create_note(title='tests', text='tests'),
                              str,
                              msg='Failed to create note')

    def test_create_list(self):
        self.keep.login(email_address=email_address, password=keep_password, token=token)
        self.assertIsInstance(self.keep.create_list(title='tests', items=[('t1', False), ('t2', True)]),
                              str,
                              msg='Failed to create list')

    def test_add_events(self):
        self.keep.login(email_address=email_address, password=keep_password, token=token)
        self.assertTrue(self.keep.add_events_to_list(list_id=trash_list_id, events=[]),
                        msg='Failed to add events to Google Keep list')

    def test_sort_items(self):
        self.keep.login(email_address=email_address, password=keep_password, token=token)
        self.keep.add_events_to_list(list_id=trash_list_id, events=[])
        self.assertTrue(self.keep.order_list_items_by_date(list_id=trash_list_id),
                        msg='Failed to sort list items')


if __name__ == '__main__':
    unittest.main()
