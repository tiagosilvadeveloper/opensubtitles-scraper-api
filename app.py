import requests
import re
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
from utils import language_code, subtitles_number, subtitle_name

app = Flask(__name__)
CORS(app)


def get_subtitles(session, title, year, max_subtitles):
  cleaned_title = title.replace('-', '+')
  url = f"https://www.opensubtitles.org/en/search2?MovieName={cleaned_title}&id=8&action=search&SubLanguageID={language_code}&SearchOnlyMovies=on&MovieImdbRatingSign=1&MovieYearSign=1&MovieYear={year}/sort-7/asc-0"
  response = session.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  links = soup.select('a[href^="/en/subtitles/"]')

  if not links:
    new_link = soup.select_one(
        f'a[href^="/en/search/sublanguageid-{language_code}/"]')
    if new_link:
      new_link = f"https://www.opensubtitles.org{new_link['href']}/sort-7/asc-0"
      response = session.get(new_link)
      soup = BeautifulSoup(response.text, 'html.parser')
      links = soup.select('a[href^="/en/subtitles/"]')

  subtitles = []
  for link in links[:max_subtitles]:
    subtitle_url = f"https://www.opensubtitles.org{link['href']}"
    download_link = get_download_link(session, subtitle_url)
    if download_link:
      subtitles.append({
          'url':
          download_link,
          'lang':
          f'{subtitle_name} {len(subtitles) + 1}'
      })
  return subtitles


def get_download_link(session, url):
  response = session.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  download_link = soup.find(
      'a', {
          'class': 'none',
          'href':
          re.compile(r'^https://dl.opensubtitles.org/en/download/file/')
      })
  if download_link:
    return download_link['href'] + '.srt'
  else:
    return None


def get_subtitles_tv(session, season, episode, title, year, max_subtitles):
  cleaned_title = title.replace('-', '+')
  url = f"https://www.opensubtitles.org/en/search/sublanguageid-{language_code}/searchonlytvseries-on/season-{season}/episode-{episode}/fixinput-on/movieyearsign-5/movieyear-{year}//moviename-{cleaned_title}/sort-7/asc-0"
  response = session.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  links = soup.select('a[href^="/en/subtitles/"]')

  subtitles = []
  if links:
      for link in links[:max_subtitles]:
          subtitle_url = f"https://www.opensubtitles.org{link['href']}"
          download_link = get_download_link(session, subtitle_url)
          if download_link:
              subtitles.append({
                  'url': download_link,
                  'lang': f'{subtitle_name} {len(subtitles) + 1}'
              })
  else:
      download_link = get_download_link(session, url)
      if download_link:
          subtitles.append({
              'url': download_link,
              'lang': f'{subtitle_name} {len(subtitles) + 1}'
          })
  return subtitles


@app.route('/tv/<title>/<year>/<season>/<episode>')
def fetch_subtitlestv(season, episode, title, year):
  with requests.Session() as s:
    subtitles = get_subtitles_tv(s, season, episode, title, year, max_subtitles=subtitles_number)
  return jsonify({"subtitles": subtitles})


@app.route('/movie/<title>/<year>')
def fetch_subtitles(title, year):
  with requests.Session() as s:
    subtitles = get_subtitles(s, title, year, max_subtitles=subtitles_number)
  return jsonify({"subtitles": subtitles})


@app.route('/')
def welcome():
    return "Welcome to the OpenSubtitles Scraper API"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
