Untappd-wrapper
===============

Python wrapper for the [Untappd API](https://untappd.com/api). Developed for personal consumption and visualization in [Tableau](https://public.tableau.com/profile/andy.miller#!/vizhome/PittsburghBrewingScene/PittsburghCraftBrewing).

## Overview

This library is simply a wrapper to connect to and parse the api data.  The script downloads, flattens and prepares the data for Tableau.

## How to Use

Get setup with the [Google Sheets API](https://developers.google.com/sheets/api/quickstart/python), which is needed for Get_Brewery_Info.py.  For Untappd, ensure you have an API key from the [Untappd API](https://untappd.com/api/dashboard) (you need to register an App).  Once you have this information, complete the "crednetials.yml.example" file and remove ".example" from the file name.

Once squared away with the various APIs (Google Sheets and Untappd), you can run the two files "Get_Brewery_IDs.py" then "Get_Brewery_Info.py".