import BibleOutline
import pandas as pd
import numpy as np
import icdatetime
from icdatetime import format_weekday
from Events import EventHook

class ReadingPlan(object):
    """
    Develop reading plan for Bible.
    
    **Methods:**
    
    **__init__** : constructor
    
    **__str__** : print object
    
    **define_reading_plan** : develops or re-defines the reading plan
    
    **daily_reading** : Pulls the number of chapters from the reading list and formats the text to display
    
    **create_plan** : Creates reading plan
           
    **days_of_week_to_read** : Sets days of week to read, or not read
    
    **count_b** : Count of books in plan
    
    **count_c** : Count of chapters in plan

    **Attributes:**
        plan : BibleOutline.BibleOutline 
            plan outline    
        days_of_week_to_read_ : list (int)
           days of week reading will occur, 1 is Monday
        not_read = None                     # days of week reading will not occur
        reading_plan = []                   # ordered list of the actual plan by day number 'book:chap-chap'
        day_count = 0                       # count of number of days in plan
        start_day = ''                      # day of week to start reading plan
        week_count = 0                      # count of number of weeks in plan
        book_count = 0                      # count of number of books in plan
        chap_count = 0                      # count of number of chapters in plan
        chaptersPerDay = 0                  # number of chapters to read per day
        chapters_remainder = 0              # chapters on last day, dont think is needed
        plan_id = ''
        plan_df = pd.DataFrame()
        reading_list = []
                
    """
    def __init__(self):
        super().__init__()
        self.plan = BibleOutline.Bible_Outline()  # plan outline
        self.days_of_week_to_read_ = []          # days of week reading will occur, 1 is Monday
        self.not_read = None                     # days of week reading will not occur
        self.reading_plan = []                   # ordered list of the actual plan by day number 'book:chap-chap'
        self.day_count = 0                       # count of number of days in plan
        self.start_day = ''                      # day of week to start reading plan
        self.week_count = 0                      # count of number of weeks in plan
        self.book_count = 0                      # count of number of books in plan
        self.chap_count = 0                      # count of number of chapters in plan
        self.chaptersPerDay = 0                  # number of chapters to read per day
        self.chapters_remainder = 0              # chapters on last day, dont think is needed
        self.plan_id = ''
        self.plan_df = pd.DataFrame()
        self.reading_list = []
        self.controller = None
        self.observers = [self.controller]
        self.psalms = False
        self.proverbs = False
        self.wisdom = False
        self.key_dict = {'day_count': self.day_count, 'plan_id': self.plan_id, 'psalms': self.psalms, 'proverbs': self.proverbs,
                         'wisdom': self.wisdom}
        pd.set_option('display.width', 1000)

    def __str__(self):
        super().__str__()

        return "\nClass: {} \n" \
               "Plan ID: {} \n" \
               "Number of Days: {}\n" \
               "Number of Books: {}\n" \
               "Number of Chapters: {}\n" \
               "Chapters Per Day: {}\n" \
               "df: {}".format(self.__class__.__name__, self.plan_id, self.day_count, self.book_count,
                               self.chap_count, self.chaptersPerDay, self.plan_df)

    def set_controller(self, controller):
        self.controller = controller

    def update(self, **kwargs):
        if kwargs:
            for key, value in kwargs:
                self.key_dict[key] = value
        print(self.key_dict)

    def define_reading_plan(self, plan_id='alpha_omega', day_count=365, read=(1, 2, 3, 4, 5, 6, 7), not_read=None,
                            start_day='Sunday'):
        """
        Provide the parameters needed to define the reading plan
        
        Parameters
        ----------
        plan_id : text : default='alpha_omega'
            ID of plan type
        day_count : int : default=365
            Number of days over which reading will take place
        read : tuple : default=(1, 2, 3, 4, 5, 6, 7)
            Days of week on which reading will occur
            TODO - need to decide if 1 will always be sunday or if it be based on `start_day`
        not_read : list : default=None
        start_day : str : default='Sunday'
             Day of week on which to start the reading plan
             
        Return
        ------
        None
        """

        self.day_count = int(day_count)
        self.week_count = int(self.day_count / 7)
        if time_type == 'week':
            self.plan_df = pd.DataFrame(columns=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                                                 'Saturday'])
            self.plan_df['Week'] = list(range(1, self.week_count + 1))
            self.plan_df.set_index('Week', inplace=True)
        self.start_day = start_day
        self.plan_id = plan_id
        self.book_count = self.count_b()
        self.chap_count = self.count_c()
        self.days_of_week_to_read(list(read), not_read)
        self.chaptersPerDay = int(self.chap_count / self.day_count)
        self.create_plan()

    def daily_reading(self, chapters):
        """
        Pulls the number of `chapters` from the reading list and formats the text to display
        
        Parameters
        ----------
        chapters : int 
            number of chapters to include
            
        Return
        ------
        text of daily reading : str
        """
        daily = ''
        prev_book = ''
        for c in range(chapters):
            if len(self.reading_list) > 0:
                book, chap = self.reading_list.pop(0)
                abbr = self.plan.bible_outline[book]['abbr']
            else:
                break
            if abbr != prev_book:
                if c > 1:
                    sep = ', '
                else:
                    sep = ''
                daily = daily + sep + abbr + ' ' + str(chap)
                prev_book = abbr
            if abbr == prev_book:
                if c == chapters - 1:
                    daily = daily + '-' + str(chap)
        daily = daily + ' | ' + str(chapters)
        return daily

    def create_plan(self):
        """
        Creates reading plan
        
        Return
        ======
        None
        """
        self.reading_plan = [self.chaptersPerDay] * self.day_count
        i = 0
        while sum(self.reading_plan) < self.chap_count:
            self.reading_plan[i] = self.reading_plan[i] + 1
            i += 1
        rl = self.reading_plan.copy()
        for i, chapters in enumerate(rl):
            self.reading_plan[i] = self.daily_reading(chapters)

        week_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        shift = week_list.index(format_weekday(self.start_day, format_='full'))
        for s in range(1, shift + 1):
            self.reading_plan.insert(0, None)

        weekly = [self.reading_plan[x:x+7] for x in range(0, len(self.reading_plan), 7)]

        self.plan_df = pd.DataFrame(weekly, columns=week_list)
        self.plan_df['Week'] = list(range(1, len(weekly) + 1))
        self.plan_df.set_index('Week', inplace=True)

        print(self.plan_df)

    def days_of_week_to_read(self, read=(1, 2, 3, 4, 5, 6, 7), not_read=None):
        """
        Sets days of week to read, or not read
        
        Parameters
        ----------
        read : list (int)
            days of week to read, default is all days, 1 is Monday, etc
        
        not_read : list (int)
            days of week to not read, will override read if both sent     
        
        Return
        ------
        None
        """
        if not_read is not None:
            not_read = icdatetime.day_to_int(not_read)
            for day in not_read:
                    self.days_of_week_to_read_.remove(day)
        else:
            self.days_of_week_to_read_ = list(read)

    def count_b(self):
        """
        Count of books in plan
        
        Return
        ------
        int
        """
        return len(self.plan.books_in_plan(self.plan_id))

    def count_c(self):
        """
        Count of chapters in plan
        
        Return
        ------
        int 
        """
        count = 0
        for book in self.plan.books_in_plan(self.plan_id):
            count += self.plan.chapters_in_book(book)
        return count

if __name__ == '__main__':
    reading_plan = ReadingPlan()
    pt = input("Enter Plan type: ")
    if pt == '':
        pt = 'alpha_omega'

    time_type = None
    while time_type not in ['day', 'week']:
        time_type = input("by day or week: ")
        # time_type = 'week' if time_type == '' else None
        if time_type == '':
            time_type = 'day'
        else:
            time_type = None

    days = input("Enter Plan Length: ")
    if days == 0 or days == '':
        days = 365

    start = input("Day of week to start Plan: ")
    if start == '':
        start = 2
    start = icdatetime.day_to_int(start)

    days_to_not_read = input('Enter days of week to not read, separated by comma [M, TU, W, TH, F, SA, SU]')
    if days_to_not_read != '':
        days_to_not_read = days_to_not_read.split(',')
    else:
        days_to_not_read = 'Sunday'

    reading_plan.define_reading_plan(plan_id=pt, day_count=days, not_read=days_to_not_read, start_day=start)

