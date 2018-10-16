getwd()
setwd("Desktop/")

d <- read.table("test.txt")
View(d)
describeBy(d)
duplicated(d[11])
describe(d[9])

d$block4 <- rep(c('1', '2', '1', '2'), each = 48)
View(d)

table(d$block4,d$V3)
table(d$block4,d$V5)
table(d$block4,d$V6)
table(d$block4,d$V7)
table(d$block4,d$V8)

xtabs(~V6+V7 + V8 + block4, data=d)
