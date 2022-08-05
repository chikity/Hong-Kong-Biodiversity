library(tidyverse)
library(janitor)
library(ggplot2)

# General Cleaning
df <- read_csv('./data/Checklist_of_Biodiversity_in_Hong_Kong.csv')
df_clean <- clean_names(df) %>% 
  rename(scientific_name = xue_ming_scientific_name, 
         name_cn = zhong_wen_ming_cheng, 
         phylum_cn = men, 
         class_cn = gang, 
         order_cn = mu, 
         family_cn = ke, 
         checklist_cn = ming_lu
         )

# Create Features
df_feature <- df_clean %>% 
  mutate(family_name = word(scientific_name, 1))



# Explore
type_df <- df_feature %>% 
  group_by(checklist) %>% 
  tally(sort = TRUE)

ggplot(data = type_df, aes(x = "", y = n, fill = checklist)) +
  geom_col() +
  geom_text(aes(label = round(n/sum(n)*100)),
            position = position_stack(vjust = 0.5)) +
  coord_polar(theta = "y") +
  theme_minimal() +
  labs(title = "Hong Kong Biodiversity", fill = "Type")
