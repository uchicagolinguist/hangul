import os
import random  

NAME = 'Hangul'

f = open(NAME+'.tex','w')

f.write('% '+NAME+'.tex\n')
f.write('\\documentclass[border=12pt]{standalone}'+'\n')
f.write('\\usepackage{tikz}'+'\n')
f.write('\n')
f.write('\\begin{document}'+'\n')
f.write('\n')

f.write('\\begin{tikzpicture}(0,0)(18,18)\n')
f.write('\n')

thickness = 30

def vowel():
	'''draw radicals for vowels'''
	none = ''
	right1 = '\t\\draw [line width='+str(thickness)+'pt, black ] (9,9) -- (11,9);\n'
	left1 = '\t\\draw [line width='+str(thickness)+'pt, black ] (7,9) -- (9,9);\n'
	right2 = '\t\\draw [line width='+str(thickness)+'pt, black ] (11,10) -- (9,10) -- (9,8) -- (11,8);\n'
	left2 = '\t\\draw [line width='+str(thickness)+'pt, black ] (7,10) -- (9,10) -- (9,8) -- (7,8);\n'
	f.write('\t\\draw [line width='+str(thickness)+'pt, black, rounded corners ] (9,3.5) -- (9,14.5);\n')
	f.write(random.choice([none,right1,left1,right2,left2]))

# vowel()
# f.write('\n')

def consonant():
	'''draw radicals for consonants'''
	O = '\t\\draw[line width='+str(thickness)+'pt, black ] (9,9) circle (75pt);\n'
	M = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (6.5,6.5) rectangle (11.5,11.5);\n'
	D = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) -- (6.5,6.5) -- (6.5,11.5) -- (11.5,11.5);\n'
	T = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) -- (6.5,6.5) -- (6.5,9) -- (11.5,9) -- (6.5,9) --(6.5,11.5) -- (11.5,11.5);\n'
	R = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) -- (6.5,6.5) -- (6.5,9) -- (11.5,9) -- (11.5,11.5) -- (6.5,11.5);\n'
	N = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) -- (6.5,6.5) -- (6.5,11.5);\n'
	G = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) -- (11.5,11.5) -- (6.5,11.5);\n'
	K = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) -- (11.5,9) -- (6.5,9) -- (11.5,9) -- (11.5,11.5) -- (6.5,11.5);\n'
	B = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,11.5) -- (11.5,6.5) -- (6.5,6.5) -- (6.5,11.5) -- (6.5,9) -- (11.5,9);\n'
	P = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) -- (6.5,6.5) -- (8,6.5) -- (8,11.5) -- (6.5,11.5) -- (11.5,11.5) -- (10,11.5) -- (10,6.5);\n'
	S = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (6.5,6.5) parabola (9,11.5);\n'+'\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) parabola (9,11.5);\n'
	J = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (6.5,6.5) parabola (9,11.5);\n'+'\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) parabola (9,11.5);\n'+'\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (6.5,11.5) -- (11.5,11.5);\n'
	C = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (6.5,6.5) parabola (9,10);\n'+'\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (11.5,6.5) parabola (9,10);\n'+'\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (6.5,10) -- (11.5,10);\n'+'\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (8,11.5) -- (10,11.5);\n'
	H = '\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (9,8) ellipse (75pt and 25pt);\n'+'\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (6.5,10) -- (11.5,10);\n'+'\t\\draw[line width='+str(thickness)+'pt, black, rounded corners ] (8,11.5) -- (10,11.5);\n'
	f.write(random.choice([O,M,D,T,R,N,G,K,B,P,S,J,C,H]))

# consonant()
# f.write('\n')

def character():
	'''combine vowels and consonants'''
	upright = '\t\\begin{scope}[shift={(4,0)}]\n'
	acostado = '\t\\begin{scope}[shift={(18,-4)}, rotate=90]\n'
	position = random.choice([upright,acostado])
	stretchX = '\t\\begin{scope}[shift={(-6.4,1)}]\n'+'\t\\pgftransformxscale{1.7}\n'
	stretchY = '\t\\begin{scope}[shift={(-1,-6.5)}]\n'+'\t\\pgftransformyscale{1.7}\n'
	f.write(position)
	vowel()
	f.write('\t\\end{scope}\n')
	if position == upright:
		f.write(stretchY)
	else:
		f.write(stretchX)
	consonant()
	f.write('\t\\end{scope}\n')

# character()
# f.write('\n')

def word(nmChar):
	xOffset = 0
	for x in range(nmChar):
		f.write('\\begin{scope}[shift={('+str(xOffset)+',0)}]\n')
		character()
		f.write('\\end{scope}\n')
		f.write('\n')
		xOffset += 12

# word(3)

def characters(nmChar):
	'''combine vowels and consonants'''
	xOffset = 0
	for x in range(nmChar):
		upright = '\t\\begin{scope}[shift={('+str(xOffset+4)+',0)}]\n'
		acostado = '\t\\begin{scope}[shift={('+str(xOffset+18)+',-4)}, rotate=90]\n'
		position = random.choice([upright,acostado])
		stretchX = '\t\\begin{scope}[shift={('+str(xOffset-6.4)+',1)}]\n'+'\t\\pgftransformxscale{1.7}\n'
		stretchY = '\t\\begin{scope}[shift={('+str(xOffset-1)+',-6.5)}]\n'+'\t\\pgftransformyscale{1.7}\n'
		f.write(position)
		vowel()
		f.write('\t\\end{scope}\n')
		if position == upright:
			f.write(stretchY)
		else:
			f.write(stretchX)
		consonant()
		f.write('\t\\end{scope}\n')
		f.write('\n')
		xOffset += 12

# characters(3)

def text(nmChar,nmWord):
	xOffset = 0
	for x in range(nmWord):
		for x in range(random.randint(1,nmChar)):
			f.write('\\begin{scope}[shift={('+str(xOffset)+',0)}]\n')
			character()
			f.write('\\end{scope}\n')
			f.write('\n')
			xOffset += 12
		f.write('\\begin{scope}[shift={('+str(xOffset)+',0)}]\n')
		f.write('\\end{scope}\n')
		f.write('\n')
		xOffset += 12

# text(7,random.randint(1,7))

def page(nmChar,nmWord,nmLine):
	yOffset = 0
	xOffset = 0
	for x in range(nmWord):
		for x in range(random.randint(1,nmChar)):
			f.write('\\begin{scope}[shift={('+str(xOffset)+','+str(yOffset)+')}]\n')
			character()
			f.write('\\end{scope}\n')
			f.write('\n')
			xOffset += 12
			if xOffset >= (12*nmLine):
				xOffset = 0
				yOffset -= 14
		f.write('\\begin{scope}[shift={('+str(xOffset)+','+str(yOffset)+')}]\n')
		f.write('\\end{scope}\n')
		f.write('\n')
		xOffset += 12
		if xOffset >= (12*nmLine):
			xOffset = 0
			yOffset -= 14

page(9,random.randint(1,9),7)

f.write('\\end{tikzpicture}\n')
f.write('\n')
f.write('\\end{document}'+'\n')

f.close()

print('fishihed '+NAME+'.tex')

os.system('pdflatex '+NAME+'.tex')

os.system('rm '+NAME+'.aux')
os.system('rm '+NAME+'.log')

print('building '+NAME+'.pdf now')