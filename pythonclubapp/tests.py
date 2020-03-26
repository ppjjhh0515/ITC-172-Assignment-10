from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.

class MeetingTest(TestCase):
    def test_string(self):
        type=Meeting(meetingtitle='Weekly team meeting')
        self.assertEqual(str(type), type.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting Name')
    
class MeetingMinutesTest(TestCase):
    def test_string(self):
        type=MeetingMinutes(minutename='Interview Session')
        self.assertEqual(str(type), type.minutename)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'Minute Name')
 
class ResourceTest(TestCase):
    def test_string(self):
        type=Resource(resourcename='zoom')
        self.assertEqual(str(type), type.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

class EventTest(TestCase):
    def test_string(self):
        type=Event(eventtitle='Board meeting')
        self.assertEqual(str(type), type.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')


class New_Meeting_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=Meeting.objects.create(typename='testmeeting')
        self.md = Meeting.objects.create(meetingtitle='meeting1', meetingdate='2020-03-26', meetingtime='11:00', location='Seattle', agenda='fortesting')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newMeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/pythonclubapp/newMeeting/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pythonclubapp/newmeeting.html')