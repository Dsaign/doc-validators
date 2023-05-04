#!/usr/bin/env python
# -*- coding: latin-1 -*-

def isValidCPF(cpf):
    # get numbers only
    cpf = [int(char) for char in cpf if char.isdigit()]
    # check if it has 11 digits
    if not cpf and len(cpf) != 11:
        return False
    # check if all numbers are equal, e.g. '111.111.111-11'
    if cpf == cpf[::-1]:
        return False
    # validate checksum digits
    for i in (10, 11):
        value = sum((cpf[num] * (i - num) for num in range(i - 1)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def isValidCNPJ(cnpj):
    # get numbers only
    cnpj = [int(char) for char in cnpj if char.isdigit()]
    # check if it has 14 digits or empty
    if not cnpj or len(cnpj) < 14:
        return False
    # get 12 first digits and generate 2 last ones
    integers = map(int, cnpj)
    new_cnpj = integers[:12]
    prod = [5,4,3,2,9,8,7,6,5,4,3,2]
    while len(new_cnpj) < 14:
        r = sum([x*y for (x, y) in zip(new_cnpj, prod)]) % 11
        f = (11 - r) if r > 1 else 0
        new_cnpj.append(f)
        prod.insert(0, 6)
    # if digits are equal, True
    if new_cnpj == integers:
        return True
    return False