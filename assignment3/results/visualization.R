setwd("~/Desktop/Kuliah/informationsystem/Assignments/informationsystem/assignment3/results")
library(dplyr)
library(ggplot2)

df1 = read.csv(file = "feed_single.csv", header = TRUE)
df2 = read.csv(file = "feed_bulk.csv", header = TRUE)
df1$time <- strftime(df1$created_at, format="%M:%S")
df2$time <- strftime(df2$created_at, format="%M:%S")

#plot single measurement
ggplot(df1, aes(x=entry_id, y=field1)) + geom_point() + geom_line()+xlab("Time") + ylab("SMA")+ggtitle("SMA vs Time (avg > 0.1)")+
  theme(plot.title = element_text(hjust = 0.5))

#plot bulk
ggplot(df2, aes(x=entry_id, y=field1)) + geom_point() + geom_line()+xlab("Time") + ylab("SMA")+ggtitle("SMA vs Time (avg > 0.5)")+
  theme(plot.title = element_text(hjust = 0.5))
