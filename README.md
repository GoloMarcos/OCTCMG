# OCTCMG

One-Class Text Collections From Marcos Gôlo

# Informations

Essas coleções textuais one-class são formadas por títulos de notícias retiradas do projeto GDELT (Global Database of Events, Language, and Tone). Os tópicos relacionados a cada coleção textual foram escolhidos com base na taxonomia do IPTC (International Press Telecommunications Council). O projeto GDELT se encontra em https://www.gdeltproject.org/ e todos os tópicos do IPTC em https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html. A coleta das notícias foi feita verificando se notícias continham o tópico em seu título. Tópicos que retornaram menos que 4000 notícias não foram considerados como coleção textual. Foi definido o limite de 6000 notícias para todas as coleções textuais. Por fim, foram obtidas 183 coleções textuais. 

# How to Use

!pip install git+https://github.com/GoloMarcos/OCTCMG/

from OneClassTextCollectionsLibrary import datasets

datasets_dictionary = datasets.load()

# Dataframe de cada coleção textual == datasets_dictionary[base name]

- Id da notícia
- Data da notícia
- Título da notícia

# Tópicos de cada coleção textual

-Restaurant 
-Opera 
-Employee 
-Logistics 
-Imports 
-Flood 
-Tariff 
-Court 
-Children 
-Series 
-Metal 
-Ethics 
-Rugby 
-Painting 
-War 
-Investments 
-School 
-Revolution 
-Society 
-People 
-Justice 
-Therapy 
-Marathon 
-Adults 
-Theft 
-Unemployment 
-Parks 
-Grocery 
-University 
-Gender 
-Assault
-Traffic 
-Retail 
-Medicare 
-Stocks 
-Massacre 
-Water 
-Rivers 
-Lifestyle 
-Voting 
-Bar 
-Earthquake 
-Welfare 
-Media 
-Impeachment 
-Illness 
-Fishing 
-Wedding 
-Fraud 
-Teachers 
-Pope 
-Fashion 
-Fire 
-Terrorism 
-Constitution 
-Unions 
-Environment 
-Currency 
-Television 
-Social-media 
-Boxing 
-Architecture 
-Birthday 
-Theatre 
-Fiction 
-Politics 
-Design 
-Church 
-Christmas 
-Drought 
-Arrest 
-Charity 
-Mosque 
-Police 
-Disaster 
-Sailing 
-Tobacco 
-Transfer 
-Education 
-Cancer 
-Students 
-Law 
-Musical 
-Family 
-Diet 
-Pension 
-Cinema 
-Advertising 
-Pandemic 
-Retirement 
-Radio 
-Judge 
-Newspaper 
-Medicine 
-Bonds 
-Volleyball 
-Consumers 
-Culture 
-Animal 
-Coal 
-Surveillance 
-Ceremony 
-Management 
-Loans 
-Suicide 
-Democracy 
-Golf 
-Medicaid 
-Drama 
-Hurricane 
-Insurance 
-Racism 
-Arson 
-Trend 
-Immigration 
-Labour 
-Automotive 
-Festival 
-Prison 
-Investigation 
-Exports 
-Tourism 
-Regulations
-Anniversary 
-Surgery 
-Petrol 
-Language 
-Party 
-Prices 
-Parliament 
-Bullying 
-Poverty 
-Banking 
-Weather 
-Dance 
-Election 
-Holiday 
-Sport 
-Game 
-Privacy 
-Crime 
-Vaccines 
-Health 
-Recession 
-Employment 
-Music 
-College 
-Wildfire 
-Celebrity 
-Beverage 
-Mortgage 
-Homicide 
-Bankruptcy 
-Adoption 
-Abortion 
-Halloween 
-Bribery 
-Securities 
-Software 
-LGBTQ 
-Government 
-Economy 
-Shareholder 
-Witness 
-Plant 
-Inflation 
-Easter 
-Kidnapping 
-Mining 
-Transport 
-Discrimination 
-Divorce 
-Toy 
-Agriculture 
-Defence 
-Hospital 
-Epidemic 
-Farms 
-Earnings 
-Nature 
-Cafe 
-Hunting 
-Marriage
