def input_num(summary):
    """
    输入数字类型,并做 int 或者 float 转化
    """
    is_put_num = True
    while is_put_num:
        num = input('>> 请输入%s:' % summary)
        try:
            num = int(num)
        except:
            try:
                num = float(num)
            except:
                print("请输入数字类型")
                continue
        if isinstance(num, (int, float)):
            is_put_num = False
    return num


if __name__ == '__main__':
    input_num()
