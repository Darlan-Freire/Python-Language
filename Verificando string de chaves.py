#Esse prog verifica se uma string de chaves abre e fecha!!!

st1 = '{{{}}}'
st2 = '{}{}{}'
st3 = '{{}{}}'
st4 = '}{}{'
st5 = '{}{{'
st6 = '{}}}}'

def verificador_chaves(string):
    controle = 0
    if len(string) % 2 == 1:
        print('As chaves NÃO correspondem')
    else:
        for ch in list(string):
            if controle == -1:
                print('As chaves NÃO correspondem')
                break
            if ch == '}':
                controle -= 1
            if ch == '{':
                controle += 1
        if controle == 0:
            print('As chaves correspondem')
        if controle > 0:
            print('As chaves NÃO correspondem')

verificador_chaves(st6)