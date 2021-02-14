---
title: CDS project idea
author: Mikkel Plesner Ottosen & Magnus Bendix Borregaard
date: 05-10-2020
---

# CDS Project idea

###### Mikkel Plesner Ottosen & Magnus Bendix Borregaard

###### 05-10-2020

## The data

On [data.europa.eu](https://data.europa.eu/euodp/da/data/dataset/covid-19-coronavirus-data/resource/260bbbde-2316-40eb-aec3-7cd7bfc2f590 'EU official data portal') one can download a variety of datasets about almost anything. One of these datasets is a .CSV file containing data about covid-19 and how it developed throughout the world.

Each row represents a day and thus the dataset contains the amount of people getting covid-19 each day in each country.

### Specification

The set contains the following columns:

- `Date`: ​The date of the data-row with the format DD/MM/YY
- `Day`,
- `Month`,
- `Year`: ​for individual parts of the date.
- `Cases`: ​The amount of cases for the given day as an integer
- `Deaths`: ​The amount of deaths for the given day as an integer
- `CountriesAndTerritories`: ​The country of the incident as a text-string
- `GeoId`: ​The id of the location. Ex: AF for Afghanistan
- `CountryterritoryCode`: ​The code of the location. Ex: AFG for Afghanistan.
- `popData2019`: ​Population number from 2019
- `ContinentExp`: ​The continent of the location. Ex Asia
- `Cumulative_number_for_14_days_of_COVID-19_cases_per_100000`: ​Cases per 100000.

## The concept

This dataset allows for a lot of different applications. Our main goal is to visualize the dataset as a graph. A graph is a set of nodes and vertices (connections or lines between nodes). We can then create these vertices between nodes and display the gravitational pull of certain nodes. If a node is very entangled in the dataset as a whole, it will generate a lot of pull and be able to tell us what actors played a larger role and when in terms of Covid-19. It could be interesting to target Dates as nodes and then visualize what dates were the worst, but we also want to include the countries and locations in some way and then try to represent both the countries and the dates in the graph.

We could also cross-reference the dataset with another dataset that shows borders and location of borders between countries in order to somehow incorporate that into the graph to maybe show how / if the virus spreads across country borders primarily.

### Gui

Since we have some experience in creating graphic user interfaces, we want to create some sort of application that allows a user to work the dataset. At the current time, we do not know how big a task this would be, so this is just an idea that could be cool to expand on if possible.
