## All details workflow of this project:

### Class Details
```mermaid
classDiagram
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
	Word_Seperator <|-- CSV_File_To_List

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
	Pronoun_Finder <|-- CSV_File_To_List

	class Conjunction_Finder {
		+str conjunction_lst_file
		+List[] conjunctions
		+List[] word_pos
		+__init__ ():
		+init_conjunctions ():
		+mark_conjunctions ():
		+__repr__ ():
	}
	Conjunction_Finder <|-- CSV_File_To_List

	Word_POS_List --* Word_Pos_List_Structure

	class Run {
		+Obj Sentence
		+Obj word_seperator
		+Obj word_pos_list
		+Obj pronoun_finder
		+Obj conjunction_finder
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
		F0[[init_pronouns]]
		F1[[mark_pronouns]]
		F --> F0
		F --> F1
	end

	subgraph Conjunction_Finder
		G[[Conjunction_Finder]]
		G0[[init_conjunctions]]
		G1[[mark_conjunctions]]
		G --> G0
		G --> G1
	end

	subgraph Run
		subgraph Run_Elements
			AA[[Run::Sentence]]
			AB[[Run::word_seperator]]
			AC[[Run::word_pos_list]]
			AD[[Run::pronoun_finder]]
			AE[[Run::conjunction_finder]]
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
```
