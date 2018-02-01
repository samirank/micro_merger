import os
from PyPDF2 import PdfFileMerger
from progress import progress


os.system('cls')


dir_path = os.path.dirname(os.path.realpath(__file__))
files=os.listdir(dir_path)
pdfs =[]
for pdf in files:
	if pdf.lower().endswith('.pdf'):
		pdfs.append(pdf)

print('\nFound '+str(len(pdfs))+' files to merge')



def merge(pdfs,dir_path):
	print('\nMerging pdf files in '+dir_path)
	total=len(pdfs)
	i=0
	msg='merging'
	progress(i, total, status='msg')
	merger = PdfFileMerger(strict = False)

	for pdf in pdfs:
		msg = 'merging .....'+str(i+1)+'/'+str(total)
		progress(i, total, status=msg)
		try:
			merger.append(dir_path+'\\'+pdf)
		except Exception as e:
			pass
		i+=1
	merged_file_name = 'merged'
	j=1
	while os.path.exists(dir_path+'\\'+merged_file_name+'.pdf'):
		merged_file_name=merged_file_name.replace(str(j-1),'')
		merged_file_name=merged_file_name+str(j)
		j+=1
	merger.write(merged_file_name+'.pdf')
	progress(i, total, status=msg)
	print('\n merge successfully completed\n')
	print('\nyour file is saved as:')
	print('\nFilename:\t'+merged_file_name+'.pdf')
	print('\nfile path:\t'dir_path)

merge(pdfs,dir_path)