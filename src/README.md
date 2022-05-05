## All details workflow of this project:

### Class Details
```mermaid
classDiagram
	class Run {
		+Obj Sentence
		+Obj word_seperator
		+Obj word_pos_list
		+Obj pronoun_finder
		+Obj conjunction_finder
	}

	class Sentence_Scanner {
		+str sentence
		+__init__ ()
		+get_input ()
		+__repr__ ()
	}
	class Word_Seperator {
		+str filename
		+str sentence
		+List[] Words
		+List[] punctuations
		+__init__ ()
		+init_punctuations ()
		+seperate_words ()
		+__repr__ ()
	}
	CSV_File_To_List <|-- Word_Seperator

	class Word_POS_List {
		+str word
		+List[] pos_list
		+__init__ ()
		+__repr__ ()
	}
	class Word_Pos_List_Structure {
		+List[] word_pos
		+__init__ ()
		+create_word_pos_list ()
		+__repr__ ()
	}
	class Pronoun_Finder {
		+str filename
		+List[] word_pos
		+List[] pronouns
		+__init__ ()
		+init_pronouns ()
		+mark_pronouns ()
		+__repr__ ()
	}
	CSV_File_To_List <|-- Pronoun_Finder
	Tag_Using_Word_List <|-- Pronoun_Finder

	class Conjunction_Finder {
		+str conjunction_lst_file
		+List[] conjunctions
		+List[] word_pos
		+__init__ ():
		+init_conjunctions ():
		+mark_conjunctions ():
		+__repr__ ():
	}
	CSV_File_To_List <|-- Conjunction_Finder
	Tag_Using_Word_List <|-- Conjunction_Finder

	class Interrogative_Finder {
		+str interrogative_lst_file
		+List[] interrogatives
		+List[] word_pos
		+__init__ ():
		+mark_interrogatives ():
		+__repr__ ():
	}
	CSV_File_To_List <|-- Interrogative_Finder
	Tag_Using_Word_List <|-- Interrogative_Finder

	class Negative_Finder {
		str negative_lst_file
		List[] negatives
		List[] word_pos
		+__init__ ():
		+mark_negatives ():
		+__repr__ ():
	}
	CSV_File_To_List <|-- Negative_Finder
	Tag_Using_Word_List <|-- Negative_Finder

	Word_POS_List --* Word_Pos_List_Structure


	class Tag_Using_Word_List {
		+__init__ ():
		+tag_using_word_list ():
	}

	class CSV_File_To_List {
		+__init__ ()
		+file_to_list ():
	}

	class tagset {
		<<enumeration>>
		NN = 'Noun'
		CND = 'Conditional'
		CNJ = 'Conjunction'
		POP = 'Postposition'
		DIS = 'Disjunction'
		NEG = 'Negative particle'
		ING = 'Interrogative particle'
		VF = 'Finite verb'
		QFNUM = 'Quantifier number'
		NV = 'Verbal Noun'
		AV = 'Verbal Adjective'
		AD = 'Adjective'
		ADA = 'Adjective of adjective'
		PP = 'Pronoun'
		PPP = 'Possesive Pronoun'
		SYM = 'Symbol'
		VNF = 'Nonfinite verb'
	}
```

### FlowChar for the Project
```mermaid
flowchart TD
	ST([Start])

	subgraph Sentence_Scanner
		B[/Sentence From Console/]
		C[[Sentence_Scanner]]
		B --> C
	end
	
	subgraph Word_Seperator
		D[[Word_Seperator]]
		D0[[seperate_words]]
		D --> D0
	end

	subgraph Word_Pos_List_Structure
		E[[Word_Pos_List_Structure]]
		E0[[create_word_pos_list]]
		E1[[Word_POS_List]]
		E1 --> E0
		E --> E0
	end

	subgraph Pronoun_Finder
		F[[Pronoun_Finder]]
		F1[[mark_pronouns]]
		F --> F1
	end

	subgraph Conjunction_Finder
		G[[Conjunction_Finder]]
		G1[[mark_conjunctions]]
		G --> G1
	end

	subgraph Conditional_Finder
		H[[Conditional_Finder]]
		H1[[mark_conditionals]]
		H --> H1
	end

	subgraph Interrogative_Finder
		I[[Interrogative_Finder]]
		I1[[mark_interrogatives]]
		I --> I1
	end

	subgraph Negative_Finder
		NF[[Negative_Finder]]
		NF1[[mark_negatives]]
		NF --> NF1
	end

	subgraph Run
		subgraph Run_Elements
			AA[[Run::Sentence]]
			AB[[Run::word_seperator]]
			AC[[Run::word_pos_list]]
			AD[[Run::pronoun_finder]]
			AE[[Run::conjunction_finder]]
			AF[[Run::conditional_finder]]
			AG[[Run::interrogative_finder]]
			AH[[Run::negative_finder]]
		end
	end

	ST --> Run

	Sentence_Scanner -- Object --> AA
	AA -- Sentence.sentence --> Word_Seperator
	Word_Seperator -- Object --> AB
	AB -- word_seperator.words --> Word_Pos_List_Structure
	Word_Pos_List_Structure -- Object --> AC
	AC -- word_pos_list.word_pos --> Pronoun_Finder
	Pronoun_Finder -- Object --> AD
	AD -- pronoun_finder.word_pos --> Conjunction_Finder
	Conjunction_Finder -- Object --> AE
	AE -- conjunction_finder.word_pos --> Conditional_Finder
	Conditional_Finder -- Object --> AF
	AF -- conditional_finder.word_pos --> Interrogative_Finder
	Interrogative_Finder -- Object --> AG
	AG -- interrogative_finder.word_pos --> Negative_Finder
	Negative_Finder -- Object --> AH
```
