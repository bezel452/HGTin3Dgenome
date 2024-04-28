data.h001 <- read.table('H001_500k.txt')
data.h050 <- read.table('H050_500K.txt')
pop.h001 <- data.h001$V1
pop.h050 <- data.h050$V1

data1.h001 <- read.table('H001_500khGT.txt')
data1.h050 <- read.table('H050_500KhGT.txt')
sam.h001 <- data1.h001$V1
sam.h050 <- data1.h050$V1

sam.h001 <- na.omit(sam.h001)
sam.h050 <- na.omit(sam.h050)

ks.test(pop.h001, 'pnorm')
ks.test(pop.h050, 'pnorm')

shapiro.test(sam.h001)
shapiro.test(sam.h050)


wilcox.test(sam.h001, pop.h001, paired = F)
wilcox.test(sam.h050, pop.h050, paired = F)

data2.h001 <- read.table('H001_500k_anno_HGT_sortedhGT.txt')
data2.h050 <- read.table('H050_500K_anno_HGT_sortedhGT.txt')
sam1.h001 <- data2.h001$V1
sam1.h050 <- data2.h050$V1
wilcox.test(sam1.h001, pop.h001, paired = F)
wilcox.test(sam1.h050, pop.h050, paired = F)
wilcox.test(sam1.h050, pop.h050, paired = F, alternative = "greater")
data3.h001 <- read.table('H001_500k_anno_only_sortedhGT.txt')
data3.h050 <- read.table('H050_500K_anno_only_sortedhGT.txt')
sam2.h001 <- data3.h001$V1
sam2.h050 <- data3.h050$V1
wilcox.test(sam2.h001, pop.h001, paired = F)
wilcox.test(sam2.h050, pop.h050, paired = F)
wilcox.test(sam2.h050, pop.h050, paired = F, alternative = "less")
