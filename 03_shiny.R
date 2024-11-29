# Load the data
library(ggplot2)
data <- read.csv("preprocessed_healthcare_data.csv")

# Healthcare costs over time by age group
ggplot(data, aes(x = Year, y = Healthcare.Costs, color = Altersklasse...Total)) +
  geom_line() +
  labs(title = "Healthcare Costs Over Time by Age Group", x = "Year", y = "Total Healthcare Costs (CHF)") +
  theme_minimal()

# Per capita healthcare costs by age group
ggplot(data, aes(x = Year, y = Per.Capita.Costs, color = Altersklasse...Total)) +
  geom_line() +
  labs(title = "Per Capita Healthcare Costs Over Time by Age Group", x = "Year", y = "Per Capita Costs (CHF)") +
  theme_minimal()

# Population vs. Healthcare Costs
ggplot(data, aes(x = Population, y = Healthcare.Costs, color = Altersklasse...Total)) +
  geom_point() +
  geom_smooth(method = "lm") +
  labs(title = "Population vs. Healthcare Costs by Age Group", x = "Population", y = "Healthcare Costs (CHF)") +
  theme_minimal()
