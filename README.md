# OpenSubtitles Scraper API

This repository contains a Python script for scraping subtitles from OpenSubtitles.org. It is designed to be deployed as an API on Vercel.

## Features

- Search for movie and TV show subtitles and get a JSON structured response.
- Customize the language code, number of subtitles fetched, and subtitle name via `utils.py`.

## Usage

Deploy this repository directly on Vercel by clicking here: [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Ftiagosilvadeveloper%2Fopensubtitles-scraper-api)

Once deployed, you can use the following endpoints:

- For movies: `{https://myapi.vercel.com}/movie/{title}/{year}`
> (e.g. [https://opensubtitles-scraper-api.vercel.app/movie/Interstellar/2014](https://opensubtitles-scraper-api.vercel.app/movie/Interstellar/2014))
- For TV shows: `{https://myapi.vercel.com}/tv/{title}/{year}/{seasonNumber}/{episodeNumber}`
> (e.g. [https://opensubtitles-scraper-api.vercel.app/tv/The-Last-of-Us/2023/1/5](https://opensubtitles-scraper-api.vercel.app/tv/The%20Last%20of%20Us/2023/1/5))

Replace `{https://myapi.vercel.com}`, `{title}`, `{year}`, `{seasonNumber}`, and `{episodeNumber}` with your desired parameters.

## Configuration

You can customize the behavior of the API by modifying the `utils.py` file:

- `language_code`: Change this to the desired [ISO 639-2 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) for the subtitles.
- `subtitles_number`: Change this to the number of subtitles you want the API to fetch.
- `subtitle_name`: Change this to customize the `lang` key that will appear in the JSON response.

## License

[MIT](https://github.com/tiagosilvadeveloper/opensubtitles-scrapper/blob/main/LICENSE)
