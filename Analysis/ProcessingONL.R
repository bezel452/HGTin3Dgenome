library(org.Hs.eg.db)
library(clusterProfiler)
library(DOSE)

load("Only/001L1.rda")
write.csv(enrichGO001L1, 'Only/001L1.csv', row.names = F)

load("Only/001L2.rda")
write.csv(enrichGO001L2, 'Only/001L2.csv', row.names = F)

load("Only/001L3.rda")
write.csv(enrichGO001L3, 'Only/001L3.csv', row.names = F)

load("Only/050L1.rda")
write.csv(enrichGO050L1, 'Only/050L1.csv', row.names = F)

load("Only/050L2.rda")
write.csv(enrichGO050L2, 'Only/050L2.csv', row.names = F)

load("Only/050L3.rda")
write.csv(enrichGO050L3, 'Only/050L3.csv', row.names = F)