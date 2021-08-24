from question_test_site.celery import app
from .models import TestRun, Test
from datetime import timedelta
from django.db.models import F
from question_test_site.settings import BASE_DIR
import csv
from django.utils.timezone import now

filename = BASE_DIR + '/report.csv'

@app.task
def create_log():

    date_checker = now() - timedelta(days=1)
    test_passed = TestRun.objects.filter(created_at__gt=date_checker)
    tests = Test.objects.all()
    with open(filename, 'w', newline='') as file:
        title_row = ['TEST', 'COUNT OF FULL PASSED', '% OF ALL PASSED']
        writer = csv.writer(file, delimiter=',')
        writer.writerow(title_row)

        for test in tests:
            passed_test = test_passed.filter(test=test)
            amount_total = len(passed_test)
            amount_full = len(passed_test.filter(
                count_of_questions=F("count_of_created_questions")
            ))
            if amount_full == 0 or amount_total == 0:
                writer.writerow([test.title, str(amount_total), str(0)])
            else:
                writer.writerow([test.title, str(amount_total), str(round((amount_full/amount_total) * 100, 2))])




