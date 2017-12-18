library(dplyr)
library(ggplot2)

df1 = read.csv(file = "feed_single.csv", header = TRUE)
df2 = read.csv(file = "feed_bulk.csv", header = TRUE)
df1$time <- strftime(df1$field2, format="%M:%S")
df2$time <- strftime(df2$created_at, format="%M:%S")

#plot single measurement
ggplot(df1, aes(x=df1$time, y=field1, group = 1)) +geom_point() + geom_line()+
  labs(x = "Time", y = "SMA", title = "SMA vs Time (avg > 0.1) measured in 5 minutes")+theme(plot.title = element_text(hjust = 0.5))

#plot bulk
ggplot(df2, aes(x=df2$time, y=field1, group = 1)) +geom_point() + geom_line()+
  labs(x = "Time", y = "SMA", title = "SMA vs Time (avg > 0.5 measured in 5 minutes")+theme(plot.title = element_text(hjust = 0.5))

