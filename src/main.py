from webscraper import Scraper
from utils import *

urls = {
    'advanced' : 'https://www.findapprenticeship.service.gov.uk/apprenticeships?SearchField=JobTitle&Keywords=Software%20developer&Location=SA16%200EH&WithinDistance=0&ApprenticeshipLevel=Advanced&DisabilityConfidentOnly=false&Latitude=51.687928&Longitude=-4.270008&Hash=226003117&SearchMode=Keyword&Category=&LocationType=NonNational&GoogleMapApiKey=AIzaSyAg5lwS3ugdAVGf5gdgNvLe_0-7XcMICIM&sortType=RecentlyAdded&SearchAction=Sort&resultsPerPage=1&DisplayDescription=true&DisplayDistance=true&DisplayClosingDate=true&DisplayStartDate=true&DisplayApprenticeshipLevel=false&DisplayWage=true',
    'higher' : 'https://www.findapprenticeship.service.gov.uk/apprenticeships?SearchField=JobTitle&Keywords=Software%20developer&Location=SA16%200EH&WithinDistance=0&ApprenticeshipLevel=Higher&DisabilityConfidentOnly=false&Latitude=51.687928&Longitude=-4.270008&Hash=226003117&SearchMode=Keyword&Category=&LocationType=NonNational&GoogleMapApiKey=AIzaSyAg5lwS3ugdAVGf5gdgNvLe_0-7XcMICIM&sortType=RecentlyAdded&SearchAction=Sort&resultsPerPage=1&DisplayDescription=true&DisplayDistance=true&DisplayClosingDate=true&DisplayStartDate=true&DisplayApprenticeshipLevel=false&DisplayWage=true'
    }


my_scraper: Scraper = Scraper()


def main():
    data = {}
    for key, url in urls.items():
        data[key] = my_scraper.open_instance_get_id(url, '/html/body/div[4]/main/div[3]/div[2]/form/section[2]/div/ul/li/h2/a')
    write_to_json(data, 'id.json')



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
