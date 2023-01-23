from collections import namedtuple


Vaulter = namedtuple('Vaulter', 'i_height s_height i_speed s_speed')


def week_1():
    """
    Prompts a user for a pole vaulter's height and maximum_speed

    Arguments:
    None

    Return values:
    height -- an integer containing the height of the pole vaulter in inches
    maximum_speed -- a float containing the maximum running speed with a pole of the pole vaulter
    """
    height = int(input("Please enter the pole vaulter's height: \n"))
    max_speed = float(input("Please enter the pole vaulter's maximum running speed: \n"))
    return height, max_speed

def week_2(height, maximum_speed):
    """
    Receives height (in inches) and maximum_speed (in mph).  Converts to SI units using the formulas given
    in the written instructions.  Returns the converted
    values.

    Arguments:
    height -- an int containing a pole vaulter's height in inches
    maximum_speed -- a float containing a pole vaulter's maximum speed in miles per hour or mph

    Return values:
    standard_height -- a float containing the converted height of the pole vaulter in meters or m
    standard_maximum_speed -- a float containing the converted maximum running speed with a pole of the pole vaulter in
                              meters per second or mps or m/s
    """
    standard_height = height * 0.0254
    standard_maximum_speed = maximum_speed * 0.44704
    return standard_height, standard_maximum_speed

def week_3(i_height, s_height, i_speed, s_speed):
    """
    Using the input values given, build and return a list, dictionary, and named tuple all representing your vaulter.

    Arguments
    i_height -- the height in imperial units
    s_height -- the height in standard units
    i_speed -- the speed in imperial units
    s_speed -- the speed in standard units

    Return Values:
    vaulter_list -- A list of lists containing two floats each e.g. [[1.0, 0.0254], [1.0, 0.44704], [1.0, 0.4535924]]
    vaulter_dict -- S dictionary where keys are the parameter names, and values the values e.g. {'i_height': 1.0,
    vaulter_namedtuple --  A Vaulter named tuple using the function parameters e.g. Vaulter(1.0, 2.45...

    return the three data structures vaulter_list, vaulter_dict, vaulter_namedtuple
    """
    vaulter_list = [[i_height, s_height], [i_speed, s_speed]]
    vaulter_dict = {'i_height':i_height, 's_height':s_height, 'i_speed':i_speed, 's_speed':s_speed}
    vaulter_namedtuple = Vaulter(i_height, s_height, i_speed, s_speed)
    return vaulter_list, vaulter_dict, vaulter_namedtuple
    
def week_4(vaulter):
    """
    Receives a vaulter's information and returns their estimated jump height

    Arguments:
    vaulter -- a list, dictionary, or namedtuple that contains a pole vaulter's information

    Return values:
    jump_height -- a float containing the approximate jump height in meters
    """
    if type(vaulter) == list:
        jump_height = (1/2) * (vaulter[1][1]) ** 2 / 9.8 + vaulter[0][1]
    elif type(vaulter) == dict:
        jump_height = (1/2) * (vaulter['s_speed']) ** 2 / 9.8 + vaulter['s_height']
    else:
        jump_height = (1/2) * (vaulter.s_speed) ** 2 / 9.8 + vaulter.s_height
    return jump_height
    
def week_5(applicants):
    """
    Given a number of applicants, prompt the user until once for each applicant and adds the i_height and i_speed as a
    2 value list to a scores list

    Arguments:
        applicants -- an int representing the number of applicants

    Return Values:
        scores -- a list of lists in the format [[i_height_1, i_speed_1],
                                                 [i_height_2, i_speed_2],
                                                 ...,
                                                 [i_height_n, i_speed_n]]
    """
    scores = []
    
    for _ in range(applicants):
        scores.append(list(week_1()))
    return scores

def week_6(scores):
    """
    Builds a list of vaulter structured types given
    a list of i_height and i_speeds in the format [[i_height_1, i_speed_1], [i_heieght_2, i_speed_2], ... ]

    Arguments:
        scores -- list of i_height and i_speeds in the format [[i_height_1, i_speed_1], [i_heieght_2, i_speed_2], ... ]

    Return Value:
        vaulters -- list of vaulters in format [[vaulter1_list, vaulter1_dict, vaulter1_namedtuple], [vaulter2_list ...]
    """
    vaulters = []
    for ip_applicant in scores:
        si_unit = list(week_2(ip_applicant[0], ip_applicant[1]))
        combo_lst = list(week_3(ip_applicant[0], si_unit[0], ip_applicant[1], si_unit[1]))
        vaulters.append(combo_lst)
    return vaulters
    
def week_7(vaulters, cutoff):
    """
    Given a list of vaulter dictionaries,
    calculates the jump heights and removes the vaulters who don't make the cutoff.

    Arguments:
        vaulters -- a list of vaulters, potentially of any data type
        cutoff -- the minimum estimated jump_height needed for a vaulter to make the team

    Return Values:
        team_members -- a list of vaulter dictionaries who beat the jump_height cutoff
    """
    valid_applicants = []
    for vaulter in vaulters:
        jump_height = week_4(vaulter)
        if jump_height >= cutoff:
            valid_applicants.append(vaulter)
    return valid_applicants
    
def week_8(vaulters):
    """
    Given a list of vaulter dictionaries, build a list of strings that reports their
    i_height, i_speed, and jump_height in the following format:
    "Applicant's height {}, applicant's vaulting speed: {}, applicant's estimated jump_height: {}"

    Remember to use the IMPERIAL units and NOT the STANDARD units.

    Arguments:
        vaulters -- a list of dictionaries representing vaulters

    Return values:
        report -- a list of strings in the format:
                       "Applicant's height {}, applicant's vaulting speed: {}, applicant's estimated jump_height: {}"

    """
    report = []
    for vaulter_dict in vaulters:
        report.append(f"Applicant's height {vaulter_dict['i_height']}, Applicant's vaulting speed: {vaulter_dict['i_speed']}, Applicant's estimated jump_height: {week_4(vaulter_dict)}")
    return report
    
def week_9(vaulter_file, cutoff):
    """
    Creates a report list using a text file.

    Arguments:
        vaulter_file -- a file with each line in the format "i_height, i_speed\n"
        cutoff -- the minimum estimated jump_height needed for a vaulter to make the team

    Return values:
        file_report -- a list of strings in the format:
                       "Applicant's height {}, applicant's vaulting speed: {}, applicant's estimated jump_height: {}"
    """
    scores = []
    si_score = []
    file_report = []
    f = open(vaulter_file) 
    lines = f.readlines()
    f.close()
    for height_speed in lines:
        height_speed = height_speed.strip('\n').split(',')
        scores.append(height_speed)
        
        si_score.append(list(week_2(int(height_speed[0]), int(height_speed[1]))))
        for si_h_s in si_score:
            jump_height = (1/2) * (si_h_s[1]) ** 2 / 9.8 + si_h_s[0]
        if jump_height >= cutoff:
            file_report.append(f"Applicant's height {float(height_speed[0])}, Applicant's vaulting speed: {float(height_speed[1])}, Applicant's estimated jump_height: {jump_height}")
    return file_report
    
def week_10(report):
    """
    Given a report, sort it by the jump_height

    Arguments:
        report -- a list of strings reporting candidate statistics

    Return values:
        sorted_report -- a sorted list of strings reporting canidate statistics (a one line comprehension is fine)
    """
    jump_height = [info for stats in report for info in stats.split(',') if 'jump_height' in info]
    sorted_report = [split_str for jump_h in jump_height for split_str in jump_h.split() if '.' in split_str]
    sorted_report = sorted(sorted_report, reverse=True)
    return sorted_report
    
if __name__ == "__main__":
    # Here is a a suite of print statements to help you test your code
    # I are the two recommended examples for basic testing: 
    #     height 1, and speed 10; a patholigical example to test edge cases
    #     height 72, speed 23; a realistic example of an olympic athelete
    
    ti_height, ti_speed = week_1()
    print("Test week 1 ti_height:", ti_height)
    print("Test week 1 ti_speed:", ti_speed)
    print()

    ts_height, ts_speed = week_2(ti_height, ti_speed)
    print("Test week 2 ts_height:", ts_height)
    print("Test week 2 ts_speed:", ts_speed)
    print()

    tv_list, tv_dict, tv_namedtuple = week_3(ti_height, ts_height, ti_speed, ts_speed)
    print("Test week 3 tv_list:", tv_list)
    print("Test week 3 tv_dict:", tv_dict)
    print("Test week 3 tv_namedtuple:", tv_namedtuple)
    print()

    l_j_height = week_4(tv_list)
    d_j_height = week_4(tv_dict)
    n_j_height = week_4(tv_namedtuple)
    print("Test week 4 l_j_height:", l_j_height) 
    print("Test week 4 tv_dict:", tv_dict)
    print("Test week 4 tv_namedtuple:", tv_namedtuple)
    print()

    applicant_num = int(input("Please enter the number of applicants you would like to test: \n"))
    app_list = week_5(applicant_num)
    for i, app in enumerate(app_list):
        print(f"Testing week 5 applicant {i}: {app}")
    print()

    sc_list = week_6(app_list)
    for j, appl in enumerate(sc_list):
        print(f"testing week 6 number {j}: \n\tlist: {appl[0]}\n\tdict: {appl[1]}\n\tamedtuple: {appl[2]}")
    print()

    cutoff_test = int(input("Please enter a value to test cutoff for week 7: \n"))
    test_team_members = week_7([sc[1] for sc in sc_list], cutoff_test)
    print("Test week 7:", test_team_members)
    print()

    test_r = week_8(test_team_members)
    for k, mem in enumerate(test_r):
        print(f"Test week 8 member {k}: {mem}\n")
    print()

    test_f = week_9("vaulter_test_file.txt", cutoff_test)
    print("Testing week 9:")
    for f in test_f:
        print('\t', f)
    print()

    test_s = week_10(test_f)
    print("Test week 10:", test_s)