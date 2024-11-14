from mrjob.job import MRJob

class MRLanguagesBudgetCountries(MRJob):
    def mapper(self, _, line):
        fields = line.split('|')
        if len(fields) < 5:
            return
        language = fields[2]
        country = fields[3]
        try:
            budget = int(fields[4])
        except ValueError:
            return
        if (language == "-1" or language == "") or (country == "-1" or country == "") or budget == -1:
            return
        yield language, (country, budget)


    def reducer(self, language, country_budget_pairs):
        country_set = set()
        total_budget = 0
        for country, budget in country_budget_pairs:
            country_set.add(country)
            total_budget += budget
        country_list = list(country_set)
        yield language, [country_list, total_budget]


if __name__ == '__main__':
    MRLanguagesBudgetCountries.run()
