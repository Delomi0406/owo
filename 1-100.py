def sum(init, final,d):
    ans=((init+final)*(final-init//d+1))//2
    return ans
def product(init,final,d):
    ans=1
    while init <= final:
        ans*=init
        init += d
    return ans
def quadraticSum (init,final,d):
    ans=0
    while init <= final:
        ans += init**2
        init += d
    return ans
init=int(input("init=?"))
final=int(input("fianl=?"))
d=int(input("d)=?"))

print(sum(init,final,d))
print(product(init,final,d))
print(quadraticSum(init,final,d))