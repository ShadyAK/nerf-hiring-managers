from pyresparser import ResumeParser
import nltk 
nltk.download('stopwords')
data = ResumeParser('/Users/shady/Downloads/ASHWIN KAURAV_resume.pdf').get_extracted_data()

# Load English language model for spaCy
#nlp = spacy.load("en_core_web_sm")

# Open the PDF file in read binary mode
'''pdf_file = open("/Users/shady/Downloads/ASHWIN KAURAV_resume.pdf", "rb")

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from all pages of the PDF file
resume_text = ""
for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    resume_text += page.extract_text()

# Process the text with spaCy
doc = nlp(resume_text)

# Extract skills and experience
skills = []
experience = []
print(doc.ents)
for ent in doc.ents:
    if ent.label_ == "SKILL":
        skills.append(ent.text)
    elif ent.label_ == "TECHNICAL SKILLS":
        experience.append(ent.text)

# Print the results
print("Skills:", skills)
print("Experience:", experience)'''
print(data)