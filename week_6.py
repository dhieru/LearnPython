text = "X-DSPAM-Confidence:    0.8475";
x = text.find('0')
flt = float(text[x:len(text)])
print flt
