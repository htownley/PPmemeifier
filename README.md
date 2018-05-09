# the-privacy-policy-memeifier

The NLP techniques employed by both programs are rudimentary. More significant is the amount of information these programs can quickly uncover about the privacy policies they are given despite the simplicity of the code. It would seem all to easy for a large tech company to conduct an even more sophisticated effort to create a privacy policy that is intuitive and engaging for all

|-----------------------------|
|   report_policy_parser.py   |
|-----------------------------|

REQUIREMENTS and INSTALLATION:
	- Python 3.6
	- Packages:
		- To install the necessary packages one can this pip command:
		- "pip install urllib3, certifi, bs4, textwrap, requests"


SUMMMARY:
report_policy_parser.py reads a given privacy policy (either online or in a textfile). Given this privacy policy the program than runs two tests. 

The "collect_test" parses through every sentence of the policy to determine whether or not there are sentences that suggest some kind of personal data is being collected (or explicitly not collected) by the company or organization.

the "third_party_test" parses through every sentence of the policy to determine whether or not there are sentences that suggest some kind of personal data is being collected by the company or organization.

The program summarizes the results from both of these tests in an html report which will appear in the folder at the conclusion of the program. This report can be opened in your browser by double clicking it.



|------------------------------|
| interactive_policy_parser.py |
|------------------------------|

REQUIREMENTS and INSTALLATION:
	- Python 3.6
	- Packages:
		- All packages from previous program must be installed
		  in addition to "gensim" (below)
		- "pip install gensim"
	- Download Google word2vec model
		- Download the file from this url: "https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing"
		- Drag it into the same folder as interactive_policy_parser.py 
		- Double click to unzip (on a mac at least)

SUMMMARY:
interactive_policy_parser.py allows you to search throught the privacy policy for sentences of interest. When you provide a keyword, the program transforms the word into its word2vec vector representation and expands the keyword query set to a list of 30 words most similiar to the keyword provided (as judged by the word2vec model). All the sentences are then searched for references to any word in this set.


