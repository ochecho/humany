def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var35 = func3(arg1, var7)
    var42 = func9(arg2, arg1)
    if var42 < arg2:
        var43 = var7 | arg2
    else:
        var43 = (469 + var7 - (((arg2 - -155 + var42) ^ var35 ^ 235) & -727) | var7) & (var42 | var42 + ((((1396176345 + var42) + -536 - arg2 + arg2) + arg1) & arg2) | arg1 - 246) & -469 ^ 1135935073
    var44 = var7 | -1950445010
    result = var7 - (arg1 & var35)
    return result
def func9(arg36, arg37):
    var38 = arg36 - (arg36 + arg36)
    var39 = arg37 + arg36
    var40 = arg37 + var39 - arg36
    var41 = var38 + arg36 & -217218199 ^ arg36 - arg37
    result = ((55 + ((-2130098197 - (var41 + var38 ^ -841)) + arg36) - var40 | arg37) ^ var41 | var38 - -328346958) - 615101697
    return result
def func3(arg8, arg9):
    var12 = class4()
    for var13 in range(7):
        var14 = var12.func5
        var14(arg8, arg8)
    var15 = func8()
    var16 = (arg8 - arg9 - -793253441) ^ -851
    var17 = ((arg9 + 104851751) | var16) | var15
    var18 = (arg8 + arg9 ^ -1774608567) + arg8
    var19 = -9 & (var16 - var17) | var17
    var20 = var16 ^ arg8
    if var15 < arg8:
        var21 = arg9 - -849 + (arg9 - 1256928376)
    else:
        var21 = (var19 | 923) & var17 & var16
    var22 = 541 ^ -827
    var23 = var20 | 1783565464
    var24 = (var20 & (var17 & arg9)) | var18
    if var19 < var17:
        var25 = (arg8 ^ var19 - var23) ^ var16
    else:
        var25 = var20 - (var24 - 256) + var18
    var26 = -1658479448 ^ arg9
    var27 = (var24 + arg9 & var20) - var15
    var28 = var22 | var16 | (929 + var16)
    if var19 < var24:
        var29 = (var24 + (var20 + var19)) | var18
    else:
        var29 = ((var17 & var26) ^ var28) & -791
    var30 = var28 ^ (157 & var22) - var18
    var31 = (var15 ^ var30) ^ var22 & arg8
    var32 = (arg8 & var26) + var17 & var17
    var33 = arg8 | -465 | var15
    var34 = var15 + 1473845636 + var23 & 1735067845
    result = var30 | var22 ^ var23 - var34
    return result
def func8():
    func6()
    result = len(xrange(41))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : 9
class class4(object):
    def func5(self, arg10, arg11):
        result = arg11 | 1109885397 + 2031079305 ^ arg10
        return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(31):
        var5 += arg4 | var5 & var6
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 45'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
