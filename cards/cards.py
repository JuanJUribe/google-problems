import sys 

def everyone_sign(names):
    if type(names) != list:
        print('everyone_sign function requires a list')
        sys.exit()
    messages = {}
    for i, recipient in names:
        friends = ', '.join(names[:i]+names[i+1:])
        message = 'Thank you! Your friends {}'.format(friends)
        messages.update({recipient : message})
    return messages