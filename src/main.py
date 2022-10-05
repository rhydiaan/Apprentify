from webscraper import Scraper
from utils import *
import time
import requests

urls = {
    'advanced' : 'https://www.findapprenticeship.service.gov.uk/apprenticeships?SearchField=JobTitle&Keywords=Software%20developer&Location=SA16%200EH&WithinDistance=0&ApprenticeshipLevel=Advanced&DisabilityConfidentOnly=false&Latitude=51.687928&Longitude=-4.270008&Hash=226003117&SearchMode=Keyword&Category=&LocationType=NonNational&GoogleMapApiKey=AIzaSyAg5lwS3ugdAVGf5gdgNvLe_0-7XcMICIM&sortType=RecentlyAdded&SearchAction=Sort&resultsPerPage=1&DisplayDescription=true&DisplayDistance=true&DisplayClosingDate=true&DisplayStartDate=true&DisplayApprenticeshipLevel=false&DisplayWage=true',
    'higher' : 'https://www.findapprenticeship.service.gov.uk/apprenticeships?SearchField=JobTitle&Keywords=Software%20developer&Location=SA16%200EH&WithinDistance=0&ApprenticeshipLevel=Higher&DisabilityConfidentOnly=false&Latitude=51.687928&Longitude=-4.270008&Hash=226003117&SearchMode=Keyword&Category=&LocationType=NonNational&GoogleMapApiKey=AIzaSyAg5lwS3ugdAVGf5gdgNvLe_0-7XcMICIM&sortType=RecentlyAdded&SearchAction=Sort&resultsPerPage=1&DisplayDescription=true&DisplayDistance=true&DisplayClosingDate=true&DisplayStartDate=true&DisplayApprenticeshipLevel=false&DisplayWage=true'
    }

init_schema = {
    'advanced' : 0,
    'higher' : 0
}

xpath = {'id': '/html/body/div[4]/main/div[3]/div[2]/form/section[2]/div/ul/li/h2/a',
'jt_click' : '/html/body/div[4]/main/div[3]/div[2]/form/section[2]/div/ul/li/div/div[1]/ul/li[1]/a',
'time' : '/html/body/div[4]/main/div[3]/div[2]/form/section[2]/div/ul/li/div/div[1]/ul/li[1]/div/span',
'wage' : '/html/body/div[4]/main/div[3]/div[2]/form/section[2]/div/ul/li/div/div[1]/ul/li[5]'
}


my_scraper: Scraper = Scraper()
db = Data('id.json', init_schema)


def main():
    read_data = db.read()
    write_data = read_data
    for key, url in urls.items():
        id = my_scraper.open_instance_get_id(url, xpath['id'])
        if read_data[key] < id:
            write_data[key] = id
            db.write(write_data)
            send_notification(key, my_scraper.find_time_from_me(url, xpath['jt_click'], xpath['time']), my_scraper.find_element_text(url, xpath['wage']))
    print('Sleeping... Zzzzz')
    time.sleep(1800)
    main()


def send_notification(level, time_to_location, wage):
    request = {
        
    "title":f"Oi! New apprenticeship {time_to_location} away!",
    "content":f"Level: {level.title()} {wage}"
    
    }
    return requests.post(url='http://192.168.1.200:8080/notification', data=json.dumps(request))


main()





########################################################################################################
#   Copyright (C) 2022  Rhydian Davies
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
