def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    def func3(arg8, arg9):
        var10 = 441 ^ arg2 | 290 + arg1
        var11 = (arg8 | arg9) + (var10 & arg1)
        var12 = var7 + 1936272855
        var13 = (arg8 + var12 | var11) & arg1
        var14 = 1128688486 ^ (var7 ^ var11) - var13
        var15 = (arg1 - arg1) & -8 ^ var14
        if var14 < var12:
            var16 = (972 | -1908215551 & arg8) ^ arg8
        else:
            var16 = var13 - var10 + arg8 | var12
        var17 = var10 ^ 926024187
        var18 = var11 - (var7 ^ arg8 ^ -1127572258)
        if arg8 < var17:
            var19 = (var17 - var18) | arg2 & var7
        else:
            var19 = (var12 - var14 ^ var17) & var10
        var20 = var13 ^ var12
        var21 = var11 | var7 - 674 - 1106821492
        if arg8 < var14:
            var22 = (var17 ^ var14 + var18) - var7
        else:
            var22 = arg1 ^ (arg9 - arg8 | var20)
        var23 = var14 ^ -1330823545 & arg2 - arg8
        var24 = var7 - var17
        var25 = var23 + arg2 + var15
        result = var18 - var23 + (var18 & var21)
        return result
    var26 = func3(arg2, var7)
    var27 = func6()
    var28 = func9()
    var29 = var28 + -1287965400 & 880559966
    var30 = var28 + (var27 & var7)
    var31 = arg2 & arg1 - var30 - var30
    var32 = arg2 ^ var28
    var33 = var31 & var7
    var34 = var26 + var28 + var32 & var30
    var35 = arg1 - var33 ^ var28 ^ var32
    var36 = var29 & var32
    var37 = var30 ^ var32 ^ (arg2 - var7)
    var38 = var30 + -613 & var7 + var34
    var39 = var31 + var37 | var33
    result = var28 - var34
    return result
def func9():
    func7()
    result = len((7 | -2 ^ 7 for i in range(47)))
    func8()
    return result
def func8():
    global len
    del len
def func7():
    global len
    len = lambda x : -6
def func6():
    func4()
    result = len(xrange(43))
    func5()
    return result
def func5():
    global len
    del len
def func4():
    global len
    len = lambda x : 0
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(15):
        var5 += arg3 + var5 ^ var6
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 40'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
