import xml.etree.ElementTree as ET
import os
import csv

# give the xml files directory path here.
path = "/home/user/Documents/"
# Loop to get all files in the directory
for fn in os.listdir(path):
    # Check the file weather it's xml or not
    if not fn.endswith('.xml'): continue

    tree = ET.parse(path + fn)
    root = tree.getroot()

    # open a file for writing in csv format
    Real_data = open('converted.csv', 'a+')

    # create the csv writer object
    csvwriter = csv.writer(Real_data)
    award_head = []

    count = 0
    for member in root.findall('Award'):
        award = []
        awardInstrument = []
        organization = []
        directorate = []
        division = []
        programOfficer = []
        investigator = []
        institution = []
        programElement = []

        award_title = member.find('AwardTitle').text
        award.append(award_title)
        award_eff_date = member.find('AwardEffectiveDate').text
        award.append(award_eff_date)
        award_exp_date = member.find('AwardExpirationDate').text
        award.append(award_exp_date)
        award_amount = member.find('AwardAmount').text
        award.append(award_amount)
        if member.find('AwardInstrument') is not None:
            value = member.find('AwardInstrument')[0].text
            awardInstrument.append(value)
        award.append(awardInstrument)
        if member.find('Organization') is not None:
            org_code = member.find('Organization')[0].text
            organization.append(org_code)
            long_name = member.find('Organization')[1][0].text
            directorate.append(long_name)
            organization.append(directorate)
            long_name_div = member.find('Organization')[2][0].text
            division.append(long_name_div)
            organization.append(division)
        award.append(organization)
        if member.find('ProgramOfficer') is not None:
            sign_blk_name = member.find('ProgramOfficer')[0].text
            programOfficer.append(sign_blk_name)
        award.append(programOfficer)
        abb_naration = member.find('AbstractNarration').text
        award.append(abb_naration)
        min_amd_letter = member.find('MinAmdLetterDate').text
        award.append(min_amd_letter)
        max_amd_letter = member.find('MaxAmdLetterDate').text
        award.append(max_amd_letter)
        arramount = member.find('ARRAAmount').text
        award.append(arramount)
        award_id = member.find('AwardID').text
        award.append(award_id)
        if member.find('Investigator') is not None:
            first_name = member.find('Investigator').find('FirstName').text
            investigator.append(first_name)
            last_name = member.find('Investigator').find('LastName').text
            investigator.append(last_name)
            mail = member.find('Investigator').find('EmailAddress').text
            investigator.append(mail)
            start_date = member.find('Investigator').find('StartDate').text
            investigator.append(start_date)
            end_date = member.find('Investigator').find('EndDate').text
            investigator.append(end_date)
            role_code = member.find('Investigator').find('RoleCode').text
            investigator.append(role_code)
        award.append(investigator)
        if member.find('Institution') is not None:
            name = member.find('Institution').find('Name').text
            institution.append(name)
            city_name = member.find('Institution').find('CityName').text
            institution.append(city_name)
            zip_code = member.find('Institution').find('ZipCode').text
            institution.append(zip_code)
            p_number = member.find('Institution').find('PhoneNumber').text
            institution.append(p_number)
            s_address = member.find('Institution').find('StreetAddress').text
            institution.append(s_address)
            c_name = member.find('Institution').find('CountryName').text
            institution.append(c_name)
            state_name = member.find('Institution').find('StateName').text
            institution.append(state_name)
            state_code = member.find('Institution').find('StateCode').text
            institution.append(state_code)
        award.append(institution)
        if member.find('ProgramElement') is not None:
            code = member.find('ProgramElement').find('Code').text
            programElement.append(code)
            text = member.find('ProgramElement').find('Text').text
            programElement.append(text)
        award.append(programElement)
        csvwriter.writerow(award)
    Real_data.close()
