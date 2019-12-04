# message = 'FHS|^~\&|SQ^2.16.840.1.113883.3.697^ISO|Caromont Laboratory^34D0242966^CLIA|NCDPH NCEDSS^2.16.840.1.113883.3.591.3.1^ISO|NCDPH EDS^2.16.840.1.113883.3.591.1.1^ISO|20140827161659||20140827161659|\r'
# message += 'BHS|^~\&|SQ^2.16.840.1.113883.3.697^ISO|Caromont Laboratory^34D0242966^CLIA|NCDPH NCEDSS^2.16.840.1.113883.3.591.3.1^ISO|NCDPH EDS^2.16.840.1.113883.3.591.1.1^ISO|20140827161659||20140827161659|\r'
# message += 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
# message += 'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
# message += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
# message += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\r'
# message += 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
# message += 'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
# message += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
# message += 'OBX|1|SN|2554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\r'
# message += 'BTS|1||2324|\r'
# message += 'FTS|1|\r'

# print(message)

import hl7

with open('elr.hl7', 'rb') as file:
    elr_message = file.read()

# print(elr_message)
print(hl7.isfile(elr_message))

# hl7_message = hl7.split_file(elr_message)
# hl7_message = hl7.parse(hl7_message)
# print(len(hl7_message))

# print(hl7_message)

# for segments in hl7_message:
#     print(segments)

if hl7.isfile(elr_message):
    hl7_messages = hl7.split_file(elr_message)
    if len(hl7_messages) > 0:
        # messages = []
        # print hl7_messages
        # index = 0
        # print list(hl7_messages)
        for message in hl7_messages:
            parsed_hl7 = hl7.parse(message)
            # index += 1
            print(parsed_hl7[3])
            
        # print messages
    # print(len(hl7_messages))
    # hl7_messages = hl7.parse(hl7_messages[1])
    # print(hl7_message)

# for segments in hl7_messages:
#     print(segments)
