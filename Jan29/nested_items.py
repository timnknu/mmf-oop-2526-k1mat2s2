# John: Original post
#   Alice: this is incredible!
#     Alex: yes, indeed
#   Cat: meow
#     Dog: not at all

comments_storage = {}

comments_storage['jb'] = ('John', 'Original post', None)
comments_storage['mki'] = ('Alice', 'this is incredible!', 'jb')
comments_storage['g761'] = ('Alex', 'yes, indeed', 'mki')
comments_storage['ml981'] = ('Cat', 'meow', 'jb')
comments_storage['mn90'] = ('Dog', 'not at all', 'ml981')


#print(comments_storage)

k = 'mn90'
while True:
    v = comments_storage[k]
    print(v)#, '---- and it points to', v[-1])
    k = v[-1]
    if k is None:
        break