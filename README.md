# OpenSubtitles Scraper

This repository contains a Python script for scraping subtitles from OpenSubtitles.org. It is designed to be deployed as an API on Vercel.

## Features

- Search for movie and TV show subtitles.
- Customize the language code, number of subtitles fetched, and subtitle name via `utils.py`.

## Usage

Deploy this repository on Vercel. Once deployed, you can use the following endpoints:

- For movies: `https://myapi.vercel.com/opensubs/movie/{title}/{year}/`
- For TV shows: `https://myapi.vercel.com/opensubs/tv/{title}/{seasonNumber}/{episodeNumber}/`

Replace `{title}`, `{year}`, `{seasonNumber}`, and `{episodeNumber}` with your desired parameters.

## Configuration

You can customize the behavior of the API by modifying the `utils.py` file:

- `language_code`: Change this to the desired [ISO 639-2 language code]([www.google.com](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes)) for the subtitles.
- `subtitles_number`: Change this to the number of subtitles you want the API to fetch.
- `subtitle_name`: Change this to customize the `lang` key that will appear in the JSON response.

## License

MIT
