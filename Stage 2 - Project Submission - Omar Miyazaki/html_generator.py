notes = """
TITLE: Introduction
DESCRIPTION: &ltlist&gt -&gt [&ltexpression&gt, &ltexpression&gt,...]
You can add numbers, characters, strings, or list. 
You can create list that are empty and lists with one item. 

TITLE: Nested Lists
DESCRIPTION: You can place lists inside of lists. 
For reading clarity, you can place lists in multiple lines. When separating lines, add the space at the end of a comma. 

TITLE: Summary
DESCRIPTION: Loops are a very useful tool. It has similarities as string but has major advantages. You can Some of these advantages are mutation. By mutating one list you an update the content that it feeds into everywhere. You can also append items to lists and find thing easily using the index procedure."""



concept_list = []
all_titles_n_descripions = []



#Def 1: function to put all concepts in a list
def divide_concepts_to_list(text):
	# loop to add all concepts into a list
	while text != "":
		#location of start and end of concept
		concept_start = text.find("TITLE:")
		concept_end = text.find("TITLE:", concept_start+1) -1
		#if there is no end concept go to the end of string
		if concept_end == -2:
			concept_end = len(text)
		
		#add found concept to list
		ind_concept = text[concept_start: concept_end]
		concept_list.append(ind_concept)

		#removing the selected concept from text
		text = text[concept_end:]
	return concept_list



#Def 2: function to split title and description into lists
def title_description_split(title_n_description):
	for concept_content in title_n_description:
		TITLE_start = concept_content.find("TITLE:") + 7
		TITLE_end = concept_content.find("DESCRIPTION:") - 1
		title_content = concept_content[TITLE_start: TITLE_end]

		#find description 
		DESCRIPTION_start = concept_content.find("DESCRIPTION:") + 13
		description_content = concept_content[DESCRIPTION_start:]

		# put title and description in own list then add all to main list
		ind_list_of_title_n_description = [title_content] + [description_content]
		all_titles_n_descripions.append(ind_list_of_title_n_description)
	return all_titles_n_descripions



#Def 3: function that adds html
def html_structure(list_w_title_n_desctiption):
	html_text = ""
	for n in list_w_title_n_desctiption:
		concept_name = n[0]
		concept_description =n[1]

		#html structure 
		html_ind =  '''
<div class="concept">
	<h3>''' + concept_name + '''</h3>	
	<p>
		''' +	concept_description + '''
	</p>
</div>'''
		
		# add all html together 
		html_text = html_text + html_ind
	return html_text 


#Def 4: Execute all previous functions 
def convert_text_to_html(my_notes):
	divide_concepts_to_list(notes)
	title_description_split(concept_list)
	return html_structure(all_titles_n_descripions)



print convert_text_to_html(notes)