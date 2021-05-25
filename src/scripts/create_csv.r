install.packages("here")
install.packages("data.table")
install.packages("readxl")
require("here")
require("data.table")
require("readxl")


# Read Excel (.xlsx) files
audio_changes <- readxl::read_xlsx(path = "Audio.xlsx", col_types = c("text"))
legend_changes <- readxl::read_xlsx(path = "Legenda.xlsx", col_types = c("text"))


# Convert Excel (.xlsx) files to .csv
setwd(here::here())

data.table::fwrite(x = audio_changes,
                   file = "../../../Documents/GitHub Repositories/mod-alien-isolation/src/audio_changes.csv",
                   sep = ",",
                   quote = TRUE)
data.table::fwrite(x = legend_changes,
                   file = "../../../Documents/GitHub Repositories/mod-alien-isolation/src/legend_changes.csv",
                   sep = ",",
                   quote = TRUE)
