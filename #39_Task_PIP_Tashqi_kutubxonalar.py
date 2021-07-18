# from googletrans import Translator
# tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
# matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
# tarjima = tarjimon.translate(matn_uz)
# print(tarjima.text)
#import requests
#from pprint import pprint

# manzil= "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)
# country = "Uzbekistan"
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# r = requests.get(url)
# r_json = r.json()[0]
# print(r_json['capital'])

# import requests
# from bs4 import BeautifulSoup

# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)


# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title") # yangiliklarning mavzusini ajratib olamiz
# print(news[0].text) # eng birinchi yangilikni konsolga chiqaramiz


# import requests

# from bs4 import BeautifulSoup
# from wordcloud import WordCloud 
# import matplotlib.pyplot as plt 


# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)

# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title")
# matn=""
# for n in news:
#     matn += n.text

# # kerakmas so'zlar
# stopwords = ["учун","бўйича","лекин","билан","ва","бор","ҳам","хил","йил"]
# # bulutni yaratamiz
# wordcloud = WordCloud(width = 1000, height = 1000, 
#                 background_color ='white', 
#                 stopwords = stopwords, 
#                 min_font_size = 20).generate(matn) 
  
# # plot the WordCloud image                        
# plt.figure(figsize = (8, 8), facecolor = None) 
# plt.imshow(wordcloud) 
# plt.axis("off") 
# plt.tight_layout(pad = 0) 
# plt.show() 
# from fuzzywuzzy import fuzz
# print(fuzz.ratio("salom",'assalom'))
# print(fuzz.ratio("salom","salim"))
# from fuzzywuzzy import process
# from uzwords import words

# # Matnlar orasidan 3 ta eng o'xshashlarini ajratib olish
# text = "салом"
# matches = process.extract(text, words, limit=3)
# print(matches)



# import wx
# from googletrans import Translator

# tarjimon = Translator()
# class MyFrame(wx.Frame):    
#     def __init__(self):
#         super().__init__(parent=None, title='Oʻzbek-Ingliz Lugʻat')
#         panel = wx.Panel(self)        
#         my_sizer = wx.BoxSizer(wx.VERTICAL)        
#         self.text_ctrl = wx.TextCtrl(panel)
#         my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        
#         my_btn = wx.Button(panel, label='TARJIMA')
#         my_btn.Bind(wx.EVT_BUTTON, self.on_press)
#         my_sizer.Add(my_btn,0,  wx.ALL | wx.CENTER, 5)        
        
#         self.text_out = wx.TextCtrl(panel,style = wx.TE_READONLY)        
#         my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)         
#         panel.SetSizer(my_sizer)        
#         self.Show()

#     def on_press(self, event):
#         value = self.text_ctrl.GetValue()
#         if not value:                       
#             self.text_out.SetValue("Soʻz kiritmadingiz")
#         else:
#             tarjima = tarjimon.translate(value, src='uz', dest='en')
#             self.text_out.SetValue(tarjima.text.capitalize()) 
    

# if __name__ == '__main__':
#     app = wx.App()
#     frame = MyFrame()
#     app.MainLoop()
