# OCTCMG

One-Class Text Collections From Marcos Gôlo

# Citing:

If you use any part of this code or the datasets in your research, please cite it using the following BibTex entry
```latex
@article{ref:Golo2021,
  title={Learning to sense from events via semantic variational autoencoder},
  author={Gôlo, Marcos Paulo Silva and Rossi, Rafael Geraldeli and Marcacini, Ricardo Marcondes},
  journal={Plos one},
  volume={16},
  number={12},
  pages={e0260701},
  year={2021},
  publisher={Public Library of Science San Francisco, CA USA}
}
```

# Informations

I collect these one-class text collections with my advisor Ricardo Marcondes Marcacini. We built these one-class text collections by the news titles from the project Global Database of Events, Language, and Tone (GDELT). We chose the topics related to each textual collection based on the International Press Telecommunications Council (IPTC) taxonomy. You can find the GDELT project at https://www.gdeltproject.org/ and all IPTC topics at https://www.iptc.org/std/NewsCodes/treeview/mediatopic/mediatopic-en-GB.html. The collection of the news was made by checking if the news contained the topic in its title. I did not consider topics that returned less than 4000 news items. Furthermore, I define the limit of 6000 news items has for all text collections. Finally, we obtain 183 text collections.

# How to Use

!pip install git+https://github.com/GoloMarcos/OCTCMG/

from OneClassTextCollectionsLibrary import datasets

datasets_dictionary = datasets.load()

# Parameters from load()

- path: path of collections 
- download_only: a boolean parameter to download the collections but not load
- dataset: a parameter to load only one collection, informing your name

# The Dataframe of each text collection return (datasets_dictionary[base name]):

- News Id 
- News Date
- News Title
- News Embeddings from BERT
- News Embeddings from DistilBERT
- News Embeddings from DistilBERT Multilingual
- News Embeddings from RoBERTa
- Class (interest or outlier)
  - the outliers are texts from the 182 other collections
  - the length of outliers are similar to 10% of the length of the texts of the class of interest 


# We obtain the embeddings with the library sentence_tranformers
- BERT model: bert-large-nli-stsb-mean-tokens
  -  Devlin, Jacob, et al. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). 2019.
- DistilBERT model: distilbert-base-nli-stsb-mean-tokens
  -  Sanh, Victor, et al. "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter." arXiv preprint arXiv:1910.01108 (2019).
- RoBERTa model: roberta-large-nli-stsb-mean-tokens
  - Liu, Yinhan, et al. "Roberta: A robustly optimized bert pretraining approach." arXiv preprint arXiv:1907.11692 (2019).
- DistilBERT Multilingual model: distiluse-base-multilingual-cased
  - Sanh, Victor, et al. "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter." arXiv preprint arXiv:1910.01108 (2019).

# One-Class Text Collections Topics

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
