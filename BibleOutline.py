class BibleOutline(object):

    bible_outline = {'Genesis':          {'abbr': 'Gen', 'chapters': 50, 't': 'OT', 'order': 1},
                     'Exodus':           {'abbr': 'Ex', 'chapters': 40, 't': 'OT', 'order': 2},
                     'Leviticus':        {'abbr': 'Lev', 'chapters': 27, 't': 'OT', 'order': 3},
                     'Numbers':          {'abbr': 'Num', 'chapters': 36, 't': 'OT', 'order': 4},
                     'Deuteronomy':      {'abbr': 'Deut', 'chapters': 34, 't': 'OT', 'order': 5},
                     'Joshua':           {'abbr': 'Josh', 'chapters': 24, 't': 'OT', 'order': 6},
                     'Judges':           {'abbr': 'Jdg', 'chapters': 21, 't': 'OT', 'order': 7},
                     'Ruth':             {'abbr': 'Ruth', 'chapters': 4, 't': 'OT', 'order': 8},
                     '1 Samuel':         {'abbr': '1 Sam', 'chapters': 31, 't': 'OT', 'order': 9},
                     '2 Samuel':         {'abbr': '2 Sam', 'chapters': 24, 't': 'OT', 'order': 10},
                     '1 Kings':          {'abbr': '1 King', 'chapters': 22, 't': 'OT', 'order': 11},
                     '2 Kings':          {'abbr': '2 King', 'chapters': 25, 't': 'OT', 'order': 12},
                     '1 Chronicles':     {'abbr': '1 Chr', 'chapters': 29, 't': 'OT', 'order': 13},
                     '2 Chronicles':     {'abbr': '2 Chr', 'chapters': 36, 't': 'OT', 'order': 14},
                     'Ezra':             {'abbr': 'Ezr', 'chapters': 10, 't': 'OT', 'order': 1},
                     'Nehemiah':         {'abbr': 'Neh', 'chapters': 13, 't': 'OT', 'order': 1},
                     'Esther':           {'abbr': 'Est', 'chapters': 10, 't': 'OT', 'order': 1},
                     'Job':              {'abbr': 'Job', 'chapters': 42, 't': 'OT', 'order': 1},
                     'Psalms':           {'abbr': 'Psa', 'chapters': 150, 't': 'OT', 'order': 1},
                     'Proverbs':         {'abbr': 'Prov', 'chapters': 31, 't': 'OT', 'order': 1},
                     'Ecclesiastes':     {'abbr': 'Ecc', 'chapters': 12, 't': 'OT', 'order': 1},
                     'Song of Songs':    {'abbr': 'Song', 'chapters': 8, 't': 'OT', 'order': 1},
                     'Lamentation':      {'abbr': 'Lam', 'chapters': 5, 't': 'OT', 'order': 1},
                     'Isaiah':           {'abbr': 'Isa', 'chapters': 66, 't': 'OT', 'order': 1},
                     'Jeremiah':         {'abbr': 'Jer', 'chapters': 52, 't': 'OT', 'order': 1},
                     'Ezekiel':          {'abbr': 'Eze', 'chapters': 48, 't': 'OT', 'order': 1},
                     'Daniel':           {'abbr': 'Dan', 'chapters': 12, 't': 'OT', 'order': 1},
                     'Hosea':            {'abbr': 'Hos', 'chapters': 14, 't': 'OT', 'order': 1},
                     'Joel':             {'abbr': 'Joel', 'chapters': 3, 't': 'OT', 'order': 1},
                     'Amos':             {'abbr': 'Amos', 'chapters': 9, 't': 'OT', 'order': 1},
                     'Obadiah':          {'abbr': 'Ob', 'chapters': 1, 't': 'OT', 'order': 1},
                     'Jonah':            {'abbr': 'Jon', 'chapters': 4, 't': 'OT', 'order': 1},
                     'Micah':            {'abbr': 'Mic', 'chapters': 7, 't': 'OT', 'order': 1},
                     'Nahum':            {'abbr': 'Nah', 'chapters': 3, 't': 'OT', 'order': 1},
                     'Habakkuk':         {'abbr': 'Hab', 'chapters': 3, 't': 'OT', 'order': 1},
                     'Zephaniah':        {'abbr': 'Zep', 'chapters': 3, 't': 'OT', 'order': 1},
                     'Haggai':           {'abbr': 'Hag', 'chapters': 2, 't': 'OT', 'order': 1},
                     'Zechariah':        {'abbr': 'Zec', 'chapters': 14, 't': 'OT', 'order': 1},
                     'Malachi':          {'abbr': 'Mal', 'chapters': 4, 't': 'OT', 'order': 1},
                     'Matthew':          {'abbr': 'Matt', 'chapters': 28, 't': 'NT', 'order': 1},
                     'Mark':             {'abbr': 'Mrk', 'chapters': 16, 't': 'NT', 'order': 1},
                     'Luke':             {'abbr': 'Luke', 'chapters': 24, 't': 'NT', 'order': 1},
                     'John':             {'abbr': 'John', 'chapters': 21, 't': 'NT', 'order': 1},
                     'Acts':             {'abbr': 'Acts', 'chapters': 28, 't': 'NT', 'order': 1},
                     'Romans':           {'abbr': 'Rom', 'chapters': 16, 't': 'NT', 'order': 1},
                     '1 Corinthians':    {'abbr': '1 Cor', 'chapters': 16, 't': 'NT', 'order': 1},
                     '2 Corinthians':    {'abbr': '2 Cor', 'chapters': 13, 't': 'NT', 'order': 1},
                     'Galatians':        {'abbr': 'Gal', 'chapters': 6, 't': 'NT', 'order': 1},
                     'Ephesians':        {'abbr': 'Eph', 'chapters': 6, 't': 'NT', 'order': 1},
                     'Philippians':      {'abbr': 'Php', 'chapters': 4, 't': 'NT', 'order': 1},
                     'Colossians':       {'abbr': 'Col', 'chapters': 4, 't': 'NT', 'order': 1},
                     '1 Thessalonians':  {'abbr': '1 Th', 'chapters': 5, 't': 'NT', 'order': 1},
                     '2 Thessalonians':  {'abbr': '2 Th', 'chapters': 3, 't': 'NT', 'order': 1},
                     '1 Timothy':        {'abbr': '1 Tim', 'chapters': 6, 't': 'NT', 'order': 1},
                     '2 Timothy':        {'abbr': '2 Tim', 'chapters': 4, 't': 'NT', 'order': 1},
                     'Titus':            {'abbr': 'Tit', 'chapters': 3, 't': 'NT', 'order': 1},
                     'Philemon':         {'abbr': 'Phm', 'chapters': 1, 't': 'NT', 'order': 1},
                     'Hebrews':          {'abbr': 'Heb', 'chapters': 13, 't': 'NT', 'order': 1},
                     'James':            {'abbr': 'Jam', 'chapters': 5, 't': 'NT', 'order': 1},
                     '1 Peter':          {'abbr': '1 Pet', 'chapters': 5, 't': 'NT', 'order': 1},
                     '2 Peter':          {'abbr': '2 Pet', 'chapters': 3, 't': 'NT', 'order': 1},
                     '1 John':           {'abbr': '1 Jhn', 'chapters': 5, 't': 'NT', 'order': 1},
                     '2 John':           {'abbr': '2 Jhn', 'chapters': 1, 't': 'NT', 'order': 1},
                     '3 John':           {'abbr': '3 Jhn', 'chapters': 1, 't': 'NT', 'order': 1},
                     'Jude':             {'abbr': 'Jud', 'chapters': 1, 't': 'NT', 'order': 1},
                     'Revelation':       {'abbr': 'Rev', 'chapters': 22, 't': 'NT', 'order': 1}}

    reading_plan_books_ = {'alpha_omega': ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua',
                                           'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings',
                                           '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms',
                                           'Proverbs', 'Ecclesiastes', 'Song of Songs', 'Lamentation', 'Isaiah',
                                           'Jeremiah', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah',
                                           'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi',
                                           'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians',
                                           '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians',
                                           '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus',
                                           'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John',
                                           '3 John', 'Jude', 'Revelation'],
                           'chronological': [],
                           'big_five': [],
                           'old_testament': [],
                           'new_testament': []}

    def __init__(self, plan_type='alpha_omega'):
        super().__init__()
        self.plan_type = plan_type
        self.reading_list_ = []

        for book in self.reading_plan_books_[self.plan_type]:
            for chapter in range(1, self.bible_outline[book]['chapters'] + 1):
                self.reading_list_.append((book, chapter))

    def reading_list(self):
        return self.reading_list_

    def books_in_plan(self, plan_name):
        return self.reading_plan_books_[plan_name]

    def chapters_in_book(self, title):
        return self.bible_outline[title]['chapters']


