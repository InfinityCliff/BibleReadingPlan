import BibleOutline
import pandas as pd
import numpy as np

class ReadingPlan(object):

    def __init__(self):
        super().__init__()
        self.plan = BibleOutline.BibleOutline()             # plan outline
        self.days_of_week_to_read_ = [1, 2, 3, 4, 5, 6, 7]  # days of week reading will occur, 1 is Monday
        self.reading_plan = []                              # ordered list of the actual plan by day number
                                                            # [book:chap-chap]
        self.day_count = 0                                  # count of number of days in plan
        self.book_count = 66                                # count of number of books in plan
        self.chap_count = 1189                              # count of number of chapters in plan
        self.chaptersPerDay = 3                             # number of chapters to read per day
        self.chaptersLastDay = 94                           # chapters on last day, dont think is needed
        self.plan_name = ''
        self.plan_df = pd.DataFrame(index=range(1, 53),
                                    columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
                                             'Sunday'])

    def __str__(self):
        super().__str__()

        return "\nClass: {} \n" \
               "Plan ID: {} \n" \
               "Number of Days: {}\n" \
               "Number of Books: {}\n" \
               "Number of Chapters: {}\n" \
               "Chapters Per Day: {}\n" \
               "Chapters on Last Day: {}\n" \
               "df: {}".format(self.__class__.__name__, self.plan_name, self.day_count,
                               self.book_count, self.chap_count, self.chaptersPerDay,
                               self.chaptersLastDay, self.plan_df)

    def define_reading_plan(self, plan_id='alpha_omega', day_count=365, read=[1, 2, 3, 4, 5, 6, 7], not_read=None):
        self.plan_name = plan_id
        self.day_count = day_count
        self.book_count = self.count_b()
        self.chap_count = self.count_c()
        self.days_of_week_to_read(read, not_read)
        self.chaptersLastDay = self.chap_count - self.day_count * self.chaptersPerDay
        self.create_plan()

    def create_plan(self):
        self.reading_plan.append(self.plan_name)
        self.plan_df.fillna(self.chaptersPerDay, inplace=True)
        # for index, row in self.plan_df.iterrows():

    @staticmethod
    def day_to_int(days_to_conv):
        """
        converts string 'days of week' 'Mon', 'tues', etc to respective integer values, 1 is Monday, etc
        :param days_to_conv: List(string): list of day to convert 
        :return: List of Integers
        """
        for i, day in enumerate(days_to_conv):
            if day.upper() in ['M', 'MONDAY', 'MON', '1', 1]:
                days_to_conv[i] = 1
            elif day.upper() in ['TU', 'TUESDAY', 'TUE', '2', 2]:
                days_to_conv[i] = 2
            elif day.upper() in ['W', 'WEDNESDAY', 'WED', '3', 3]:
                days_to_conv[i] = 3
            elif day.upper() in ['TH', 'THURSDAY', 'THUR', '4', 4]:
                days_to_conv[i] = 4
            elif day.upper() in ['F', 'FRIDAY', 'FRI', '5', 5]:
                days_to_conv[i] = 5
            elif day.upper() in ['SA', 'SATURDAY', 'SAT', '6', 6]:
                days_to_conv[i] = 6
            elif day.upper() in ['SU', 'SUNDAY', 'SUNDAY', '7', 7]:
                days_to_conv[i] = 7
            else:
                raise ValueError('%s is not a valid Day of Week' % day)

        return days_to_conv

    def days_of_week_to_read(self, read=[1, 2, 3, 4, 5, 6, 7], not_read=None):
        """
        Sets days of week to read, or not read
        :param read: List(int): days of week to read, default is all days, 1 is Monday, etc
        :param not_read: List(int): days of week to not read, will override read if both sent
        :return: None
        """
        if not_read is not None:
            not_read = self.day_to_int(not_read)
            for day in not_read:
                    self.days_of_week_to_read_.remove(day)
        else:
            self.days_of_week_to_read_ = read

    def count_b(self):
        """
        counts books in plan
        :return: int
        """
        return len(self.plan.reading_plan_books(self.plan_name))

    def count_c(self):
        """
        Counts chapters in plan
        :return: int 
        """
        count = 0
        for book in self.plan.reading_plan_books(self.plan_name):
            count += self.plan.chapters(book)
        return count

    def chap_per_day(self):
        """
        Determines chapter per day matrix
        :return: None
        """
        self.chaptersPerDay = int(self.chap_count / self.day_count)
        self.chaptersLastDay = self.chap_count - self.chaptersPerDay * self.day_count

if __name__ == '__main__':
    plan = ReadingPlan()
    pt = input("Enter Plan type: ")
    if pt == '':
        pt = 'alpha_omega'
    days = input("Enter Days to read: ")
    days_to_not_read = input('Enter days of week to not read, separated by comma [M, TU, W, TH, F, SA, SU]')
    if days_to_not_read != '':
        days_to_not_read = days_to_not_read.split(',')
    else:
        days_to_not_read = None

    if days == 0 or days == '':
        days = 365
    plan.define_reading_plan(plan_id=pt, day_count=days, not_read=days_to_not_read)

    print(plan)
