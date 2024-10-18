# MyRepo: General Sequencing Data Analysis and Biological Experiment Methods

This repository contains materials and notes related to sequencing data analysis and biological experiment protocols. Explore the resources below for detailed information on methods and workflows.
* To download and print the .md files
```bash
#example
pandoc  --pdf-engine=xelatex -V mainfont="Arial" file.md -o file.pdf 
```
---

# Sequencing Data Analysis Materials

## Online Training and Workshops
- [EMBL-EBI Online Training Courses](https://www.ebi.ac.uk/training/on-demand) - Comprehensive list of courses
- [3rd International Workshop on the Epigenetics of Osteoarthritis](https://www.epigeneticsoa.com/program) - OA Related

The important book I bought for learning Bioinformatics
- [cell-line-to-command-line](https://divingintogeneticsandgenomics.ck.page/products/cell-line-to-command-line)
- [practical computing for biologists](https://pdfroom.com/books/practical-computing-for-biologists/jb5qOKXBgxQ/download) it covers regular expression, Unix commands and some python stuffs that directly related to biology
---

## Statistical Analysis
1. [Statistical Models](./Statistics_01_Statistical_models.md)
2. [Statistical Analysis for Mendelian Randomization (MR)](./Statistics_02_Statistical_analysis_for_MR.md)

---

## Bioinformatics
- [Bioinformatics Starter Pack](./Bioinformatics_01_Bioinformatics_Starter_Pack.md)

### Basic R
- [Understand Your Data in R](https://runuply.github.io/protocol_repo/r/r_basic_from_bbc_core.html)
- [The art of R programming](https://github.com/aaaastark/Data-Scientist-Books/blob/main/The%20Art%20of%20R%20Programming%20A%20Tour%20of%20Statistical%20Software%20Design.pdf), it covers the basics, learn to use packages like dplyr, ggplot2 will greatly reduce the complexity of your code and enhancer your productivity.

### Basic Python
- [Test the python on vs](./python/python_01_test_on_vs_code.py)
- Book maybe useful for you [python programming for absolute beginners](https://github.com/CWade3051/Py/blob/master/Absolute%20Book/Python%20Programming%20for%20the%20Absolute%20Beginner%2C%203rd%20Edition/Python%20Programming%20for%20the%20Absolute%20Beginner%2C%203rd%20Edition.pdf).

### Basic Linux Command Line (unix skills will never fade)
- [GitHub Setup and Workflow](./Linux_command_line_01_Git_setup.md)
- [Van Andel Institute bioinfo workshop 2024-HPC](http://hpcworkshop.vai.org/)
- [Van Andel Institute bioinfo workshop 2024-Intro_to_Linux_for_HPC](https://vari-bbc.github.io/Intro_to_Linux_for_HPC/index.html)

### Several resources to read before any project:
- 1. [A Quick Guide to Organizing Computational Biology Projects](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424&ck_subscriber_id=1874464006&utm_source=convertkit&utm_medium=email&utm_campaign=My%202%20cents%20on%20coding%20when%20I%20was%20a%20bioinformatics%20beginner%20-%2015155532)

- 2. [Designing project by Vince Buffalo Vince Buffalo](https://nicercode.github.io/blog/2013-04-05-projects/?ck_subscriber_id=1874464006&utm_source=convertkit&utm_medium=email&utm_campaign=My%202%20cents%20on%20coding%20when%20I%20was%20a%20bioinformatics%20beginner%20-%2015155532) has a book which highly recommend: [Bioinformatics data skills](https://www.oreilly.com/library/view/bioinformatics-data-skills/9781449367480/?ck_subscriber_id=1874464006&utm_source=convertkit&utm_medium=email&utm_campaign=My%202%20cents%20on%20coding%20when%20I%20was%20a%20bioinformatics%20beginner%20-%2015155532). 

​
- 3. [Best Practices for Scientific Computing​](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745&ck_subscriber_id=1874464006&utm_source=convertkit&utm_medium=email&utm_campaign=My%202%20cents%20on%20coding%20when%20I%20was%20a%20bioinformatics%20beginner%20-%2015155532).The take home message for me is that it is not enough for you to just run the code, get some results and then publish them.

- 4. I learned a lot from Tommy Tang, please follow his X https://x.com/tangming2005, he tweets tools and papers.
   -- Dealing with genomic intervals. He mentioned in the early days, he wrote his script in python doing the same thing as bedtools (published in 2010). He mentioned Dr. Ting Wang also did the same thing, writing a Perl script to do the intersection of genomic regions and found TP53 binds to TEs. See his paper [https://www.pnas.org/doi/epdf/10.1073/pnas.0703637104](https://www.pnas.org/doi/epdf/10.1073/pnas.0703637104) in 2007. The Bioconductor ecosystem and also has the GenomicRanges package which is the foundation of dealing with genomic intervals
​
---

## Molecular Biology protocols
1. [Protocol for Osteoclast Differentiation from Mouse Bone Marrow Monocytes](./Biological_experiment_01_BMDM_OC_differention.md)
2. [Protocol for Isolation and Culture of Primary Articular Chondrocytes from Mouse Growth Plate](./Biological_experiment_02_Growth_plate_AC_isolation_culture.md)
3. [Protocol for Cut&Run Assay of Mapping DNA-Protein Interactions](./Biological_experiment_03_cutrun.md)
4. [Protocol for In Vitro Cell Stretching Experiments](./Biological_experiment_04_STEX_Stretching.md)
5. [Protocol for Collect bone marrow mononuclear cells](https://github.com/Runuply/protocol_repo/wiki/Biological_experiment#05_collect_bone_marrow_mononuclear_cells)


---
This repository will be continuously updated with additional methods and resources.
