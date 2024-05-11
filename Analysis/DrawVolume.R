library(ggplot2)
uni <- data.frame(sam1.h001 ** 3, sam1.h050 ** 3)
copy <- data.frame(sam.h001 ** 3, sam.h050 ** 3)
only <- data.frame(sam2.h001 ** 3, sam2.h050 ** 3)
all <- data.frame(pop.h001 ** 3, pop.h050 ** 3)

puni.1 <- ggplot(uni, aes(sam1.h001.3)) +
  geom_histogram(bins=15, fill="darkblue") +
  geom_vline(xintercept = c(0.25, 0.5, 0.75), lty="dashed") +
  annotate("text", x = 0.15, y = 12, label = "1", size = 15) +
  annotate("text", x = 0.35, y = 12, label = "2", size = 15) +
  annotate("text", x = 0.65, y = 12, label = "3", size = 15) +
  annotate("text", x = 0.85, y = 12, label = "4", size = 15) +
  labs(x = "Ratio of Volume", y = "Frequency") +
  theme_bw()+
  theme(text = element_text(size = 30)) 
puni.1

puni.2 <- ggplot(uni, aes(sam1.h050.3)) +
  geom_histogram(bins=15, fill="darkblue") +
  geom_vline(xintercept = c(0.25, 0.5, 0.75), lty="dashed") +
  annotate("text", x = 0.15, y = 10, label = "1", size = 15) +
  annotate("text", x = 0.35, y = 10, label = "2", size = 15) +
  annotate("text", x = 0.65, y = 10, label = "3", size = 15, color = "white") +
  annotate("text", x = 0.85, y = 10, label = "4", size = 15) +
  labs(x = "Ratio of Volume", y = "Frequency") +
  theme_bw()+
  theme(text = element_text(size = 30)) 
puni.2

pcopy.1 <- ggplot(copy, aes(sam.h001.3)) +
  geom_histogram(bins=40, fill="darkblue") +
  geom_vline(xintercept = c(0.25, 0.5, 0.75), lty="dashed") +
  annotate("text", x = 0.15, y = 30, label = "1", size = 15) +
  annotate("text", x = 0.35, y = 30, label = "2", size = 15) +
  annotate("text", x = 0.65, y = 30, label = "3", size = 15) +
  annotate("text", x = 0.85, y = 30, label = "4", size = 15) +
  labs(x = "Ratio of Volume", y = "Frequency") +
  theme_bw()+
  theme(text = element_text(size = 30)) 
pcopy.1

pcopy.2 <- ggplot(copy, aes(sam.h050.3)) +
  geom_histogram(bins=40, fill="darkblue") +
  geom_vline(xintercept = c(0.25, 0.5, 0.75), lty="dashed") +
  annotate("text", x = 0.15, y = 31, label = "1", size = 15) +
  annotate("text", x = 0.35, y = 31, label = "2", size = 15) +
  annotate("text", x = 0.65, y = 31, label = "3", size = 15) +
  annotate("text", x = 0.85, y = 31, label = "4", size = 15) +
  labs(x = "Ratio of Volume", y = "Frequency") +
  theme_bw()+
  theme(text = element_text(size = 30)) 
pcopy.2

ponly.1 <- ggplot(only, aes(sam2.h001.3)) +
  geom_histogram(bins=15, fill="darkblue") +
  geom_vline(xintercept = c(0.25, 0.5, 0.75), lty="dashed") +
  annotate("text", x = 0.15, y = 9, label = "1", size = 15) +
  annotate("text", x = 0.35, y = 9, label = "2", size = 15) +
  annotate("text", x = 0.65, y = 9, label = "3", size = 15) +
  annotate("text", x = 0.85, y = 9, label = "4", size = 15) +
  labs(x = "Ratio of Volume", y = "Frequency") +
  theme_bw()+
  theme(text = element_text(size = 30)) 
ponly.1

ponly.2 <- ggplot(only, aes(sam2.h050.3)) +
  geom_histogram(bins=15, fill="darkblue") +
  geom_vline(xintercept = c(0.25, 0.5, 0.75), lty="dashed") +
  annotate("text", x = 0.15, y = 9, label = "1", size = 15) +
  annotate("text", x = 0.35, y = 9, label = "2", size = 15) +
  annotate("text", x = 0.65, y = 9, label = "3", size = 15) +
  annotate("text", x = 0.85, y = 9, label = "4", size = 15) +
  labs(x = "Ratio of Volume", y = "Frequency") +
  theme_bw()+
  theme(text = element_text(size = 30)) 
ponly.2

pall.1 <- ggplot(all, aes(pop.h001.3)) +
  geom_histogram(bins=50, fill="darkblue") +
  geom_vline(xintercept = c(0.25, 0.5, 0.75), lty="dashed") +
  annotate("text", x = 0.15, y = 175, label = "1", size = 15) +
  annotate("text", x = 0.35, y = 175, label = "2", size = 15) +
  annotate("text", x = 0.65, y = 175, label = "3", size = 15) +
  annotate("text", x = 0.85, y = 175, label = "4", size = 15) +
  labs(x = "Ratio of Volume", y = "Frequency") +
  theme_bw()+
  theme(text = element_text(size = 30)) 
pall.1

pall.2 <- ggplot(all, aes(pop.h050.3)) +
  geom_histogram(bins=50, fill="darkblue") +
  geom_vline(xintercept = c(0.25, 0.5, 0.75), lty="dashed") +
  annotate("text", x = 0.15, y = 175, label = "1", size = 15) +
  annotate("text", x = 0.35, y = 175, label = "2", size = 15) +
  annotate("text", x = 0.65, y = 175, label = "3", size = 15) +
  annotate("text", x = 0.85, y = 175, label = "4", size = 15) +
  labs(x = "Ratio of Volume", y = "Frequency") +
  theme_bw()+
  theme(text = element_text(size = 30)) 
pall.2