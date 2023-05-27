"""
1回だけのループをして、以下のことができたら幸せなのをテストする
- 変数のスコープを作る
- breakでの脱出
"""
def counts():
    print("count check")

    print("(1,)")
    i = 0
    for _ in (1,):
        i += 1
        print("in loop {}".format(i))

    print("range(1)")
    i = 0
    for _ in range(1):
        i += 1
        print("in loop {}".format(i))

    """
    # これはエラーになる
    print("(1)")
    i = 0
    for _ in (1):
        i += 1
        print("in loop {}".format(i))
    """

def scope():
    print("check scope")
    print("before loop")

    for _ in (1,):
        x = 1
        print("in loop, {}".format(x))
        x += 1

    print("after loop")
    print("outer scope? ".format(x))

    return

def breaking():
    print("check break")
    print("before loop")

    for _ in (1,):
        print("in loop")
        break
        print("in loop2")
    print("after loop")


    print("after loop")

    return

counts()
scope()
breaking()

