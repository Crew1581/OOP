import re
class StrExtension:
    @staticmethod
    def remove_vowels(s):
        return re.sub(r'[aeiouyAEIOUY]', '', s)
    @staticmethod
    def leave_alpha(s):
        return re.sub(r'[\W\b_0-9]','',s)

    @staticmethod
    def replace_all(string, chars, char):
        return re.sub(rf'[{chars}]', rf'{char}', string)
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))