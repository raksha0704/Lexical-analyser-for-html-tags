import re
import sys
#print(sys.argv)
s = ""
f = ""
ip =""
if sys.argv[1] == '1':
	#print("taken from file")
	f = sys.argv[2]
	ip = open(f,'r').readlines()
if sys.argv[1] == '2':
	#print("taken from user")
	s = sys.argv[2]
	ip = [s,]
d = {}
d2 = {}
tagFinalList = []
attFinalList = []
stack = []
lineno = 0
tags=["body","html","title","h1","h2","h3","h4","h5","h6","ul","p","li","link","script","frame","font","i","table","head","tr","td","th",
"textarea","span","form","input","dl","block","video","docType","hr","meta","q","big","a","time","sup","sub"]

attributes = ["class","style","title","value","src","height","width","name","rel","cols","href"]
f2 = open('bugs.txt','w')
f3 = open('no_comments.txt','w')
##f.write(s)


flag = 0
line = 0
for s in ip:

	line += 1
	full = 0
	#print("flag:" ,flag)
	comment = re.findall('<!--.*?-->',s)
	for co in comment:
		s = s.replace(co,'')

	commentC = re.findall('.*?-->',s)
	for co in commentC:
		flag = 0
		s = s.replace(co,'')	

	comment = re.findall('<!--.*',s)
	for co in comment:
		flag = 1
		s = s.replace(co,'')

	
	if commentC == [] and flag:
		#print(s)
		s=""			
	#print(s)	
	f3.write(s)	
	#f3.write("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
f3.close()

F = open('no_comments.txt','r')
li = F.readlines()
for s in li:	
	total=re.findall('<[ ]*[^/][^<>]+>',s)
	#print(total)
	for i in total:
		tag = re.findall('<\w+',i)
		for t in tag:
			t =t.replace('<','').strip()
			#print(t)
			if t in tags:
				#print(tag ,": valid")
				if t in d2.keys():
					d2[t] += 1
				else:
					d2[t] = 1
				tagWithNum = t+str(d2[t])
				if '=' in i:
					#print(i)
					p = re.findall('[\w\-]+[ ]*=[ ]*\"[\w\-/:\.\;0123456789 ]+\"',i)
					for part in p:
						part = part.split('=')
						attname = part[0].strip()
						if attname in attributes:
							val = part[1].strip()
							val = val.replace('"','')
							val = re.split('[ ]+',val)
							for v in val:
								#print(t,attname,v)
								v = v.strip()
								attFinalList.append(( attname,'attribute', v,tagWithNum),)

	
for s in li:
	#print(s)
	lineno += 1
	tagname=re.findall("<[ /]*\w+",s)
	#attname=re.findall("<[ /]*\w+([ ]+\w+[ ]*=[ ]*\"[ ]*\w+[ ]*\")+",s)
	#attrval=re.findall("=[ ]*\"\w+[ ]*\w+\"",s)
	#ctag = re.findall("</\w+",s)
	#print(tagname)
	#print(attname)
	#print("heloooooooooooooooooooooooooo",ctag)

	#print("ctagggggggggggggggggggg:",ctag)
	#print(tagname)
	#print(attname)
	#print(attrval)
	#tags={"div ":0,"/div ":0}
	        #do line nos
	
	if len(tagname) > 0:
		for t in tagname:
			#print(" t :      ",t)
			if '</' not in t:
				token = t.split('<')
				token = token[1].strip()
				#print(token)
				if token in tags:
					if token in d.keys():
						d[token] += 1
					else:
						d[token] = 1
					tagWithNum = token+str(d[token])
					#print('<',tagWithNum,',','tag',",",lineno,'>','Valid')
					tagFinalList.append((tagWithNum,'tag','Opening_tag',lineno,'Valid'),)
					if token != 'a' and token != 'br' and token!= 'meta' and token!= 'link'  and token!= 'input': 
						stack.append((token,tagWithNum),)
						f2.write(str(stack))
						f2.write('\n')
				else:
					#print('<',token,',','tag',",",lineno,'>','Invalid')
					tagFinalList.append((token,'tag','Opening_tag',lineno,'Invalid'),)
			else:
				c = t
				#print("stack:                                    ",stack)
				#print("in ctgggggggggg")
				c = c.replace("</","")
				c = c.strip()
				if(c!= 'br'):
					if c in tags :
						length = len(stack)
						found = False	
						#print("hey",stack[-1][0])	
						if length >0 and stack[-1][0] == c:	
							#print('<',stack[-1][1],',','tag',",",'Closing_tag',',',lineno,'>','Valid')
							tagFinalList.append((stack[-1][1],'tag','Closing_tag',lineno,'Valid'),)
							del stack[-1]
						
						else:
							#print('<',c,',','tag',",",'Closing_tag',',',lineno,'>','ERROR')
							tagFinalList.append((c,'tag','Closing_tag',lineno,'ERROR'),)		


					else:
						#print("c tag invalid:",c,"yo")
						#print('<',t,',','tag',",",'Closing_tag',',',lineno,'>','Invalid')
						tagFinalList.append((c,'tag','Closing_tag',lineno,'Invalid'),)	
				else:
					tagFinalList.append((c,'tag','Closing_tag',lineno,'Valid'),)

F.close()							

f = open('op.txt','w')
for t in tagFinalList:
	for i in t:
		f.write(str(i)+ " ")
	for st in stack:
		#print("yooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
		if t[0] == st[1] and st[0]!='a':
			f.write('Closing_tag_missing')
	f.write('\n')

f.write("end \n")

for t in attFinalList:
	for i in t:
		f.write(str(i)+ " ")
	f.write('\n')

f.close()	

P = re.findall('[<(</)]\w+[ ]*<',s)
for p in P:
	temp = p.split('<')[0]
	#print(temp)
	s = s.replace(temp,temp+'>')


'''toReplace = re.findall('>.*<.*<',s)
for i in toReplace:
	print(i)
	i = i.split('>')[1]
	print(i)
	old = i
	new = i.replace('<','><')
	print(new)
	s.replace(i,old)
	print(s)''' 
