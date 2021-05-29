install.packages("here")
install.packages("data.table")
install.packages("readxl")
require("here")
require("data.table")
require("readxl")


# Read Excel (.xlsx) files
audio_changes <- readxl::read_xlsx(path = "Audio.xlsx",
                                   col_names = TRUE,
                                   col_types = c("text"))
legend_changes <- readxl::read_xlsx(path = "Legenda.xlsx",
                                    col_names = TRUE,
                                    col_types = c("text"))


# Remove unnecessary columns to Github
audio_changes <- audio_changes[, 3:ncol(audio_changes)]
legend_changes <- legend_changes[, 3:ncol(legend_changes)]


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
