library(org.Hs.eg.db)
library(clusterProfiler)
library(DOSE)

file <- 'H050_500K_1gene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)
enrichGO4 <- enrichGO(gene = my_id,
                        OrgDb = 'org.Hs.eg.db',
                        keyType = 'REFSEQ',
                        ont = 'ALL',
                        pAdjustMethod = 'fdr',
                        pvalueCutoff = 0.05,
                        qvalueCutoff = 0.2,
                        readable = FALSE)
  
save(enrichGO4, file = 'enrichGO050500K4')
rm(enrichGO4)

file <- 'H050_500K_LessThan1Qgene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)
enrichGO1 <- enrichGO(gene = my_id,
                      OrgDb = 'org.Hs.eg.db',
                      keyType = 'REFSEQ',
                      ont = 'ALL',
                      pAdjustMethod = 'fdr',
                      pvalueCutoff = 0.05,
                      qvalueCutoff = 0.2,
                      readable = FALSE)

save(enrichGO1, file = 'enrichGO050500K1')
rm(enrichGO1)

file <- 'H050_500K_LessThanHalfgene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)
enrichGO2 <- enrichGO(gene = my_id,
                      OrgDb = 'org.Hs.eg.db',
                      keyType = 'REFSEQ',
                      ont = 'ALL',
                      pAdjustMethod = 'fdr',
                      pvalueCutoff = 0.05,
                      qvalueCutoff = 0.2,
                      readable = FALSE)

save(enrichGO2, file = 'enrichGO050500K2')
rm(enrichGO2)

file <- 'H050_500K_LessThan3Qgene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)
enrichGO3 <- enrichGO(gene = my_id,
                      OrgDb = 'org.Hs.eg.db',
                      keyType = 'REFSEQ',
                      ont = 'ALL',
                      pAdjustMethod = 'fdr',
                      pvalueCutoff = 0.05,
                      qvalueCutoff = 0.2,
                      readable = FALSE)

save(enrichGO3, file = 'enrichGO050500K3')
rm(enrichGO3)




