def check_is_valid_new_pswd(old_pswd, new_pswd):
    for i in range(1, len(old_pswd)):
        # right side 3 rotation
        old_pswd = old_pswd[-1] + old_pswd[:-1]
        if old_pswd == new_pswd:
            return True, i % len(old_pswd) 
    return False, None

def get_left_side_rotations(old_pswd, new_pswd):
    for i in range(1, len(old_pswd)+1):
        old_pswd = old_pswd[1:] + old_pswd[0]
        if old_pswd == new_pswd:
            return i % len(old_pswd)

def main():
    old_pswd = 'robin'
    new_pswd = 'rinbo'
    is_valid_new_pswd, rigth_side_rotations = check_is_valid_new_pswd(old_pswd, new_pswd)
    if is_valid_new_pswd:
        left_side_rotations = get_left_side_rotations(old_pswd, new_pswd)
        print(min(rigth_side_rotations, left_side_rotations))
    else:
        print(is_valid_new_pswd)

main()