package com.crossway.biblereadingplan.products;
//TODO need to finish out the mundane comments at the end of this
//TODO delete deprecated methods and variables if not needed

/**
 * Represents each book of the Bible.
 *
 */
public class BibleBook {

	//FIELDS
	/**
	 * Name of Bible book.
	 */
	private String name = "unnamed";
	/**
	 * Abbreviation of Bible book.
	 */
	private String abbr = "unnamed";
	/**
	 * Current chapter, used when building plan.
	 */
	private int currentChapter = 1;
	/**
	 * Last chapter or total number of chapters in book.
	 */
	private int lastChapter;
	/**
	 * Number of day the book is being read
	 * @deprecated should not be in use when building plan, replaced by bweekarray
	 */
	private int daysreading = 7;
	/**
	 * Number of days book is being read
	 * @deprecated should be replaced by chaptersPerDay in ReadingPlan.java
	 */
	private Integer[] bweekarray = {0, 0, 0, 0, 0, 0, 0};
	/**
	 * True if the book is being read, set to false when build plan gets to last chapter.  
	 * This is trigger to jump to next book. 
	 */
	private boolean isReading = true;
	/**
	 * True if the book is being read on Sunday.
	 */
	private boolean sunday = true;
	/**
	 * True if the book is being read on Monday.
	 */
	private boolean monday = true;
	/**
	 * True if the book is being read on Tuesday.
	 */
	private boolean tuesday = true;
	/**
	 * True if the book is being read on Wednesday.
	 */
	private boolean wednesday = true;
	/**
	 * True if the book is being read on Thursday.
	 */
	private boolean thursday = true;
	/**
	 * True if the book is being read on Friday.
	 */
	private boolean friday = true;
	/**
	 * True if the book is being read on Saturday.
	 */
	private boolean saturday = true;

	
	//CONSTRUCTOR
	/**
	 * Defaults book to being read on all days.
	 * @param name Name of Book.
	 * @param abbr Abbreviation of book.
	 * @param lastChapter Last chapter of book.
	 */
	public BibleBook (String name, String abbr, int lastChapter) {
		this.name = name;
		this.abbr = abbr;
		this.lastChapter = lastChapter;
		this.sunday = true; 
		this.monday = true;
		this.tuesday = true;
		this.wednesday = true;
		this.thursday = true;
		this.friday = true;
		this.saturday = true;
	} // end constructor 1 of book

	
	/**
	 * Allows creation of book with days not being read.
	 * @param name Name of Book.
	 * @param abbr Abbreviation of book.
	 * @param lastChapter Last chapter of book.
	 * @param sun True if reading on Sunday.
	 * @param mon True if reading on Monday.
	 * @param tue True if reading on Tuesday.
	 * @param wed True if reading on Wednesday.
	 * @param thu True if reading on Thursday.
	 * @param fri True if reading on Friday.
	 * @param sat True if reading on Saturday.
	 */
	public BibleBook (String name, String abbr, int lastChapter,
						     boolean sun, boolean mon, boolean tue, boolean wed,
						     boolean thu, boolean fri, boolean sat) {
		this.name = name;
		this.abbr = abbr;
		this.lastChapter = lastChapter;
		this.monday = mon;
		this.tuesday = tue;
		this.wednesday = wed;
		this.thursday = thu;
		this.friday = fri;
		this.saturday = sat;
		this.sunday = sun;
	} // end constructor 2 book

	
	//METHODS
	/**
	 * Resets the currentChapter to one and isReading to true.
	 */
	public void reset(){
		currentChapter = 1;
		isReading = true;
	} //reset
	
	/**
	 * Move chapter pointer to next chapter
	 */
	public void nextChapter(){
		setCurrentChapter(currentChapter + 1);
	} //end Next

	//GETTERS AND SETTERS
	/**
	 * @return Name of book 
	 */
	public String getName() {
		return name;
	}
	/**
	 * Sets the name of the book to String provided
	 * @param name Name of book
	 */
	public void setName(String name) {
		this.name = name;
	}

	/**
	 * @return Abbreviation of book
	 */
	public String getAbbr() {
		return abbr;
	}

	/**
	 * Sets the abbreviation of the book
	 * @param abbr Abbreviation of the book
	 */
	public void setAbbr(String abbr) {
		this.abbr = abbr;
	}

	public int getCurrentChapter() {
		return currentChapter;
	}

	public void setCurrentChapter(int currentChapter) {
		this.currentChapter = currentChapter;
	}

	public int getLastChapter() {
		return lastChapter;
	}

	public void setLastChapter(int lastChapter) {
		this.lastChapter = lastChapter;
	}

	/**
	 * @return the daysreading
	 */
	public int getDaysreading() {
		return daysreading;
	}

	/**
	 * Decrements the number of days on which the book is being read if read is false
	 * @param read boolean. False is not reading book on day.
	 */
//	public void decDaysreading(boolean read) {
//		if (!read) {
//			this.daysreading--;
//		}
//	}

	/**
	 * @param ordinal of value requested from array
	 * @return the bweekarray
	 */
	public int getBweekarray(int ordinal) {
		return bweekarray[ordinal];
	}

	/**
	 * @param bweekarray the bweekarray to set
	 */
	public void setBweekarray(Integer[] bweekarray) {
		this.bweekarray = bweekarray;
	}
	
	/**
	 * @param ordinal which array member to set value to 
	 * @param value to set in bweekarray
	 */
	public void setBweekarray(int ordinal, int value) {
		this.bweekarray[ordinal] = value;
	}
	
	/**
	 * Returns true if the book is being read on day of week passed to method
	 * @param dayOfWeek Current day of week
	 * @return true if the book is being read on the provided day, otherwise false
	 */
	public boolean isReadingOnDay(int dayOfWeek) {
		switch (dayOfWeek) {
		case 1:
			return sunday;
		case 2:
			return monday;
		case 3:
			return tuesday;
		case 4:
			return wednesday;
		case 5:
			return thursday;
		case 6:
			return friday;
		case 7:
			return saturday;
		default:
			return false;
		} //switch (dayOfWeek)
	} //isReadingOnDay
	
	/**
	 * @param day day to change
	 * @param value value to change respective day to
	 */
	public void setDay(String day, boolean value){
		switch (day) {
		case "SUNDAY":
			setSunday(value);
			break;
		case "MONDAY":
			setMonday(value);
			break;
		case "TUESDAY":
			setTuesday(value);
			break;
		case "WEDNESDAY":
			setWednesday(value);
			break;
		case "THURSDAY":
			setThursday(value);
			break;
		case "FRIDAY":
			setFriday(value);
			break;
		case "SATURDAY":
			setSaturday(value);
			break;
		default:
			break;
		}
	}
	
	public boolean isReading() {
		return isReading;
	}

	public void setReading(boolean isReading) {
		this.isReading = isReading;
	}

	public boolean isMonday() {
		return monday;
	}

	public void setMonday(boolean monday) {
		this.monday = monday;
	}

	public boolean isTuesday() {
		return tuesday;
	}

	public void setTuesday(boolean tuesday) {
		this.tuesday = tuesday;
	}

	public boolean isWednesday() {
		return wednesday;
	}

	public void setWednesday(boolean wednesday) {
		this.wednesday = wednesday;
	}

	public boolean isThursday() {
		return thursday;
	}

	public void setThursday(boolean thursday) {
		this.thursday = thursday;
	}

	public boolean isFriday() {
		return friday;
	}

	public void setFriday(boolean friday) {
		this.friday = friday;
	}

	public boolean isSaturday() {
		return saturday;
	}

	public void setSaturday(boolean saturday) {
		this.saturday = saturday;
	}

	public boolean isSunday() {
		return sunday;
	}

	public void setSunday(boolean sunday) {
		this.sunday = sunday;
	}
} //end class Book