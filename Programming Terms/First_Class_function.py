
def square(x):
    return pow(x,2)

def m_map(func, arg_ls):
    result = []

    for i in arg_ls:
        result.append(func(i))
    return result

lis = [1, 2, 3, 4, 5]
sq = m_map(square, lis) # This is the same as the example bellow:
                        # sq = map(square, lis)
                        # print(list(sq))
print(sq)


def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message # By not putting the parentheses we assing
                       # instead of calling, the function

lg_t = logger
lg_t('hack')() # Is equal to :lg_t = logger('hack')
               #              lg_t()
