#! /usr/bin/python3

def has_straight(pswd:str) -> bool:
    if len(pswd) < 3: return False
    l = 1
    n = ord(pswd[0]) + 1
    for c in pswd[1:]:
        v = ord(c)
        l = l + 1 if v == n else 1
        n = v + 1
        if l == 3: return True

    return False

def no_bad(pswd:str) -> bool:
    return all(map(lambda c : c not in ['i','l','o'], pswd))

def has_dubs(pswd:str) -> bool:
    dubs = 0
    last = pswd[0]
    overlap = False
    for c in pswd[1:]:
        if overlap:
            overlap = False
        elif c == last:
            dubs += 1
            overlap = True
        last = c

    return dubs > 1

def valid_pswd(pswd:str) -> bool:
    return has_straight(pswd) and no_bad(pswd) and has_dubs(pswd)

def increment(pswd:list) -> list:
    for i in range(len(pswd) -1 , -1 ,-1):
        if pswd[i] == 'z':
            pswd[i] = 'a'
        else:
            nc = ord(pswd[i]) + 1
            pswd[i] = chr(nc)
            return pswd

    return pswd

def main():
    pwdL = ['v', 'z', 'b', 'x', 'k', 'g', 'h', 'b']
    pwds = [''.join(pwdL)]
    while len(pwds) < 3:
        pwdL = increment(pwdL)
        pwd = ''.join(pwdL)
        if valid_pswd(pwd):
            pwds.append(pwd)
            print(f'Password Found: {pwd}')

if __name__ == '__main__':
    main()
