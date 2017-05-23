package com.crossway.biblereadingplan.products;

/**
 * This is the Bible.  Contains a static array of BibleBook for each book in bible.  
 * Build each book with the full name, abbreviation and number of chapters as initial fields.  
 * <i>Note:</i> Lamentation is out of order to allow it to be grouped with the Wisdom books.
 */
public class Bible {
	public static BibleBook[] bible = {
	new BibleBook("Genesis", "Gen", 50),
	new BibleBook("Exodus" , "Ex" , 40),
	new BibleBook("Leviticus", "Lev", 27),
	new BibleBook("Numbers", "Num", 36),
	new BibleBook("Deuteronomy", "Deut", 34),
	new BibleBook("Joshua", "Josh", 24),
	new BibleBook("Judges", "Jdg", 21),
	new BibleBook("Ruth", "Ruth", 4),
	new BibleBook("1 Samuel", "1 Sam", 31),
	new BibleBook("2 Samuel", "2 Sam", 24),
	new BibleBook("1 Kings", "1 King", 22),
	new BibleBook("2 Kings", "2 King", 25),
	new BibleBook("1 Chronicles", "1 Chr", 29),
	new BibleBook("2 Chronicles", "2 Chr", 36),
	new BibleBook("Ezra", "Ezr", 10),
	new BibleBook("Nehemiah", "Neh", 13),
	new BibleBook("Esther", "Est", 10),
	new BibleBook("Job", "Job", 42),
	new BibleBook("Psalms", "Psa", 150),
	new BibleBook("Proverbs", "Prov", 31),
	new BibleBook("Ecclesiastes", "Ecc", 12),
	new BibleBook("Song of Songs", "Song", 8),
	new BibleBook("Lamentation", "Lam", 5),
	new BibleBook("Isaiah", "Isa", 66),
	new BibleBook("Jeremiah", "Jer", 52),
	new BibleBook("Ezekiel", "Eze", 48),
	new BibleBook("Daniel", "Dan", 12),
	new BibleBook("Hosea", "Hos", 14),
	new BibleBook("Joel", "Joel", 3),
	new BibleBook("Amos", "Amos", 9),
	new BibleBook("Obadiah", "Ob", 1),
	new BibleBook("Jonah", "Jon", 4),
	new BibleBook("Micah", "Mic", 7),
	new BibleBook("Nahum", "Nah", 3),
	new BibleBook("Habakkuk", "Hab", 3),
	new BibleBook("Zephaniah", "Zep", 3),
	new BibleBook("Haggai", "Hag", 2),
	new BibleBook("Zechariah", "Zec", 14),
	new BibleBook("Malachi", "Mal", 4),
	new BibleBook("Matthew", "Matt", 28),
	new BibleBook("Mark", "Mrk", 16),
	new BibleBook("Luke", "Luke", 24),
	new BibleBook("John", "John", 21),
	new BibleBook("Acts", "Acts", 28),
	new BibleBook("Romans", "Rom", 16),
	new BibleBook("1 Corinthians", "1 Cor", 16),
	new BibleBook("2 Corinthians", "2 Cor", 13),
	new BibleBook("Galatians", "Gal", 6),
	new BibleBook("Ephesians", "Eph", 6),
	new BibleBook("Philippians", "Php", 4),
	new BibleBook("Colossians", "Col", 4),
	new BibleBook("1 Thessalonians", "1 Th", 5),
	new BibleBook("2 Thessalonians", "2 Th", 3),
	new BibleBook("1 Timothy", "1 Tim", 6),
	new BibleBook("2 Timothy", "2 Tim", 4),
	new BibleBook("Titus", "Tit", 3),
	new BibleBook("Philemon", "Phm", 1),
	new BibleBook("Hebrews", "Heb", 13),
	new BibleBook("James", "Jam", 5),
	new BibleBook("1 Peter", "1 Pet", 5),
	new BibleBook("2 Peter", "2 Pet", 3),
	new BibleBook("1 John", "1 Jhn", 5),
	new BibleBook("2 John", "2 Jhn", 1),
	new BibleBook("3 John", "3 Jhn", 1),
	new BibleBook("Jude", "Jud", 1),
	new BibleBook("Revelation", "Rev", 22)};
	
	/**
	 * Returns the BibleBook requested based on its abbreviation.
	 * @param abbr Book abbreviation
	 * @return The BibleBook with the corresponding abbreviation that was passed to the method.  
	 * Returns <b>null</b> if book abbreviation not found.
	 */
	public static BibleBook getBook(String abbr){
		for (BibleBook book : bible) {
			if (book.getAbbr().equals(abbr)) {
				return book;
			} //if (book.getAbbr().equals(abbr))
		} //for (Book book : bible)
		return null;
	} //Book getBook(String abbr){
	
} //end class Bible
