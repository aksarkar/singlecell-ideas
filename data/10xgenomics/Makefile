DATA := 293t \
293t_3t3 \
frozen_pbmc_b_c_50_50 \
frozen_pbmc_b_c_90_10 \
frozen_pbmc_b_c_99_1 \
jurkat_293t_50_50 \
jurkat_293t_99_1 \
cd14_monocytes \
b_cells \
cd34 \
cd4_t_helper \
regulatory_t \
naive_t \
memory_t \
cd56_nk \
cytotoxic_t \
naive_cytotoxic \
fresh_68k_pbmc_donor_a \
jurkat 

CURL := curl -O

all: $(DATA)
	find -name "Makefile" -prune -o -name "*.gz" -prune -o -type f -print | parallel gzip

.PHONY: all

# Make doesn't like colons
# http://lists.gnu.org/archive/html/bug-make/2004-10/msg00010.html
jurkat_293t_50_50_filtered_gene_bc_matrices.tar.gz:
	curl "https://cf.10xgenomics.com/samples/cell-exp/1.1.0/jurkat:293t_50:50/jurkat:293t_50:50_filtered_gene_bc_matrices.tar.gz" -o $@

.INTERMEDIATE: jurkat_293t_50_50_filtered_gene_bc_matrices.tar.gz

%_filtered_gene_bc_matrices.tar.gz:
	$(CURL) "https://cf.10xgenomics.com/samples/cell-exp/1.1.0/$*/$@"

%: %_filtered_gene_bc_matrices.tar.gz
	mkdir -p $@
	tar xf $< -C $@
