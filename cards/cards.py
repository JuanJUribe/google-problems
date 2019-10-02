import sys 

def everyone_sign(names):
    if type(names) != list:
        raise ValueError('everyone_sign function requires a list as argument')
    names = list(set(names))
    messages = {}
    for i, recipient in enumerate(names):
        friends = ', '.join(names[:i]+names[i+1:])
        message = 'Thank you! Your friends {}'.format(friends)
        messages.update({recipient : message})
    return messages