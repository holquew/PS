import re

# NUMBER - 0부터 9까지 숫자로만 이루어짐
def is_valid_number(s):
    if s.isdigit():
        return True
    else:
        return False

# STRING - 영어 대소문자
def is_valid_string(s):
    if re.match('[a-zA-Z]+', s):
        return True
    else:
        return False


def solution(program, flag_rules, commands):
    ARGUMENT_CODES = {
        'NULL': 0,
        'NUMBER': 1,
        'NUMBERS': 11, 
        'STRING': 2, 
        'STRINGS': 22, 
    }

    answer = []
    flags = {}

    for rule in flag_rules:
        splitted_rule = rule.split()

        if len(splitted_rule) == 2: 
            name, arg = splitted_rule[0], splitted_rule[1]
            flags[name] = ARGUMENT_CODES[arg]
        
        elif len(splitted_rule) == 3: 
            alias, existing = splitted_rule[0], splitted_rule[2]
            
            try: 
                flags[alias] = flags[existing]
            except KeyError: 
                for _ in range(len(commands)):
                    answer.append(False)
                
                return answer


    for command in commands:
        words = command.split()
        if words[0] != program: 
            answer.append(False)
            break

        words = words[1:]
        is_argu = False
        flag_code = None 
        used_flags = []
        for index, word in enumerate(words): 
            if is_argu: 
                if not flag_code in used_flags:
                    if flag_code == 1:
                        if not is_valid_number(word): 
                            answer.append(False)
                            break
                        is_argu = False 
                    
                    elif flag_code == 11: 
                        if not is_valid_number(word): 
                            answer.append(False)
                            break
                        try: 
                            word = words[index + 1]
                            if word in flags: 
                                is_argu = False 
                        except IndexError: 
                            answer.append(True)
                            break
                    
                    elif flag_code == 2: 
                        if not is_valid_string(word): 
                            answer.append(False)
                            break
                        is_argu = False 
                    
                    elif flag_code == 22: 
                        if not is_valid_string(word): 
                            answer.append(False)
                            break
                        try: 
                            word = words[index + 1]
                            if word in flags: 
                                is_argu = False 
                        except IndexError: 
                            answer.append(True)
                            break
                    
                    used_flags.append(flag_code)
                else: 
                    answer.append(False)
                    break
                
            else: 
                if not word in flags: 
                    answer.append(False)
                    break
                
                flag_code = flags[word]
                if flag_code != 0: 
                    is_argu = True
        else: 
            answer.append(True)

    return answer


print(
    solution(
        "bank",
        ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"],
        ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]
    )
)
