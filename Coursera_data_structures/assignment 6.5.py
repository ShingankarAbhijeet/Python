## string Slicing##

text = "X-DSPM-Confidence:0.8475"
pos = text.find(':')
print(pos)
pos2 = text[pos +1 : ]
print(pos2)

text = "  X-DSPM-Confidence:0.8475   "
pos = text.find(':')
pos2 = text[pos +1 : ]
fval = float(pos2)
print(fval) 