# https://www.hackerrank.com/challenges/python-quest-1/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


from io import StringIO
buf = StringIO()

for i in range(1,int(input())):
  #print(sum(map(lambda x: i * 10**x, range(i))))
  buf.write( "".join([str(i)]*i))
  buf.write('\n')
print(buf.getvalue())
