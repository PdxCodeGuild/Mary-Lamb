'''
Counts the numbers of lambs in chapter 1
'''

lambs = 0
with open('chapter1', 'r+') as chapter1

    text = chapter1.read()
    words = text.split()
    for word in words:
        if word.lower() == 'lamb':
            lambs += 1

    # add this to the end of overview file
with open('overview', 'w') as overview
    lambs_statement = 'The number of times lambs is said in Chapter 1: {}'.format(lambs)
    overview.write('\n' + lambs_statement)
