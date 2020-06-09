setwd('..')
setwd('reports/figures')

# We first install packages biocManager and TCGAbiolinks that are needed
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager", repos = "http://cran.us.r-project.org")

BiocManager::install("TCGAbiolinks")

library(TCGAbiolinks)
library(SummarizedExperiment)

#Then we can draw the survival plots from the clinical data from TCGA
clin.gbm <- GDCquery_clinic("TCGA-GBM", "clinical")
TCGAanalyze_survival(clin.gbm, "gender", main = "TCGA Set\n GBM",height = 10, width=10)

clin.gbm <- GDCquery_clinic("TCGA-LGG", "clinical")
TCGAanalyze_survival(clin.gbm, "gender", main = "TCGA Set\n LGG",height = 10, width=10)
