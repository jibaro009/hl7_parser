import hl7
import re

# File paths
cr_lf = '\r\n'
tab = '\t'
# file_name = 'test_files/elr_wilson.hl7'
# file_name = 'test_files/elr_catawba.hl7'
file_name = 'test_files/elr_caromont.hl7'
# report_name = 'report/' + 'basic_elr_validation_report_wilson.txt'
# report_name = 'report/' + 'basic_elr_validation_report_catawba.txt'
report_name = 'report/' + 'basic_elr_validation_report_caromont.txt'
report = ''

# def MSH(segment):
#     print('MSH Segment')
#     for fields in segment:
#             print(fields)

# def PID():
#     print('PID Segment')

def msh(msh_segment):
    # print(msh_segment(1)(10))
    msh_fields = 'MSH Segment' + cr_lf
    msh_fields += 'MSH-03:{}'.format(str(msh_segment(1)(3))) + cr_lf
    msh_fields += 'MSH-04:{}'.format(str(msh_segment(1)(4))) + cr_lf
    msh_fields += 'MSH-05:{}'.format(str(msh_segment(1)(5))) + cr_lf
    msh_fields += 'MSH-06:{}'.format(str(msh_segment(1)(6))) + cr_lf
    msh_fields += 'MSH-07:{}'.format(str(msh_segment(1)(7))) + cr_lf
    msh_fields += 'MSH-09:{}'.format(str(msh_segment(1)(9))) + cr_lf
    msh_fields += 'MSH-10:{}'.format(str(msh_segment(1)(10))) + cr_lf
    msh_fields += 'MSH-11:{}'.format(str(msh_segment(1)(11))) + cr_lf
    msh_fields += 'MSH-12:{}'.format(str(msh_segment(1)(12))) + cr_lf
    msh_fields += 'MSH-15:{}'.format(str(msh_segment(1)(15))) + cr_lf
    msh_fields += 'MSH-16:{}'.format(str(msh_segment(1)(16))) + cr_lf
    msh_fields += 'MSH-21:{}'.format(str(msh_segment(1)(21))) + cr_lf
    msh_fields += '' + cr_lf

    return msh_fields

def pid(pid_segment):
    # print(str(pid_segment(1)(2)))
    pid_fields = 'PID Segment' + cr_lf
    pid_fields += 'PID-02:{}'.format(str(pid_segment(1)(2))) + cr_lf
    pid_components = ''
    # pid_fields += 'PID-03:{}'.format(str(pid_segment(1)(3))) + cr_lf
    # PID-3 repetitions
    index = 1
    pid_fields += 'PID-03:' + cr_lf
    for pid_3_repetition in pid_segment(1)(3):
        pid_fields += tab + 'PID-03[{}]:{}'.format(str(index),str(pid_3_repetition)) + cr_lf
        # pid components
        # print(len(pid_3_repetition))
        # print(pid_3_repetition)
        index_component = 1 
        for pid_components in pid_3_repetition:
            if pid_components(1) != '':
                pid_fields += tab + tab + 'PID-03[{}].{}:{}'.format(str(index),str(index_component),str(pid_components)) + cr_lf
            index_component += 1
        index_component = 1
        index +=1
    index = 1

    pid_fields += 'PID-04:{}'.format(str(pid_segment(1)(4))) + cr_lf
    pid_fields += 'PID-05:' + cr_lf
    # pid_fields += 'PID-05:{}'.format(str(pid_segment(1)(5))) + cr_lf
    for pid_5_repetition in pid_segment(1)(5):
        for pid_components in pid_5_repetition:
            if pid_components(1) != '':
                pid_fields += tab + 'PID-05.{}:{}'.format(str(index_component),str(pid_components)) + cr_lf
            index_component += 1
        index_component = 1
        index +=1
    index =1

    pid_fields += 'PID-06:{}'.format(str(pid_segment(1)(6))) + cr_lf
    pid_fields += 'PID-07:{}'.format(str(pid_segment(1)(7))) + cr_lf
    pid_fields += 'PID-08:{}'.format(str(pid_segment(1)(8))) + cr_lf
    pid_fields += 'PID-09:{}'.format(str(pid_segment(1)(9))) + cr_lf
    pid_fields += 'PID-10:{}'.format(str(pid_segment(1)(10))) + cr_lf
    pid_fields += 'PID-11:' + cr_lf
    # pid_fields += 'PID-11:{}'.format(str(pid_segment(1)(11))) + cr_lf
    for pid_5_repetition in pid_segment(1)(11):
        for pid_components in pid_5_repetition:
            if pid_components(1) != '':
                pid_fields += tab + 'PID-11.{}:{}'.format(str(index_component),str(pid_components)) + cr_lf
            index_component += 1
        index_component = 1
        index +=1    
    index = 1

    pid_fields += 'PID-13:{}'.format(str(pid_segment(1)(13))) + cr_lf
    pid_fields += 'PID-14:{}'.format(str(pid_segment(1)(14))) + cr_lf
    pid_fields += 'PID-15:{}'.format(str(pid_segment(1)(15))) + cr_lf
    pid_fields += 'PID-19:{}'.format(str(pid_segment(1)(19))) + cr_lf
    pid_fields += 'PID-22:{}'.format(str(pid_segment(1)(22))) + cr_lf
    pid_fields += 'PID-29:{}'.format(str(pid_segment(1)(29))) + cr_lf
    pid_fields += 'PID-30:{}'.format(str(pid_segment(1)(30))) + cr_lf
    pid_fields += '' + cr_lf

    return pid_fields

def orc(orc_segment):
    orc_fields = 'ORC Segment' + cr_lf
    orc_fields += 'ORC-10:{}'.format(str(orc_segment(1)(10))) + cr_lf
    orc_fields += 'ORC-12.1:{}'.format(str(orc_segment(1)(12)(1)(2))) + cr_lf
    orc_fields += 'ORC-12.3:{}'.format(str(orc_segment(1)(12)(1)(3))) + cr_lf
    orc_fields += 'ORC-21.1:{}'.format(str(orc_segment(1)(21)(1)(1))) + cr_lf
    orc_fields += 'ORC-21.7:{}'.format(str(orc_segment(1)(21)(1)(7))) + cr_lf
    orc_fields += 'ORC-22:{}'.format(str(orc_segment(1)(22))) + cr_lf
    orc_fields += 'ORC-23:{}'.format(str(orc_segment(1)(23))) + cr_lf
    orc_fields += 'ORC-24:{}'.format(str(orc_segment(1)(24))) + cr_lf
    orc_fields += '' + cr_lf

    return orc_fields

def obr(obr_segments):
    index = 1
    obr_fields = '' + cr_lf
    obr_fields = 'OBR Segment(s)' + cr_lf
    for obr_field in obr_segments:
        obr_fields += 'OBR[{}]'.format(str(index)) + cr_lf
        obr_fields += 'OBR[{}]-02.1:{}'.format(str(obr_field(1)), str(obr_field(2)(1)(1))) + cr_lf
        obr_fields += 'OBR[{}]-03.1:{}'.format(str(obr_field(1)), str(obr_field(3)(1)(1))) + cr_lf
        obr_fields += 'OBR[{}]-02 (Susceptibility):{}'.format(str(obr_field(1)), str(obr_field(2)(1))) + cr_lf
        obr_fields += 'OBR[{}]-03 (Susceptibility):{}'.format(str(obr_field(1)), str(obr_field(3)(1))) + cr_lf
        obr_fields += 'OBR[{}]-04:{}'.format(str(obr_field(1)), str(obr_field(4))) + cr_lf
        obr_fields += 'OBR[{}]-16:{}'.format(str(obr_field(1)), str(obr_field(16))) + cr_lf
        obr_fields += 'OBR[{}]-22:{}'.format(str(obr_field(1)), str(obr_field(22))) + cr_lf
        obr_fields += 'OBR[{}]-25:{}'.format(str(obr_field(1)), str(obr_field(25))) + cr_lf
        # print(len(obr_field))
        if len(obr_field) > 27:
            if obr_field(26)(1) != '':
                obr_fields += 'OBR 26 (Susceptibilities)' + cr_lf
                obr_fields += tab + 'OBR[{}]-26:{}'.format(str(obr_field(1)), str(obr_field(26))) + cr_lf
                obr_fields += tab + tab + 'OBR[{}]-26.1:{}'.format(str(obr_field(1)), str(obr_field(26)(1)(1))) + cr_lf
                obr_fields += tab + tab + 'OBR[{}]-26.2:{}'.format(str(obr_field(1)), str(obr_field(26)(1)(2))) + cr_lf
                obr_fields += tab + tab + 'OBR[{}]-26.3:{}'.format(str(obr_field(1)), str(obr_field(26)(1)(3))) + cr_lf
            else:
                obr_fields += 'OBR[{}]-26:'.format(str(obr_field(1))) + cr_lf

            if obr_field(29)(1) != '':
                obr_fields += 'OBR 29 (Susceptibilities)' + cr_lf
                obr_fields += tab + 'OBR[{}]-29:{}'.format(str(obr_field(1)), str(obr_field(29))) + cr_lf
                obr_fields += tab + tab + 'OBR[{}]-29.1:{}'.format(str(obr_field(1)), str(obr_field(29)(1)(1))) + cr_lf
                obr_fields += tab + tab + 'OBR[{}]-29.2:{}'.format(str(obr_field(1)), str(obr_field(29)(1)(2))) + cr_lf
            else:
                obr_fields += 'OBR[{}]-29:'.format(str(obr_field(1))) + cr_lf

            if obr_field(31)(1) != '':
                obr_fields += 'OBR[{}]-31:{}'.format(str(obr_field(1)), str(obr_field(31))) + cr_lf
            else:
                obr_fields += 'OBR[{}]-31:'.format(str(obr_field(1))) + cr_lf

            # obr_fields += 'OBR[{}]-29.1:{}'.format(str(obr_field(1)), str(obr_field(29)(1)(1))) + cr_lf
        obr_fields += '' + cr_lf

        index += 1

        

        #debug code
        # index_j = 1
        # for field in obr_field:
        #     print('OBR-{}:{}'.format(str(index_j), str(field)))
        #     index_j += 1
    obr_fields += '' + cr_lf

    return obr_fields

def obx(obx_segments):
    obx_fields = 'OBX Segment(s)' + cr_lf
    index = 1
    for obx_field in obx_segments:
        obx_fields += 'OBX[{}]'.format(str(index)) + cr_lf
        obx_fields += 'OBX[{}]-02:{}'.format(str(obx_field(1)), str(obx_field(2))) + cr_lf
        obx_fields += 'OBX[{}]-03:{}'.format(str(obx_field(1)), str(obx_field(3))) + cr_lf
        obx_fields += 'OBX[{}]-04:{}'.format(str(obx_field(1)), str(obx_field(4))) + cr_lf
        obx_fields += 'OBX[{}]-05:{}'.format(str(obx_field(1)), str(obx_field(5))) + cr_lf
        obx_fields += 'OBX[{}]-06:{}'.format(str(obx_field(1)), str(obx_field(6))) + cr_lf
        obx_fields += 'OBX[{}]-07:{}'.format(str(obx_field(1)), str(obx_field(7))) + cr_lf
        obx_fields += 'OBX[{}]-23.1:{}'.format(str(obx_field(1)), str(obx_field(23)(1)(1))) + cr_lf
        obx_fields += 'OBX[{}]-23.6:{}'.format(str(obx_field(1)), str(obx_field(23)(1)(6))) + cr_lf
        obx_fields += 'OBX[{}]-23.10:{}'.format(str(obx_field(1)), str(obx_field(23)(1)(10))) + cr_lf
        obx_fields += '' + cr_lf
        index += 1

    obx_fields += '' + cr_lf

    return obx_fields

def spm(spm_segments):
    spm_fields = 'SPM Segment(s)' + cr_lf
    index = 1
    for spm_field in spm_segments:
        spm_fields += 'SPM[{}]'.format(str(index)) + cr_lf
        spm_fields += 'SPM[{}]-2.2.1:{}'.format(str(spm_field(1)), str(spm_field(2)(1)(2)(1))) + cr_lf
        spm_fields += 'SPM[{}]-4:{}'.format(str(spm_field(1)), str(spm_field(4))) + cr_lf
        spm_fields += 'SPM[{}]-8:{}'.format(str(spm_field(1)), str(spm_field(8))) + cr_lf
        spm_fields += '' + cr_lf
        index +=1

    spm_fields += ''

    return spm_fields

def susceptibility(segments):
    susceptibility_fields = 'For Susceptibility Only' + cr_lf 
    susceptibility_fields += '-----------------------' + cr_lf 
    # Need to add code to look if OBX-3 is a susceptibility
    # print(segments('OBX')(1)(3))
    # print(segments('OBR')(2)(26)(1))
    
    # OBR 26 link
    child_obr_26_1 = str(segments('OBR')(2)(26)(1)(1))
    child_obr_26_2 = str(segments('OBR')(2)(26)(1)(2))
    child_obr_26_3 = str(segments('OBR')(2)(26)(1)(3))
    parent_obx_3 = str(segments('OBX')(1)(3))
    parent_obx_4 = str(segments('OBX')(1)(4))
    parent_obx_5_5 = str(segments('OBX')(1)(5)(1)(5))
    parent_obx_5_9 = str(segments('OBX')(1)(5)(1)(9))

    # OBR 26-1
    susceptibility_fields += 'OBR-26.1 link to parent OBX-3:' + cr_lf
    susceptibility_fields += tab + 'OBR-26.1:{}'.format(child_obr_26_1) + cr_lf
    susceptibility_fields += tab + 'OBX-03  :{}'.format(parent_obx_3) + cr_lf

    if re.sub('&','',child_obr_26_1) == re.sub('\^','',parent_obx_3):
        susceptibility_fields += tab + tab + 'Child OBR-26.1 = to Parent OBX-3' + cr_lf + cr_lf
    else:
        susceptibility_fields += tab + tab + 'Child OBR-26.1 <> to Parent OBX-3' + cr_lf + cr_lf
    
    # OBR 26-2
    susceptibility_fields += 'OBR-26.2 link to parent OBX-4:' + cr_lf
    susceptibility_fields += tab + 'OBR-26.2:{}'.format(child_obr_26_2) + cr_lf
    susceptibility_fields += tab + 'OBX-04  :{}'.format(parent_obx_4) + cr_lf


    if child_obr_26_2 == parent_obx_4:
        susceptibility_fields += tab + tab + 'Child OBR-26.2 = to Parent OBX-4' + cr_lf + cr_lf
    else:
        susceptibility_fields += tab + tab + 'Child OBR-26.2 <> to Parent OBX-4' + cr_lf + cr_lf
    
    # OBR 26.3
    susceptibility_fields += 'OBR-26.3 link to parent OBX-5.9 or 5.5:' + cr_lf
    susceptibility_fields += tab + 'OBR-26.3:{}'.format(child_obr_26_3) + cr_lf
    susceptibility_fields += tab + 'OBX-05.9:{}'.format(parent_obx_5_9) + cr_lf

    if child_obr_26_3.upper() == parent_obx_5_9.upper():
        susceptibility_fields += tab + tab + 'Child OBR-26.3 = to Parent OBX-5.9' + cr_lf + cr_lf
    else:
        susceptibility_fields += tab + tab + 'Child OBR-26.3 <> to Parent OBX-5.9' + cr_lf + cr_lf

    # OBR 29 link
    child_obr_29_1 = str(segments('OBR')(2)(29)(1)(1))
    child_obr_29_2 = str(segments('OBR')(2)(29)(1)(2))
    parent_obr_2 = str(segments('OBR')(1)(2))
    parent_obr_3 = str(segments('OBR')(1)(3))

    # OBR 29-1
    susceptibility_fields += 'OBR-29.1 link to parent OBR-2:' + cr_lf
    susceptibility_fields += tab + 'OBR-29.1:{}'.format(child_obr_29_1) + cr_lf
    susceptibility_fields += tab + 'OBR-02  :{}'.format(parent_obr_2) + cr_lf

    if re.sub('&','',child_obr_29_1) == re.sub('\^','',parent_obr_2):
        susceptibility_fields += tab + tab + 'Child OBR-29.1 = to Parent OBR-2' + cr_lf + cr_lf
    else:
        susceptibility_fields += tab + tab + 'Child OBR-29.1 <> to Parent OBR-2' + cr_lf + cr_lf

    # OBR 29-1
    susceptibility_fields += 'OBR-29.2 link to parent OBR-3:' + cr_lf
    susceptibility_fields += tab + 'OBR-29.2:{}'.format(child_obr_29_2) + cr_lf
    susceptibility_fields += tab + 'OBR-03  :{}'.format(parent_obr_3) + cr_lf

    if re.sub('&','',child_obr_29_2) == re.sub('\^','',parent_obr_3):
        susceptibility_fields += tab + tab + 'Child OBR-29.2 = to Parent OBR-3' + cr_lf + cr_lf
    else:
        susceptibility_fields += tab + tab + 'Child OBR-29.2 <> to Parent OBR-3' + cr_lf + cr_lf

    # OBX-2 Code
    # print(len(segments('OBR')))
    susceptibility_fields += 'OBX-2 Data types' + cr_lf
    
    valid_data_types = [
                        'CWE',
                        'SN',
                        'NM']
    invalid_data_type_flag = False
    obx_1_tracker = 0
    
    for segment in segments('OBX'):
        # print(segment(1))
        if str(segment(1)) == '1':
            obx_1_tracker += 1
        
        if obx_1_tracker >= 2:
            # Check susceptibility OBX-2 Data Type
            if str(segment(2)) in valid_data_types:
                susceptibility_fields += tab + 'OBX[{:0>2}]-2 data type: {}'.format(str(segment(1)), str(segment(2))) + cr_lf
                # invalid_data_type_flag = True
            else:
                susceptibility_fields += tab + 'OBX[{:0>2}]-2 data type: {} => Invalid'.format(str(segment(1)), str(segment(2))) + cr_lf
                # invalid_data_type_flag = False

    susceptibility_fields += '' + cr_lf
    # print(str(invalid_data_type_flag))
    # n = '1'
    # print('{:0>2}'.format(n))
    # print(obx_1_tracker)

    # OBX-3 Code.
    susceptibility_fields += 'OBX-3 Checking for LOINC Codes'  + cr_lf
    pattern = '(\d{1,5}-\d{1})'
    loinc_pattern = re.compile(pattern)
    obx_1_tracker = 0
    for segment in segments('OBX'):
        # print(segment(1))
        if str(segment(1)) == '1':
            obx_1_tracker += 1
        
        if obx_1_tracker >= 2:
            #  Check susceptibility OBX-3 LOINC Code
            # print((re.match(loinc_pattern,str(segment(3)(1)))))')
            # print(segment(3)(1)(3))
            if str(segment(3)(1)(3)) == 'LN':
                susceptibility_fields += 'OBX[{:0>2}]-3.1: {:<10} OBX[{:0>2}]-3.3: {}. LOINC code pattern is: {}'.format(str(segment(1)), str(segment(3)(1)(1)), str(segment(1)), str(segment(3)(1)(3)), 'valid' if loinc_pattern.match(str(segment(3)(1))) else 'invalid') + cr_lf
            else:
                susceptibility_fields += 'OBX[{:0>2}]-3.1: {:<10} OBX[{:0>2}]-3.3: {}. "LN" code expected'.format(str(segment(1)), str(segment(3)(1)(1)), str(segment(1)), str(segment(3)(1)(3))) + cr_lf
            # if loinc_pattern.match(str(segment(3)(1))):
                # print(segment(3)(1)(1))
                # print('OBX[{:0>2}]-3.1 Has a valid LOINC Code pattern: {} \t\t OBX[{:0>2}]3'.format(str(segment(1)), str(segment(3)(1)(1))))
            # else:
            #     print('OBX[{:0>2}]-3 LOINC Code has an invalid pattern: {}'.format(str(segment(3)(1))))
            # print(loinc_pattern.match(str(segment(3)(1))))
            # if str(segment(2)) in valid_data_types:
            #     susceptibility_fields += tab + 'OBX-2 data type: {}, OBX[{:0>2}]'.format(str(segment(2)), str(segment(1))) + cr_lf
            #     # invalid_data_type_flag = True
            # else:
            #     susceptibility_fields += tab + 'OBX-2 data type: {}, OBX[{:0>2}] => Invalid'.format(str(segment(2)), str(segment(1))) + cr_lf



    # susceptibility_fields += 'OBR 26 (Susceptibilities)' + cr_lf
    # susceptibility_fields += tab + 'OBR[{}]-26:{}'.format(str(obr_field(1)), str(obr_field(26))) + cr_lf
    # susceptibility_fields += tab + tab + 'OBR[{}]-26.1:{}'.format(str(obr_field(1)), str(obr_field(26)(1)(1))) + cr_lf
    # susceptibility_fields += tab + tab + 'OBR[{}]-26.2:{}'.format(str(obr_field(1)), str(obr_field(26)(1)(2))) + cr_lf
    # susceptibility_fields += tab + tab + 'OBR[{}]-26.3:{}'.format(str(obr_field(1)), str(obr_field(26)(1)(3))) + cr_lf
    
    susceptibility_fields += '' + cr_lf

    return susceptibility_fields

def generate_elr_report(parsed_hl7):
    report_content = ''
    index = 1

    # print(str(parsed_hl7).upper())


    # MSH Segment
    report_content = msh(parsed_hl7.segments('MSH'))
    # PID Segment
    report_content += pid(parsed_hl7.segments('PID'))
    # Print ORC Segment
    report_content += orc(parsed_hl7.segments('ORC'))
    # Print OBR Segment
    report_content += obr(parsed_hl7.segments('OBR'))
    # Print OBX Segment
    report_content += obx(parsed_hl7.segments('OBX'))
    # Print SPM Segment
    report_content += spm(parsed_hl7.segments('SPM'))
    # Print Susceptibilities
    if re.search('SUSCEPTIBILITY', str(parsed_hl7).upper()):
        report_content += susceptibility(parsed_hl7.segments)
        
    return report_content

# Turning of this function
# def print_elr_info(parsed_hl7, segment, field, component = 1, subfield = None):
#     if subfield is None:
#         # print(segment + '-' + str(field) + ': ' + str(parsed_hl7.segment(segment)(field)))
#         print('{}-{}:{}'.format(segment, field, str(parsed_hl7.segment(segment)(field))))
#     else:
#         # print(segment + '-' + str(field) + '.' + str(component) + '.' + str(subfield) + ': ' + str(parsed_hl7.segment(segment)(field)(1)(component)(subfield)))
#         print('{}-{}.{}:{}'.format(segment, field, component, str(parsed_hl7.segment(segment)(field)(1)(component)(subfield))))
#         # if segment == 'SPM':
#         #     # print(parsed_hl7.segment('SPM')(2)(1)(2))
#         #     print(parsed_hl7.parse_key('SPM.2.2.1'))

with open(file_name, 'r') as file:
    elr_message = file.read()

# print(elr_message)
# print(hl7.isfile(elr_message))

# Replace LN with CR
elr_message += re.sub(r'\n',r'\r',elr_message)
hl7_message = hl7.split_file(elr_message)

parsed_hl7 = hl7.parse(hl7_message[0])

#Debug
'''
print(hl7_message)
print(len(hl7_message))
'''
# print(parsed_hl7)

# index = 0
# for segments in parsed_hl7:
    # print(segments)
    # print(segments[0])
    # for fields in segments:
    #     print(fields)
    # index += 1
    # if str(segments[0]) == 'MSH':
    #     print('Do MSH stuff')
    # elif str(segments[0]) == 'PID':
    #     print('Do PID stuff')
    # print(segment_name(str(segments[0])))
    # segment_name(segments)


# print('Index = {}'.format(index))
# segments = parsed_hl7.segment('MSH')

# print(segments)

# for segment in segments:
#     print(segment)

# if the splitted message list is greater than 1 loop over each element and parse it
if len(hl7_message) > 1:
    for message in hl7_message:
        # print(message)
        parsed_hl7 = hl7.parse(message)
        # print(parsed_hl7[0][0])
        report += (generate_elr_report(parsed_hl7))
else:
    parsed_hl7 = hl7.parse(hl7_message[0])
    report = (generate_elr_report(parsed_hl7))
    # print(parsed_hl7[0][0])

# print(report_content)
with open(report_name, 'w') as file:
    file.write(report)

parsed_hl7 = None
report = None

