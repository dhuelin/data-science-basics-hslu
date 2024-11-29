library(shiny)
library(jsonlite)
library(ggplot2)

# Read the CSV file generated from generate_masterlist.ipynb, if you don't have a master list already, please generate it there.
data <- read.csv("Data/masterlist.csv", check.names = FALSE) # set check names to false as headers are used in UI, thus shouldn't be changed
