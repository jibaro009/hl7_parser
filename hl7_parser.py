import hl7
import re

file_name = 'test_files/elr_wilson.hl7'
file_name = 'test_files/elr_catawba.hl7'

def generate_elr_report(parsed_hl7):
    # MSH Segment
    print('MSH Segment')
    print_elr_info(parsed_hl7,'MSH',3)
    print_elr_info(parsed_hl7,'MSH',4)
    print_elr_info(parsed_hl7,'MSH',5)
    print_elr_info(parsed_hl7,'MSH',6)
    print_elr_info(parsed_hl7,'MSH',7)
    print_elr_info(parsed_hl7,'MSH',9)
    print_elr_info(parsed_hl7,'MSH',10)
    print_elr_info(parsed_hl7,'MSH',11)
    print_elr_info(parsed_hl7,'MSH',12)
    print_elr_info(parsed_hl7,'MSH',15)
    print_elr_info(parsed_hl7,'MSH',16)
    print_elr_info(parsed_hl7,'MSH',21)

    # PID Segment
    print('')
    print('PID Segment')
    print_elr_info(parsed_hl7,'PID',2)
    print_elr_info(parsed_hl7,'PID',3)
    print_elr_info(parsed_hl7,'PID',4)
    print_elr_info(parsed_hl7,'PID',5)
    print_elr_info(parsed_hl7,'PID',6)
    print_elr_info(parsed_hl7,'PID',7)
    print_elr_info(parsed_hl7,'PID',8)
    print_elr_info(parsed_hl7,'PID',9)
    print_elr_info(parsed_hl7,'PID',10)
    print_elr_info(parsed_hl7,'PID',11)
    print_elr_info(parsed_hl7,'PID',13)
    print_elr_info(parsed_hl7,'PID',14)
    print_elr_info(parsed_hl7,'PID',15)
    print_elr_info(parsed_hl7,'PID',19)
    print_elr_info(parsed_hl7,'PID',22)
    print_elr_info(parsed_hl7,'PID',29)
    print_elr_info(parsed_hl7,'PID',30)

    # Print ORC Segment
    print('')
    print('ORC Segment')
    print_elr_info(parsed_hl7,'ORC',10)
    print_elr_info(parsed_hl7,'ORC',12,2)
    print_elr_info(parsed_hl7,'ORC',12,3)
    print_elr_info(parsed_hl7,'ORC',21,1)
    print_elr_info(parsed_hl7,'ORC',21,7)
    print_elr_info(parsed_hl7,'ORC',22)
    print_elr_info(parsed_hl7,'ORC',23)
    print_elr_info(parsed_hl7,'ORC',24)

    # Print OBR Segment
    print('')
    print_elr_info(parsed_hl7,'OBR',3,1)
    print_elr_info(parsed_hl7,'OBR',4)
    print_elr_info(parsed_hl7,'OBR',16)
    print_elr_info(parsed_hl7,'OBR',22)
    print_elr_info(parsed_hl7,'OBR',25)
    print_elr_info(parsed_hl7,'OBR',31)

    # Print OBX Segment
    print('')
    print('OBX Segment')
    print_elr_info(parsed_hl7,'OBX',2)
    print_elr_info(parsed_hl7,'OBX',3)
    print_elr_info(parsed_hl7,'OBX',4)
    print_elr_info(parsed_hl7,'OBX',5)
    print_elr_info(parsed_hl7,'OBX',6)
    print_elr_info(parsed_hl7,'OBX',7)
    print_elr_info(parsed_hl7,'OBX',23,6)
    print_elr_info(parsed_hl7,'OBX',23,10)

    # Print SPM Segment
    print('')
    print("SPM Segment")
    print_elr_info(parsed_hl7,'SPM',2,2,1)
    print_elr_info(parsed_hl7,'SPM',4)
    print_elr_info(parsed_hl7,'SPM',8)

def print_elr_info(parsed_hl7, segment, field, component = 1, subfield = None):
    if subfield is None:
        print(segment + '-' + str(field) + ': ' + str(parsed_hl7.segment(segment)(field)))
    else:
        print(segment + '-' + str(field) + '.' + str(component) + '.' + str(subfield) + ': ' + str(parsed_hl7.segment(segment)(field)(1)(component)(subfield)))
        # if segment == 'SPM':
        #     # print(parsed_hl7.segment('SPM')(2)(1)(2))
        #     print(parsed_hl7.parse_key('SPM.2.2.1'))

with open(file_name, 'r') as file:
    elr_message = file.read()

# print(elr_message)
# print(hl7.isfile(elr_message))

# Replace LN with CR
elr_message += re.sub(r'\n',r'\r',elr_message)
hl7_message = hl7.split_file(elr_message)
# print(hl7_message)
# print(len(hl7_message))

# if the splitted message list is greater than 1 loop over each element and parse it
if len(hl7_message) > 1:
    for message in hl7_message:
        # print(message)
        parsed_hl7 = hl7.parse(message)
        # print(parsed_hl7[0][0])
        generate_elr_report(parsed_hl7)

else:
    parsed_hl7 = hl7.parse(hl7_message[0])
    generate_elr_report(parsed_hl7)
    # print(parsed_hl7[0][0])

