import re

def remove_comments(string):
    pattern =r'(1.*1)|(2.*2)|(3.*3)'

    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):

        if match.group(2) is not None:
            print('2:' + match.group(2))
            # print('3:' + match.group(3))
            return "" 
        elif match.group(3) is not None:
            # print('2:' + match.group(2))
            print('3:' + match.group(3))
        else: # otherwise, we will return the 1st group
            print('1:' + match.group(1))
            return match.group(1) # captured quoted-string
    return regex.sub(_replacer, string)