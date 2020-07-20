ALL = immune-cell-census adult-retina

all: $(ALL)

%: %.mtx.zip
	unzip -d $* $<

adult-retina.mtx.zip:
	curl -L "https://data.humancellatlas.org/project-assets/project-matrices/8185730f-4113-40d3-9cc3-929271784c2b.homo_sapiens.mtx.zip" -o $@

immune-cell-census.mtx.zip:
	curl -L "https://data.humancellatlas.org/project-assets/project-matrices/cc95ff89-2e68-4a08-a234-480eca21ce79.homo_sapiens.mtx.zip" -o $@

immune-cell-census.loom:
	curl -L "https://data.humancellatlas.org/project-assets/project-matrices/cc95ff89-2e68-4a08-a234-480eca21ce79.homo_sapiens.loom" -o $@

.INTERMEDIATE: $(ALL:=.mtx.zip)
