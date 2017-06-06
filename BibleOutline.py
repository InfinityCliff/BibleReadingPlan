import operator


class Bible_Outline(object):

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
                     'Ezra':             {'abbr': 'Ezr', 'chapters': 10, 't': 'OT', 'order': 15},
                     'Nehemiah':         {'abbr': 'Neh', 'chapters': 13, 't': 'OT', 'order': 16},
                     'Esther':           {'abbr': 'Est', 'chapters': 10, 't': 'OT', 'order': 17},
                     'Job':              {'abbr': 'Job', 'chapters': 42, 't': 'OT', 'order': 18},
                     'Psalms':           {'abbr': 'Psa', 'chapters': 150, 't': 'OT', 'order': 19},
                     'Proverbs':         {'abbr': 'Prov', 'chapters': 31, 't': 'OT', 'order': 20},
                     'Ecclesiastes':     {'abbr': 'Ecc', 'chapters': 12, 't': 'OT', 'order': 21},
                     'Song of Songs':    {'abbr': 'Song', 'chapters': 8, 't': 'OT', 'order': 22},
                     'Lamentation':      {'abbr': 'Lam', 'chapters': 5, 't': 'OT', 'order': 23},
                     'Isaiah':           {'abbr': 'Isa', 'chapters': 66, 't': 'OT', 'order': 24},
                     'Jeremiah':         {'abbr': 'Jer', 'chapters': 52, 't': 'OT', 'order': 25},
                     'Ezekiel':          {'abbr': 'Eze', 'chapters': 48, 't': 'OT', 'order': 26},
                     'Daniel':           {'abbr': 'Dan', 'chapters': 12, 't': 'OT', 'order': 27},
                     'Hosea':            {'abbr': 'Hos', 'chapters': 14, 't': 'OT', 'order': 28},
                     'Joel':             {'abbr': 'Joel', 'chapters': 3, 't': 'OT', 'order': 29},
                     'Amos':             {'abbr': 'Amos', 'chapters': 9, 't': 'OT', 'order': 30},
                     'Obadiah':          {'abbr': 'Ob', 'chapters': 1, 't': 'OT', 'order': 31},
                     'Jonah':            {'abbr': 'Jon', 'chapters': 4, 't': 'OT', 'order': 32},
                     'Micah':            {'abbr': 'Mic', 'chapters': 7, 't': 'OT', 'order': 33},
                     'Nahum':            {'abbr': 'Nah', 'chapters': 3, 't': 'OT', 'order': 34},
                     'Habakkuk':         {'abbr': 'Hab', 'chapters': 3, 't': 'OT', 'order': 35},
                     'Zephaniah':        {'abbr': 'Zep', 'chapters': 3, 't': 'OT', 'order': 36},
                     'Haggai':           {'abbr': 'Hag', 'chapters': 2, 't': 'OT', 'order': 37},
                     'Zechariah':        {'abbr': 'Zec', 'chapters': 14, 't': 'OT', 'order': 38},
                     'Malachi':          {'abbr': 'Mal', 'chapters': 4, 't': 'OT', 'order': 39},
                     'Matthew':          {'abbr': 'Matt', 'chapters': 28, 't': 'NT', 'order': 40},
                     'Mark':             {'abbr': 'Mrk', 'chapters': 16, 't': 'NT', 'order': 41},
                     'Luke':             {'abbr': 'Luke', 'chapters': 24, 't': 'NT', 'order': 42},
                     'John':             {'abbr': 'John', 'chapters': 21, 't': 'NT', 'order': 43},
                     'Acts':             {'abbr': 'Acts', 'chapters': 28, 't': 'NT', 'order': 44},
                     'Romans':           {'abbr': 'Rom', 'chapters': 16, 't': 'NT', 'order': 45},
                     '1 Corinthians':    {'abbr': '1 Cor', 'chapters': 16, 't': 'NT', 'order': 46},
                     '2 Corinthians':    {'abbr': '2 Cor', 'chapters': 13, 't': 'NT', 'order': 47},
                     'Galatians':        {'abbr': 'Gal', 'chapters': 6, 't': 'NT', 'order': 48},
                     'Ephesians':        {'abbr': 'Eph', 'chapters': 6, 't': 'NT', 'order': 49},
                     'Philippians':      {'abbr': 'Php', 'chapters': 4, 't': 'NT', 'order': 50},
                     'Colossians':       {'abbr': 'Col', 'chapters': 4, 't': 'NT', 'order': 51},
                     '1 Thessalonians':  {'abbr': '1 Th', 'chapters': 5, 't': 'NT', 'order': 52},
                     '2 Thessalonians':  {'abbr': '2 Th', 'chapters': 3, 't': 'NT', 'order': 53},
                     '1 Timothy':        {'abbr': '1 Tim', 'chapters': 6, 't': 'NT', 'order': 54},
                     '2 Timothy':        {'abbr': '2 Tim', 'chapters': 4, 't': 'NT', 'order': 55},
                     'Titus':            {'abbr': 'Tit', 'chapters': 3, 't': 'NT', 'order': 56},
                     'Philemon':         {'abbr': 'Phm', 'chapters': 1, 't': 'NT', 'order': 57},
                     'Hebrews':          {'abbr': 'Heb', 'chapters': 13, 't': 'NT', 'order': 58},
                     'James':            {'abbr': 'Jam', 'chapters': 5, 't': 'NT', 'order': 59},
                     '1 Peter':          {'abbr': '1 Pet', 'chapters': 5, 't': 'NT', 'order': 60},
                     '2 Peter':          {'abbr': '2 Pet', 'chapters': 3, 't': 'NT', 'order': 61},
                     '1 John':           {'abbr': '1 Jhn', 'chapters': 5, 't': 'NT', 'order': 62},
                     '2 John':           {'abbr': '2 Jhn', 'chapters': 1, 't': 'NT', 'order': 63},
                     '3 John':           {'abbr': '3 Jhn', 'chapters': 1, 't': 'NT', 'order': 64},
                     'Jude':             {'abbr': 'Jud', 'chapters': 1, 't': 'NT', 'order': 65},
                     'Revelation':       {'abbr': 'Rev', 'chapters': 22, 't': 'NT', 'order': 66}}

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

    def ot_books(self):
        return {k: v for k, v in self.bible_outline.items() if v['t'] == 'OT'}

    def nt_books(self):
        return {k: v for k, v in self.bible_outline.items() if v['t'] == 'NT'}

    def sorted_book_abbr(self, book_list=None):
        if book_list is None:
            book_list = self.bible_outline
        elif book_list == 'OT':
            book_list = self.ot_books()
        elif book_list == 'NT':
            book_list = self.nt_books()
        else:
            raise ValueError("{} is not valid book list".format(book_list))

        unsorted_books_abbr = [(v['abbr'], v['order']) for k, v in book_list.items()]
        return sorted(unsorted_books_abbr, key=operator.itemgetter(1))

