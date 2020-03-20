import hl7
import re

# File paths
cr_lf = '\r\n'
file_name = 'test_files/elr_wilson.hl7'
# file_name = 'test_files/elr_catawba.hl7'
report_name = 'report/' + 'basic_elr_validation_report_wilson.txt'
# report_name = 'report/' + 'basic_elr_validation_report_catawba.txt'
report = ''
report_content = ''

# def MSH(segment):
#     print('MSH Segment')
#     for fields in segment:
#             print(fields)

# def PID():
#     print('PID Segment')

def msh():
    

def generate_elr_report(parsed_hl7):
    index = 1
    # MSH Segment
    report_content =('MSH Segment') + cr_lf
    report_content += ('MSH-3:{}'.format(str(parsed_hl7.segment('MSH')(3)))) + cr_lf
    report_content += ('MSH-4:{}'.format(str(parsed_hl7.segment('MSH')(4)))) + cr_lf
    report_content += ('MSH-5:{}'.format(str(parsed_hl7.segment('MSH')(5)))) + cr_lf
    report_content += ('MSH-6:{}'.format(str(parsed_hl7.segment('MSH')(6)))) + cr_lf
    report_content += ('MSH-7:{}'.format(str(parsed_hl7.segment('MSH')(7)))) + cr_lf
    report_content += ('MSH-9:{}'.format(str(parsed_hl7.segment('MSH')(9)))) + cr_lf
    report_content += ('MSH-10:{}'.format(str(parsed_hl7.segment('MSH')(10)))) + cr_lf
    report_content += ('MSH-11:{}'.format(str(parsed_hl7.segment('MSH')(11)))) + cr_lf
    report_content += ('MSH-12:{}'.format(str(parsed_hl7.segment('MSH')(12)))) + cr_lf
    report_content += ('MSH-15:{}'.format(str(parsed_hl7.segment('MSH')(15)))) + cr_lf
    report_content += ('MSH-16:{}'.format(str(parsed_hl7.segment('MSH')(16)))) + cr_lf
    report_content += ('MSH-21:{}'.format(str(parsed_hl7.segment('MSH')(21)))) + cr_lf
    report_content += ('') + cr_lf

    # PID Segment
    report_content += ('PID Segment') + cr_lf
    report_content += ('PID-2:{}'.format(str(parsed_hl7.segment('PID')(2)))) + cr_lf
    report_content += ('PID-3:{}'.format(str(parsed_hl7.segment('PID')(3)))) + cr_lf
    report_content += ('PID-4:{}'.format(str(parsed_hl7.segment('PID')(4)))) + cr_lf
    report_content += ('PID-5:{}'.format(str(parsed_hl7.segment('PID')(5)))) + cr_lf
    report_content += ('PID-6:{}'.format(str(parsed_hl7.segment('PID')(6)))) + cr_lf
    report_content += ('PID-7:{}'.format(str(parsed_hl7.segment('PID')(7)))) + cr_lf
    report_content += ('PID-8:{}'.format(str(parsed_hl7.segment('PID')(8)))) + cr_lf
    report_content += ('PID-9:{}'.format(str(parsed_hl7.segment('PID')(9)))) + cr_lf
    report_content += ('PID-10:{}'.format(str(parsed_hl7.segment('PID')(10)))) + cr_lf
    report_content += ('PID-11:{}'.format(str(parsed_hl7.segment('PID')(11)))) + cr_lf
    report_content += ('PID-13:{}'.format(str(parsed_hl7.segment('PID')(13)))) + cr_lf
    report_content += ('PID-14:{}'.format(str(parsed_hl7.segment('PID')(14)))) + cr_lf
    report_content += ('PID-15:{}'.format(str(parsed_hl7.segment('PID')(15)))) + cr_lf
    report_content += ('PID-19:{}'.format(str(parsed_hl7.segment('PID')(19)))) + cr_lf
    report_content += ('PID-22:{}'.format(str(parsed_hl7.segment('PID')(22)))) + cr_lf
    report_content += ('PID-29:{}'.format(str(parsed_hl7.segment('PID')(29)))) + cr_lf
    report_content += ('PID-30:{}'.format(str(parsed_hl7.segment('PID')(30)))) + cr_lf
    report_content += ('') + cr_lf

    # Print ORC Segment
    report_content += ('ORC Segment') + cr_lf
    report_content += ('ORC-10:{}'.format(str(parsed_hl7.segment('ORC')(10)))) + cr_lf
    report_content += ('ORC-12.1:{}'.format(str(parsed_hl7.segment('ORC')(12)(1)(2)))) + cr_lf
    report_content += ('ORC-12.3:{}'.format(str(parsed_hl7.segment('ORC')(12)(1)(3)))) + cr_lf
    report_content += ('ORC-21.1:{}'.format(str(parsed_hl7.segment('ORC')(21)(1)(1)))) + cr_lf
    report_content += ('ORC-21.7:{}'.format(str(parsed_hl7.segment('ORC')(21)(1)(7)))) + cr_lf
    report_content += ('ORC-22:{}'.format(str(parsed_hl7.segment('ORC')(22)))) + cr_lf
    report_content += ('ORC-23:{}'.format(str(parsed_hl7.segment('ORC')(23)))) + cr_lf
    report_content += ('ORC-24:{}'.format(str(parsed_hl7.segment('ORC')(24)))) + cr_lf
    report_content += ('') + cr_lf
    # print_elr_info(parsed_hl7,'ORC',10)
    # print_elr_info(parsed_hl7,'ORC',12,2)
    # print_elr_info(parsed_hl7,'ORC',12,3)
    # print_elr_info(parsed_hl7,'ORC',21,1)
    # print_elr_info(parsed_hl7,'ORC',21,7)
    # print_elr_info(parsed_hl7,'ORC',22)
    # print_elr_info(parsed_hl7,'ORC',23)
    # print_elr_info(parsed_hl7,'ORC',24)


    # Print OBR Segment
    report_content += ('OBR Segment(s)') + cr_lf
    obr_segments = parsed_hl7.segments('OBR')
    for obr_field in obr_segments:
        report_content += ('OBR[{}]'.format(index)) + cr_lf
        report_content += ('OBR[{}]-3.1:{}'.format(str(obr_field(1)), str(obr_field(3)(1)(1)))) + cr_lf
        report_content += ('OBR[{}]-4:{}'.format(str(obr_field(1)), str(obr_field(4)))) + cr_lf
        report_content += ('OBR[{}]-16:{}'.format(str(obr_field(1)), str(obr_field(16)))) + cr_lf
        report_content += ('OBR[{}]-22:{}'.format(str(obr_field(1)), str(obr_field(22)))) + cr_lf
        report_content += ('OBR[{}]-25:{}'.format(str(obr_field(1)), str(obr_field(25)))) + cr_lf
        if len(obr_field) >= 33:
            report_content += ('OBR[{}]-31:{}'.format(str(obr_field(1)), str(obr_field(32)))) + cr_lf
        report_content += ('') + cr_lf
        
        index += 1
        # print(len(obr_field))
        # index_j = 1
        # for field in obr_field:
        #     print('OBR-{}:{}'.format(str(index_j), str(field)))
        #     index_j += 1

    # print_elr_info(parsed_hl7,'OBR',3,1)
    # print_elr_info(parsed_hl7,'OBR',4)
    # print_elr_info(parsed_hl7,'OBR',16)
    # print_elr_info(parsed_hl7,'OBR',22)
    # print_elr_info(parsed_hl7,'OBR',25)
    # print_elr_info(parsed_hl7,'OBR',31)

    # Print OBX Segment
    report_content += ('OBX Segment(s)') + cr_lf
    obx_segments = parsed_hl7.segments('OBX')
    index = 1
    for obx_field in obx_segments:
        report_content += ('OBX[{}]'.format(str(index))) + cr_lf
        report_content += ('OBX[{}]-2:{}'.format(str(obx_field(1)), str(obx_field(2)))) + cr_lf
        report_content += ('OBX[{}]-3:{}'.format(str(obx_field(1)), str(obx_field(3)))) + cr_lf
        report_content += ('OBX[{}]-4:{}'.format(str(obx_field(1)), str(obx_field(4)))) + cr_lf
        report_content += ('OBX[{}]-5:{}'.format(str(obx_field(1)), str(obx_field(5)))) + cr_lf
        report_content += ('OBX[{}]-6:{}'.format(str(obx_field(1)), str(obx_field(6)))) + cr_lf
        report_content += ('OBX[{}]-7:{}'.format(str(obx_field(1)), str(obx_field(7)))) + cr_lf
        report_content += ('OBX[{}]-23.1:{}'.format(str(obx_field(1)), str(obx_field(23)(1)(1)))) + cr_lf
        report_content += ('OBX[{}]-23.6:{}'.format(str(obx_field(1)), str(obx_field(23)(1)(6)))) + cr_lf
        report_content += ('OBX[{}]-23.10:{}'.format(str(obx_field(1)), str(obx_field(23)(1)(10)))) + cr_lf
        report_content += ('') + cr_lf
        
        index += 1

    # print_elr_info(parsed_hl7,'OBX',2)
    # print_elr_info(parsed_hl7,'OBX',3)
    # print_elr_info(parsed_hl7,'OBX',4)
    # print_elr_info(parsed_hl7,'OBX',5)
    # print_elr_info(parsed_hl7,'OBX',6)
    # print_elr_info(parsed_hl7,'OBX',7)
    # print_elr_info(parsed_hl7,'OBX',23,6)
    # print_elr_info(parsed_hl7,'OBX',23,10)


    # Print SPM Segment
    report_content += ('SPM Segments(s)') + cr_lf
    spm_segments = parsed_hl7.segments('SPM')
    index = 1
    for spm_field in spm_segments:
        report_content += ('SPM[{}]'.format(str(index))) + cr_lf
        report_content += ('SPM[{}]-2.2.1:{}'.format(str(spm_field(1)), str(spm_field(2)(1)(2)(1)))) + cr_lf
        report_content += ('SPM[{}]-4:{}'.format(str(spm_field(1)), str(spm_field(4)))) + cr_lf
        report_content += ('SPM[{}]-8:{}'.format(str(spm_field(1)), str(spm_field(8)))) + cr_lf
        report_content += ('') + cr_lf
        
        index +=1

    # print('')
    # print("SPM Segment")
    # print_elr_info(parsed_hl7,'SPM',2,2,1)
    # print_elr_info(parsed_hl7,'SPM',4)
    # print_elr_info(parsed_hl7,'SPM',8)

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

