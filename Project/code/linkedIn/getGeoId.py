import codecs      #swedish alphabet
from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import platform
import time


def find_path(platform):
    match platform:
        case "linux":
            return 'Project/code/linkedIn/geo_ids.txt'
        case "darwin":
            return 'Project/code/linkedIn/geo_ids.txt'
        case _:
            return 'Project\code\linkedIn\geo_ids.txt'

 
url = 'https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0'
driver = webdriver.Firefox()
driver.get(url)

municipalities = ["Upplands Väsby, Stockholm", "Vallentuna, Stockholm", "Österåker, Stockholm", "Värmdö, Stockholm", "Järfälla, Stockholm", "Ekerö, Stockholm", "Huddinge, Stockholm", "Botkyrka, Stockholm", "Salem, Stockholm", "Haninge, Stockholm", "Tyresö, Stockholm", "Upplands-Bro, Stockholm", "Nykvarn, Stockholm", "Täby, Stockholm", "Danderyd, Stockholm", "Sollentuna, Stockholm", "Stockholm, Stockholm", "Södertälje, Stockholm", "Nacka, Stockholm", "Sundbyberg, Stockholm", "Solna, Stockholm", "Lidingö, Stockholm", "Vaxholm, Stockholm", "Norrtälje, Stockholm", "Sigtuna, Stockholm", "Nynäshamn, Stockholm", "Håbo, Uppsala", "Älvkarleby, Uppsala", "Knivsta, Uppsala", "Heby, Uppsala", "Tierp, Uppsala", "Uppsala, Uppsala", "Enköping, Uppsala", "Östhammar, Uppsala", "Vingåker, Södermanland", "Gnesta, Södermanland", "Nyköping, Södermanland", "Oxelösund, Södermanland", "Flen, Södermanland", "Katrineholm, Södermanland", "Eskilstuna, Södermanland", "Strängnäs, Södermanland", "Trosa, Södermanland", "Ödeshög, Östergötland", "Ydre, Östergötland", "Kinda, Östergötland", "Boxholm, Östergötland", "Åtvidaberg, Östergötland", "Finspång, Östergötland", "Valdemarsvik, Östergötland", "Linköping, Östergötland", "Norrköping, Östergötland", "Söderköping, Östergötland", "Motala, Östergötland", "Vadstena, Östergötland", "Mjölby, Östergötland", "Aneby, Jönköping", "Gnosjö, Jönköping", "Mullsjö, Jönköping", "Habo, Jönköping", "Gislaved, Jönköping", "Vaggeryd, Jönköping", "Jönköping, Jönköping", "Nässjö, Jönköping", "Värnamo, Jönköping", "Sävsjö, Jönköping", "Vetlanda, Jönköping", "Eksjö, Jönköping", "Tranås, Jönköping", "Lessebo, Kronoberg", "Tingsryd, Kronoberg", "Alvesta, Kronoberg", "Älmhult, Kronoberg", "Markaryd, Kronoberg", "Växjö, Kronoberg", "Ljungby, Kronoberg", "Högsby, Kalmar", "Torsås, Kalmar", "Mörbylånga, Kalmar", "Hultsfred, Kalmar", "Mönsterås, Kalmar", "Emmaboda, Kalmar", "Kalmar, Kalmar", "Nybro, Kalmar", "Oskarshamn, Kalmar", "Västervik, Kalmar", "Vimmerby, Kalmar", "Borgholm, Kalmar", "Gotland, Gotland", "Olofström, Blekinge", "Karlskrona, Blekinge", "Ronneby, Blekinge", "Karlshamn, Blekinge", "Sölvesborg, Blekinge", "Svalöv, Skåne", "Staffanstorp, Skåne", "Burlöv, Skåne", "Vellinge, Skåne", "Östra Göinge, Skåne", "Örkelljunga, Skåne", "Bjuv, Skåne", "Kävlinge, Skåne", "Lomma, Skåne", "Svedala, Skåne", "Skurup, Skåne", "Sjöbo, Skåne", "Hörby, Skåne", "Höör, Skåne", "Tomelilla, Skåne", "Bromölla, Skåne", "Osby, Skåne", "Perstorp, Skåne", "Klippan, Skåne", "Åstorp, Skåne", "Båstad, Skåne", "Malmö, Skåne", "Lund, Skåne", "Landskrona, Skåne", "Helsingborg, Skåne", "Höganäs, Skåne", "Eslöv, Skåne", "Ystad, Skåne", "Trelleborg, Skåne", "Kristianstad, Skåne", "Simrishamn, Skåne", "Ängelholm, Skåne", "Hässleholm, Skåne",  "Hylte, Halland", "Halmstad, Halland", "Laholm, Halland", "Falkenberg, Halland", "Varberg, Halland", "Kungsbacka, Halland", "Arvidsjaur, Norrbotten", "Arjeplog, Norrbotten", "Jokkmokk, Norrbotten", "Överkalix, Norrbotten", "Kalix, Norrbotten", "Övertorneå, Norrbotten", "Pajala, Norrbotten", "Gällivare, Norrbotten", "Älvsbyn, Norrbotten", "Luleå, Norrbotten", "Piteå, Norrbotten", "Boden, Norrbotten", "Haparanda, Norrbotten", "Kiruna, Norrbotten", "Nordmaling, Västerbotten", "Bjurholm, Västerbotten", "Vindeln, Västerbotten", "Robertsfors, Västerbotten", "Norsjö, Västerbotten", "Malå, Västerbotten", "Storuman, Västerbotten", "Sorsele, Västerbotten", "Dorotea, Västerbotten", "Vännäs, Västerbotten", "Vilhelmina, Västerbotten", "Åsele, Västerbotten", "Umeå, Västerbotten", "Lycksele, Västerbotten", "Skellefteå, Västerbotten", "Ragunda, Jämtland", "Bräcke, Jämtland", "Krokom, Jämtland", "Strömsund, Jämtland", "Åre, Jämtland", "Berg, Jämtland", "Härjedalen, Jämtland", "Östersund, Jämtland", "Ånge, Västernorrland", "Timrå, Västernorrland", "Härnösand, Västernorrland", "Sundsvall, Västernorrland", "Kramfors, Västernorrland", "Sollefteå, Västernorrland", "Örnsköldsvik, Västernorrland", "Ockelbo, Gävleborg", "Hofors, Gävleborg", "Ovanåker, Gävleborg", "Nordanstig, Gävleborg", "Ljusdal, Gävleborg", "Gävle, Gävleborg", "Sandviken, Gävleborg", "Söderhamn, Gävleborg", "Bollnäs, Gävleborg", "Hudiksvall, Gävleborg", "Vansbro, Dalarna", "Malung-Sälen, Dalarna", "Gagnef, Dalarna", "Leksand, Dalarna", "Rättvik, Dalarna", "Orsa, Dalarna", "Älvdalen, Dalarna", "Smedjebacken, Dalarna", "Mora, Dalarna", "Falun, Dalarna", "Borlänge, Dalarna", "Säter, Dalarna", "Hedemora, Dalarna", "Avesta, Dalarna", "Ludvika, Dalarna", "Skinnskatteberg, Västmanland", "Surahammar, Västmanland", "Kungsör, Västmanland", "Hallstahammar, Västmanland", "Norberg, Västmanland", "Västerås, Västmanland", "Sala, Västmanland", "Fagersta, Västmanland", "Köping, Västmanland", "Arboga, Västmanland", "Laxå, Örebro", "Lekeberg, Örebro", "Hallsberg, Örebro", "Degerfors, Örebro", "Hällefors, Örebro", "Örebro, Örebro", "Kumla, Örebro", "Askersund, Örebro", "Karlskoga, Örebro", "Nora, Örebro", "Lindesberg, Örebro", "Kil, Värmland", "Eda, Värmland", "Torsby, Värmland", "Storfors, Värmland", "Hammarö, Värmland", "Munkfors, Värmland", "Forshaga, Värmland", "Grums, Värmland", "Årjäng, Värmland", "Sunne, Värmland", "Karlstad, Värmland", "Kristinehamn, Värmland", "Filipstad, Värmland", "Hagfors, Värmland", "Arvika, Värmland", "Säffle, Värmland", "Härryda, Västra Götaland", "Partille, Västra Götaland", "Öckerö, Västra Götaland", "Stenungsund, Västra Götaland", "Tjörn, Västra Götaland", "Orust, Västra Götaland", "Sotenäs, Västra Götaland", "Munkedal, Västra Götaland", "Tanum, Västra Götaland", "Dals-Ed, Västra Götaland", "Färgelanda, Västra Götaland", "Ale, Västra Götaland", "Lerum, Västra Götaland", "Vårgårda, Västra Götaland", "Bollebygd, Västra Götaland", "Grästorp, Västra Götaland", "Essunga, Västra Götaland", "Karlsborg, Västra Götaland", "Gullspång, Västra Götaland", "Tranemo, Västra Götaland", "Bengtsfors, Västra Götaland", "Mellerud, Västra Götaland", "Lilla Edet, Västra Götaland", "Mark, Västra Götaland", "Svenljunga, Västra Götaland", "Herrljunga, Västra Götaland", "Vara, Västra Götaland", "Götene, Västra Götaland", "Tibro, Västra Götaland", "Töreboda, Västra Götaland", "Göteborg, Västra Götaland", "Mölndal, Västra Götaland", "Kungälv, Västra Götaland", "Lysekil, Västra Götaland", "Uddevalla, Västra Götaland", "Strömstad, Västra Götaland", "Vänersborg, Västra Götaland", "Trollhättan, Västra Götaland", "Alingsås, Västra Götaland", "Borås, Västra Götaland", "Ulricehamn, Västra Götaland", "Åmål, Västra Götaland", "Mariestad, Västra Götaland", "Lidköping, Västra Götaland", "Skara, Västra Götaland", "Skövde, Västra Götaland", "Hjo, Västra Götaland", "Tidaholm, Västra Götaland", "Falköping, Västra Götaland"]

#Identifies the searchbar
searchbar = driver.find_element(By.XPATH, ("//input[@id='job-search-bar-location']"))

file_path = find_path(platform)

file = codecs.open(file_path,'w', 'utf-8')
for muni in municipalities:
    # Writes a municipality
    searchbar.clear()
    searchbar.send_keys(muni)
    time.sleep(5)

    #Find and store the geo_id for the current municipality
    geo_id = driver.find_element(By.XPATH, ("//li[@id='location-1']/span")).get_attribute("data-id")
    file.write("{"+ geo_id +", "+ muni +"}\n")

file.close()


# Existerar ej: "Uppvidinge, Kronoberg", och "Ljusnarsberg, Örebro"

# Has two Geo id's: "Göteborg, Västra Götaland" (One is a radius, and one is functional)

# Geo id's that gives ad in a radius (mostly duplicate ads): 
# [Use only "{104312072, Täby, Stockholm}" instead of these] "Vallentuna, Stockholm", "Ekerö, Stockholm", "Tyresö, Stockholm", "Täby, Stockholm", "Danderyd, Stockholm", "Sollentuna, Stockholm", "Nacka, Stockholm", "Sundbyberg, Stockholm", "Solna, Stockholm", "Vaxholm, Stockholm", "Nynäshamn, Stockholm", 
# "{104792890, Gnesta, Södermanland}", 
# "{104640929, Mullsjö, Jönköping}", 
# [Use only "{101759788, Malmö, Skåne}" instead of these] "Vellinge, Skåne", "Kävlinge, Skåne", "Perstorp, Skåne", "Åstorp, Skåne", "Malmö, Skåne", "Lund, Skåne", 
# [Don't use] "Boden, Norrbottens", 
# [Use only "{105391169, Östersund, Jämtland}" instead of these] "Bräcke, Jämtland", "Östersund, Jämtland", 
# [Don't use] "Timrå, Västernorrland", 
# [Use only "{116351998, Falun, Dalarna}" instead of these] "Falun, Dalarna", "Ludvika, Dalarna", 
# [Use only "{112614768, Lekeberg, Örebro}" instead of these] "Lekeberg, Örebro", "Hallsberg, Örebro", "Nora, Örebro", 
# [Use only "{104448936, Kil, Värmland}" instead of theese] "Kil, Värmland", "Hammarö, Värmland", "Munkfors, Värmland", "Grums, Värmland", 
# "Skövde, Västra Götaland, "Alingsås, Västra Götaland", "Trollhättan, Västra Götaland", "Mölndal, Västra Götaland", "Göteborg, Västra Götaland", "Essunga, Västra Götaland", "Tjörn, Västra Götaland", "Partille, Västra Götaland"