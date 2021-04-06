# OCTCMG

One-Class Text Collections From Marcos Gôlo

# Informations

These one-class text collections are made up of titles news from the GDELT project (Global Database of Events, Language, and Tone). The topics related to each textual collection were chosen based on the taxonomy of the IPTC (International Press Telecommunications Council). The GDELT project can be found at https://www.gdeltproject.org/ and all IPTC topics at https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html. The collection of the news was made by checking if the news contained the topic in its title. Topics that returned less than 4000 news items were not considered as a text collection. The limit of 6000 news items has been defined for all text collections. Finally, 183 text collections were obtained.

# How to Use

!pip install git+https://github.com/GoloMarcos/OCTCMG/

from OneClassTextCollectionsLibrary import datasets

datasets_dictionary = datasets.load()

# The Dataframe of each text collection return (datasets_dictionary[base name]):

- News Id 
- News Date
- News Title

# One-Class Text Collections

- Restaurant | Opera | Employee | Logistics | Imports | Flood | Tariff | Court | Children  | Series | Metal | Ethics  
- War | Investments | School | Revolution | Society | People | Justice | Therapy | Marathon | Adults | Theft 
- University | Gender | Assault | Traffic | Retail | Medicare | Stocks | Massacre | Water | Rivers | Lifestyle 
- Welfare | Media | Impeachment | Illness | Fishing | Wedding | Fraud | Teachers | Pope | Fashion | Fire | Terrorism 
- Environment | Currency | Television | Social-media | Boxing | Architecture | Birthday | Theatre | Fiction | Politics 
- Drought | Arrest | Charity | Mosque | Police | Disaster | Sailing | Tobacco | Transfer | Education | Cancer | Students 
- Diet | Pension |Cinema | Advertising | Pandemic | Retirement | Radio | Judge | Newspaper | Medicine | Bonds 
- Animal | Coal | Surveillance | Ceremony | Management | Loans | Suicide | Democracy | Golf | Medicaid | Drama 
- Arson | Trend | Immigration | Labour | Automotive | Festival | Prison | Investigation | Exports | Tourism 
- Petrol | Language | Party | Prices | Parliament | Bullying | Poverty | Banking | Weather | Dance | Election | Holiday 
- Crime | Vaccines | Health | Recession | Employment | Music | College | Wildfire | Celebrity | Beverage | Mortgage 
- Abortion | Halloween | Bribery | Securities | Software | LGBTQ | Government | Economy | Shareholder | Witness 
- Mining | Transport | Discrimination | Divorce | Toy | Agriculture | Defence | Hospital | Epidemic | Farms | Earnings 
- Christmas | Family | Culture | Racism | Surgery | Privacy | Adoption | Kidnapping | Marriage | Grocery 
- Rugby | Unemployment | Parks | Voting | Bar | Constitution | Unions | Design | Church | Law | Musical  
- Insurance | Anniversary | Sport | Game | Homicide | Bankruptcy | Inflation | Easter | Nature | Cafe | Hunting 
- Volleyball | Hurricane | Regulations | Plant | Earthquake | Painting | Consumers
