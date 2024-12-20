# IMDb Movie Data Analysis

## Project Overview

This project, developed in Python, performs a basic data analysis of IMDb movie data. The dataset, sourced from Kaggle ([IMDb Movie Dataset](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)), includes various attributes of movies like title, release year, director, budget, and IMDb score, among others. The project explores different analytical methods and techniques, focusing on extracting insights, identifying patterns, and creating visualizations for movie data analysis.

- [IMDb Movie Data Analysis](#imdb-movie-data-analysis)
  - [Project Overview](#project-overview)
  - [Key Objectives](#key-objectives)
  - [Dataset](#dataset)
  - [Project Structure](#project-structure)
  - [Methods and Techniques](#methods-and-techniques)
  - [Results](#results)
  - [Requirements](#requirements)
  - [Usage](#usage)

## Key Objectives

The project aims to answer the following research questions:

1. What characteristics define highly-rated movies?
2. Are there notable differences in movie budgets across different countries?
3. Which directors have the highest number of popular movies?

## Dataset

The dataset consists of various attributes related to movies, including:

- **Title**: The name of the movie
- **Year**: Release year
- **Director**: Name of the movie’s director
- **IMDb Score**: IMDb rating of the movie
- **Budget**: Movie’s budget
- **Country**: Country of origin
- **Language**: Primary language of the movie
- **Color**: Color type of the movie (Color or Black and White)

## Project Structure

The project is organized into several sections:

- **Data Loading and Exploration**: Initial data loading and exploration without using the `pandas` library, focusing on practicing Python’s core data handling techniques.
- **Data Processing**: Cleaning and transforming the dataset, including handling missing values, correcting data types, and filtering unnecessary columns.
- **Analysis**: Answering research questions by generating insights and analyzing patterns.
- **Visualization**: Using `matplotlib` and `seaborn` to visualize findings.

## Methods and Techniques

- **Data Extraction**: Basic data handling without `pandas` for initial practice, transitioning to `pandas` for advanced tasks.
- **Data Manipulation**: Filtering, cleaning, and transforming data.
- **Visualization**: Plotting distributions, correlations, and patterns using Python libraries (`matplotlib`, `seaborn`).
- **Pattern Identification**: Analyzing relationships between movie attributes and ratings.

## Results

Insights derived from the project include:

- Characteristics of top-rated movies.
- Country-based budget differences.
- Directors with the most popular movies.

## Requirements

To run this project, you’ll need:

[Anaconda](https://www.anaconda.com/) or Jupyter plugin

## Usage

1. Clone the repository.
2. Download the IMDb dataset from Kaggle ([link](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)) and place it in the `data_in` folder.
3. Run the Jupyter Notebook for analysis.
