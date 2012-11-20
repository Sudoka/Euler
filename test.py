def is_palindromic(n): return str(n)==str(n)[::-1]

limit = 1000
sqrt_limit = int(limit**.5)
pal = set()
 
for i in range(1, sqrt_limit):
  sos = i*i
  for j in range(i+1, sqrt_limit):
    sos += j*j
    if sos>=limit: break
    if is_palindromic(sos): pal.add(sos)

print sorted(list(pal))
print sum(pal)
