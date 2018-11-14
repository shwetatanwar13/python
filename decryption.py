

a="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
c="map"
b=[]
for i in c:
  if i in (' ',',','\'','.'):
      b.append(i)
  else:
      b.append(chr(ord(i)+2) if (ord(i)+2) <=122 else chr(ord(i)+2-26))
print(''.join(i for i in b))