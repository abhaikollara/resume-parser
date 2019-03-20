import re
from collections import defaultdict
from entity_tagger import SpacyTagger, BERTTagger
from utils import read_text


class Parser:

    def __init__(self, tagger=None):
        self.data = {}
        self.tagger = tagger or BERTTagger()

    @staticmethod
    def get_sections(text):
        '''Splits text into various sections
        based on keyword search
        '''
        text = [line.strip() for line in text.splitlines()]
        text = filter(lambda x: x != '', text)

        sections = {'intro': [], 'experience': [],
                    'skills': [], 'education': []}
        section_name = "intro"
        for line in text:
            if any(keyword in line.lower()
                   for keyword in ['experience', 'work experience', 'employment']) \
                    and len(line.split()) < 3:
                section_name = 'experience'
            elif any(keyword in line.lower() for keyword in ['skills']):
                section_name = 'skills'
            elif any(keyword in line.lower() for keyword in ['education']):
                section_name = 'education'
            sections[section_name].append(line)

        # Rejoin split lines
        for k in sections.keys():
            sections[k] = '\n'.join(sections[k])

        return sections

    def parse(self, text):
        '''Extracts information from appropriate
        sections in the text
        '''
        data = {}
        sections = Parser.get_sections(text)

        data['name'] = self.get_name(sections['intro'])
        data['city'] = self.get_city(sections['intro'])
        data['email'] = self.get_email(sections['intro'])
        data['phone'] = self.get_phone_numbers(sections['intro'])
        data['previous_companies'] = self.get_previous_companies(
            sections['experience'])
        data['education'] = self.get_education(sections['education'])
        data['experience'] = self.get_experience(sections['experience'])
        data['skills'] = self.get_skills(sections['skills'])
        return data

    def parse_file(self, path):
        text = read_text(path)
        return self.parse(text)

    def get_name(self, text):
        '''Returns the first line of text
        after stripping whitespace
        '''
        # Entity recognition doesn't work as well
        return text.strip().splitlines()[0]

    def get_city(self, text):
        tags = self.tagger(text)
        gpes = [x.entity for x in tags if x.label in [
            'GPE', 'LOC'] and x.entity != '']

        return gpes

    def get_email(self, text):
        emails = re.findall(
            r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
        return emails

    def get_phone_numbers(self, text):
        # TODO: Change regex for different countries
        phones = re.findall(
            r"(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$", text)
        return phones

    def get_previous_companies(self, text):
        ''' Checks for ORG (Organiszation) entities
        within the text
        '''
        tags = self.tagger(text)
        orgs = [x.entity for x in tags if x.label == 'ORG']

        return orgs

    def get_experience(self, text):
        '''Finds date spans and calculates years of experience
        '''
        # TODO: Calculate years of experience from dates
        tags = self.tagger(text)
        dates = [x.entity for x in tags if x.label == 'DATE']

        return dates

    def get_education(self, text):
        '''Keyword search to identify educational
        instituions
        '''
        orgs = []
        for line in text.splitlines():
            if any(keyword in line.lower() for keyword in ['school', 'college', 'university', 'institute']):
                orgs.append(line)
        return orgs

    def get_skills(self, text):
        skills = []
        for line in text.splitlines():
            skills.extend(line.split(','))

        return skills
