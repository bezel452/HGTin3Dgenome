library(ggplot2)
library(tidyverse)

preProcessing <- function(File, Category){
  eGO <- read.table(File, header = T, sep = ',')
  eGO <- separate(data = eGO, col=GeneRatio, into = c("GR1", "GR2"), sep = "/")
  eGO <- separate(data = eGO, col=BgRatio, into = c("BR1", "BR2"), sep = "/")
  eGO <- mutate(eGO, EnrichmentFactor = (as.numeric(GR1)/as.numeric(GR2))/(as.numeric(BR1)/as.numeric(BR2)))
  
  eGOBP <- eGO %>%
    filter(ONTOLOGY=='BP') %>%
    filter(row_number() >= 1, row_number() <= Category)
  
  eGOCC <- eGO %>%
    filter(ONTOLOGY=='CC') %>%
    filter(row_number() >= 1, row_number() <= Category)
  
  eGOMF <- eGO %>%
    filter(ONTOLOGY=='MF') %>%
    filter(row_number() >= 1, row_number() <= Category)
  
  eGO10 <- rbind(eGOBP, eGOMF, eGOCC)
  return(eGO10)
}

L1.001_10 <- preProcessing("Only/001L1.csv", 10)

dot_p <- ggplot(L1.001_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L1.001_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L2.001_10 <- preProcessing("Only/001L2.csv", 10)
dot_p <- ggplot(L2.001_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L2.001_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L3.001_10 <- preProcessing("Only/001L3.csv", 10)

dot_p <- ggplot(L3.001_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L3.001_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L1.050_10 <- preProcessing("Only/050L1.csv", 10)
dot_p <- ggplot(L1.050_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L1.050_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L2.050_10 <- preProcessing("Only/050L2.csv", 10)
dot_p <- ggplot(L2.050_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L2.050_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L3.050_10 <- preProcessing("Only/050L3.csv", 10)
dot_p <- ggplot(L3.050_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L3.050_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L1c.001_10 <- preProcessing("enrichGO001500K1.csv", 10)

dot_p <- ggplot(L1c.001_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L1c.001_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L2c.001_10 <- preProcessing("enrichGO001500K2.csv", 10)

dot_p <- ggplot(L2c.001_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L2c.001_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L3c.001_10 <- preProcessing("enrichGO001500K3.csv", 10)

dot_p <- ggplot(L3c.001_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L3c.001_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L4c.001_10 <- preProcessing("enrichGO001500K4.csv", 10)

dot_p <- ggplot(L4c.001_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L4c.001_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L1c.050_10 <- preProcessing("enrichGO050500K1.csv", 10)

dot_p <- ggplot(L1c.050_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L1c.050_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L2c.050_10 <- preProcessing("enrichGO050500K2.csv", 10)

dot_p <- ggplot(L2c.050_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L2c.050_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L3c.050_10 <- preProcessing("enrichGO050500K3.csv", 10)

dot_p <- ggplot(L3c.050_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L3c.050_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1

L4c.050_10 <- preProcessing("enrichGO050500K4.csv", 10)

dot_p <- ggplot(L4c.050_10, aes(EnrichmentFactor, Description)) +
  geom_point(aes(size=Count, color=-1*log10(p.adjust), shape=ONTOLOGY)) +
  scale_color_gradient(low="red", high="green") +
  labs(color=expression(-log[10](p_value)), size="Count", shape="Ontology",
       x="Fold enrichment", y="GO term") +
  theme_bw()
dot_p
dot_p1 <- dot_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
dot_p1

bar_p <- ggplot(L4c.050_10, aes(Count, Description)) +
  geom_bar(stat="identity", width=0.8, aes(fill = -1*log10(p.adjust))) +
  scale_fill_gradient(low="red", high="blue") +
  labs(fill=expression(-log[10](p_value)), x="Counts", y="GO term") +
  theme_bw()
bar_p
bar_p1 <- bar_p + facet_grid(ONTOLOGY ~., scale = 'free_y', space = 'free_y')
bar_p1