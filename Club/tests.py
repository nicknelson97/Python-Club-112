from django.test import TestCase
from . models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.

class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(mtitle='meeting')
        

    def test_typestring(self):
        self.assertEqual(str(self.type), 'meeting')
    
    def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')