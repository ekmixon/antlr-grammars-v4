# del_stmt: DEL exprlist

del x, d[1], await f

# pass_stmt: PASS
for i in u: pass

# break_stmt: BREAK
for i in u: break

# continue_stmt: CONTINUE
for i in u: continue

# return_stmt: RETURN testlist?
def f():
    # RETURN
    return
def g():
    # RETURN testlist
    return 1, 3

# [Python 3] raise_stmt: RAISE (test (FROM test)?)?

# RAISE test FROM test
raise a from b
