# Questions:
	* the characters of the phrase ? random ? 
	* text bolb : extract noun ? or noun + phrase ? 
	* wordnet : how to compare ? 



# Notes:
1. sepeate the paragraph
	* \r\p
	* whitespace in tail of line 
	* whitespace in next line 


2. for every sentence
	* give an index
	* divide by category based on language (azure API / stop words check)
	* 

3. nlp preparetions:
	* remove all punctuation.
	* remove all digits
	* case fold
	* extract and token phrase & remove (avoid duplicated)
	* tokenize -> words & phrase
	* stemming (if needs index for every words ?) : no -> get top N, do stemming again in get the index of the tokenization ?
	* get top 2N frequent words
	* for these 2N words, calcuate the value in wordsnet
	(one word has two digit value now)
	* get the top N based on weight
	* by index -> phrase 
	* find the detailed place in the sentence


4. how to recognise the phrase 
	* text blob - python
	