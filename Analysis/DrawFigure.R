library(ggplot2)

uni <- data.frame(sam1.h001, sam1.h050)
copy <- data.frame(sam.h001, sam.h050)
only <- data.frame(sam2.h001, sam2.h050)
all <- data.frame(pop.h001, pop.h050)

puni.1 <- ggplot(uni, aes(sam1.h001)) +
  geom_histogram(bins=20, fill="lightblue") +
  geom_vline(xintercept = c(0.5 ^ (2/3), 0.5^(1/3), 0.75^(1/3)), lty="dashed") +
  annotate("text", x = 0.5 ^ (2/3) - 0.05, y = 13, label = "x = (1/2) ^ (2/3)") +
  annotate("text", x = 0.5^(1/3) - 0.05, y = 13, label = "x = (1/2) ^ (1/3)") +
  annotate("text", x = 0.75^(1/3) + 0.05, y = 13, label = "x = (3/4) ^ (1/3)") +
  labs(x = "Ratio of Radius", y = "Frequency") +
  theme_bw()
puni.1

puni.2 <- ggplot(uni, aes(sam1.h050)) +
  geom_histogram(bins=20, fill="lightblue") +
  geom_vline(xintercept = c(0.5 ^ (2/3), 0.5^(1/3), 0.75^(1/3)), lty="dashed") +
  annotate("text", x = 0.5 ^ (2/3) - 0.05, y = 13, label = "x = (1/2) ^ (2/3)") +
  annotate("text", x = 0.5^(1/3) - 0.05, y = 13, label = "x = (1/2) ^ (1/3)") +
  annotate("text", x = 0.75^(1/3) + 0.05, y = 13, label = "x = (3/4) ^ (1/3)") +
  labs(x = "Ratio of Radius", y = "Frequency") +
  theme_bw()
puni.2

pcopy.1 <- ggplot(copy, aes(sam.h001)) +
  geom_histogram(bins=40, fill="lightblue") +
  geom_vline(xintercept = c(0.5 ^ (2/3), 0.5^(1/3), 0.75^(1/3)), lty="dashed") +
  annotate("text", x = 0.5 ^ (2/3) - 0.05, y = 40, label = "x = (1/2) ^ (2/3)") +
  annotate("text", x = 0.5^(1/3) - 0.05, y = 40, label = "x = (1/2) ^ (1/3)") +
  annotate("text", x = 0.75^(1/3) + 0.05, y = 40, label = "x = (3/4) ^ (1/3)") +
  labs(x = "Ratio of Radius", y = "Frequency") +
  theme_bw()
pcopy.1

pcopy.2 <- ggplot(copy, aes(sam.h050)) +
  geom_histogram(bins=40, fill="lightblue") +
  geom_vline(xintercept = c(0.5 ^ (2/3), 0.5^(1/3), 0.75^(1/3)), lty="dashed") +
  annotate("text", x = 0.5 ^ (2/3) - 0.05, y = 40, label = "x = (1/2) ^ (2/3)") +
  annotate("text", x = 0.5^(1/3) - 0.05, y = 40, label = "x = (1/2) ^ (1/3)") +
  annotate("text", x = 0.75^(1/3) + 0.05, y = 40, label = "x = (3/4) ^ (1/3)") +
  labs(x = "Ratio of Radius", y = "Frequency") +
  theme_bw()
pcopy.2

ponly.1 <- ggplot(only, aes(sam2.h001)) +
  geom_histogram(bins=20, fill="lightblue") +
  geom_vline(xintercept = c(0.5 ^ (2/3), 0.5^(1/3), 0.75^(1/3)), lty="dashed") +
  annotate("text", x = 0.5 ^ (2/3) - 0.05, y = 8, label = "x = (1/2) ^ (2/3)") +
  annotate("text", x = 0.5^(1/3) - 0.05, y = 8, label = "x = (1/2) ^ (1/3)") +
  annotate("text", x = 0.75^(1/3) + 0.05, y = 8, label = "x = (3/4) ^ (1/3)") +
  labs(x = "Ratio of Radius", y = "Frequency") +
  theme_bw()
ponly.1

ponly.2 <- ggplot(only, aes(sam2.h050)) +
  geom_histogram(bins=20, fill="lightblue") +
  geom_vline(xintercept = c(0.5 ^ (2/3), 0.5^(1/3), 0.75^(1/3)), lty="dashed") +
  annotate("text", x = 0.5 ^ (2/3) - 0.05, y = 7, label = "x = (1/2) ^ (2/3)") +
  annotate("text", x = 0.5^(1/3) - 0.05, y = 7, label = "x = (1/2) ^ (1/3)") +
  annotate("text", x = 0.75^(1/3) + 0.05, y = 7, label = "x = (3/4) ^ (1/3)") +
  labs(x = "Ratio of Radius", y = "Frequency") +
  theme_bw()
ponly.2

pall.1 <- ggplot(all, aes(pop.h001)) +
  geom_histogram(bins=50, fill="lightblue") +
  geom_vline(xintercept = c(0.5 ^ (2/3), 0.5^(1/3), 0.75^(1/3)), lty="dashed") +
  annotate("text", x = 0.5 ^ (2/3) - 0.05, y = 300, label = "x = (1/2) ^ (2/3)") +
  annotate("text", x = 0.5^(1/3) - 0.05, y = 300, label = "x = (1/2) ^ (1/3)") +
  annotate("text", x = 0.75^(1/3) + 0.05, y = 300, label = "x = (3/4) ^ (1/3)") +
  labs(x = "Ratio of Radius", y = "Frequency") +
  theme_bw()
pall.1

pall.2 <- ggplot(all, aes(pop.h050)) +
  geom_histogram(bins=50, fill="lightblue") +
  geom_vline(xintercept = c(0.5 ^ (2/3), 0.5^(1/3), 0.75^(1/3)), lty="dashed") +
  annotate("text", x = 0.5 ^ (2/3) - 0.05, y = 300, label = "x = (1/2) ^ (2/3)") +
  annotate("text", x = 0.5^(1/3) - 0.05, y = 300, label = "x = (1/2) ^ (1/3)") +
  annotate("text", x = 0.75^(1/3) + 0.05, y = 300, label = "x = (3/4) ^ (1/3)") +
  labs(x = "Ratio of Radius", y = "Frequency") +
  theme_bw()
pall.2
