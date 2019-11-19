from pyresparser import ResumeParser
import urllib.request
from urllib.parse import urljoin
from os.path import splitext
from pathlib import Path
import json
# url = "https://ls-uploads-development.s3.amazonaws.com/cvs/wiXAbEE9aQxp-2b18355c-a8b1-4a24-b56d-d9aaae656d8a-cv.pdf"
# urllib.request.urlretrieve(url, './compiled')
# path = Path("https://ls-uploads-development.s3.amazonaws.com/cvs/mvXq0itdUvff-2b18355c-a8b1-4a24-b56d-d9aaae656d8a-cv.docx")
# path.name
# print(path.name)

file_path = "https://ls-uploads-development.s3.amazonaws.com/cvs/CbbABvtJNNAF-2461b7ba-cdfc-4eb8-b19b-e021626c4f0b-cv.pdf"
file_ext = f".{file_path.split('.')[-1]}"
print(file_ext)
# a = '.pdf'
# if(file_ext == 'pdf')
# {
#     print('PDF file detected' + file_ext)
# }
# else:
#     print('File extention is' + file_ext)

data = urllib.request.urlopen(file_path)

print('data received', data)

datatoWrite = data.read()

with open('./Parse.pdf', 'wb') as f:
    f.write(datatoWrite)
# print('data', data)
# def download_the_file(file_url)
# from nltk from stop
dataParse = ResumeParser('./Parse.pdf').get_extracted_data()
print('data', dataParse)

# datatoWrite = dataParse.read()

with open('ProfessionaResume.txt', 'w') as outfile:
    json.dump(dataParse, outfile, sort_keys=True, indent=4)