# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#The language spoken the most in Switzerland is the same as in Spain. (FALSE)
spain_language_spoken = 'Spanish'
switzerland_language_spoken = 'German'

print ('switzerland_language_spoken' == 'spain_language_spoken')

#The most prevalent religion in Switzerland is the same as in Spain. (TRUE)
spain_religion = ('Roman Catholic')
switzerland_religion = ('Roman Catholic')

print (switzerland_religion == spain_religion)

#The name length of Spain's capital does not equal that of Switzerland. (TRUE)
spain_capital = (len('Madrid'))
switzerland_capital = (len('Zurich'))

print (int(switzerland_capital) == int(switzerland_capital))

#Switzerland's GDP is greater than Spain's GDP. (FALSE)
spain_gdp = (1798 * 10**18)
switzerland_gdp = (618228 * 10**9)

print (int(switzerland_gdp) > int(spain_gdp))

#The population growth is less than 1% in Switzerland and Spain.(TRUE)
spain_population_growth = (0.13)
switzerland_population_growth = (0.65)

print ((spain_population_growth < 1) and (switzerland_population_growth < 1))


#At least one of the two countries has a population count of over 10 million. (TRUE)
spain_population = (47163418)
switzerland_population = (8508698)
population_gt = 10000000

print ('spain_population' > 'population_gt') or ('switzerland_population' > 'population_gt')

#Exactly one of the two countries has a population count of over 10 million. (TRUE)
if spain_population > population_gt:
    print ('spain_population' > 'population_gt')
elif switzerland_population > population_gt:
    print ('switzerland_population' > 'population_gt')
