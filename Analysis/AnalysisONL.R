library(org.Hs.eg.db)
library(clusterProfiler)
library(DOSE)

file <- 'onl_001L1Qgene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)

enrichGO001L1 <- enrichGO(gene = my_id,
                        OrgDb = 'org.Hs.eg.db',
                        keyType = 'REFSEQ',
                        ont = 'ALL',
                        pAdjustMethod = 'fdr',
                        pvalueCutoff = 0.05,
                        qvalueCutoff = 0.2,
                        readable = FALSE)

save(enrichGO001L1, file = '001L1.rda')

file <- 'onl_001L2Qgene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)

enrichGO001L2 <- enrichGO(gene = my_id,
                          OrgDb = 'org.Hs.eg.db',
                          keyType = 'REFSEQ',
                          ont = 'ALL',
                          pAdjustMethod = 'fdr',
                          pvalueCutoff = 0.05,
                          qvalueCutoff = 0.2,
                          readable = FALSE)

save(enrichGO001L2, file = '001L2.rda')

file <- 'onl_001L3Qgene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)

enrichGO001L3 <- enrichGO(gene = my_id,
                          OrgDb = 'org.Hs.eg.db',
                          keyType = 'REFSEQ',
                          ont = 'ALL',
                          pAdjustMethod = 'fdr',
                          pvalueCutoff = 0.05,
                          qvalueCutoff = 0.2,
                          readable = FALSE)

save(enrichGO001L3, file = '001L3.rda')

file <- 'onl_050L1Qgene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)

enrichGO050L1 <- enrichGO(gene = my_id,
                          OrgDb = 'org.Hs.eg.db',
                          keyType = 'REFSEQ',
                          ont = 'ALL',
                          pAdjustMethod = 'fdr',
                          pvalueCutoff = 0.05,
                          qvalueCutoff = 0.2,
                          readable = FALSE)

save(enrichGO050L1, file = '050L1.rda')

file <- 'onl_050L2Qgene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)

enrichGO050L2 <- enrichGO(gene = my_id,
                          OrgDb = 'org.Hs.eg.db',
                          keyType = 'REFSEQ',
                          ont = 'ALL',
                          pAdjustMethod = 'fdr',
                          pvalueCutoff = 0.05,
                          qvalueCutoff = 0.2,
                          readable = FALSE)

save(enrichGO050L2, file = '050L2.rda')

file <- 'onl_050L3Qgene'
data1 = read.table(file)
my_id <- data1$V1
my_id <- gsub("\\..*", "", my_id)

enrichGO050L3 <- enrichGO(gene = my_id,
                          OrgDb = 'org.Hs.eg.db',
                          keyType = 'REFSEQ',
                          ont = 'ALL',
                          pAdjustMethod = 'fdr',
                          pvalueCutoff = 0.05,
                          qvalueCutoff = 0.2,
                          readable = FALSE)

save(enrichGO050L3, file = '050L3.rda')