from GoogleNews import GoogleNews
import pandas as pd

googlenews = GoogleNews()

googlenews.set_lang('tr')
googlenews.set_time_range('06/02/2023','16/02/2023')
googlenews.set_encode('utf-8')
googlenews.get_news('deprem')

dataset_link = googlenews.get_links()
dataset_text = googlenews.get_texts()

print(len(dataset_link))
print(len(dataset_text))

total_data = pd.DataFrame(zip(dataset_text, dataset_link), columns=['news', 'link'])
total_data.to_csv("earthquake-dataset.csv")