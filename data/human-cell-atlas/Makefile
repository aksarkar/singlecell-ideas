ALL = immune-cell-census adult-retina
CURL = curl -o $@ -L

all: $(ALL)

%: %.mtx.zip
	unzip -d $* $<

liver-caudate-lobe.mtx.zip:
	$(CURL) "https://data.humancellatlas.org/project-assets/project-matrices/4d6f6c96-2a83-43d8-8fe1-0f53bffd4674.homo_sapiens.mtx.zip"

adult-retina.mtx.zip:
	$(CURL) "https://data.humancellatlas.org/project-assets/project-matrices/8185730f-4113-40d3-9cc3-929271784c2b.homo_sapiens.mtx.zip"

immune-cell-census.mtx.zip:
	$(CURL) "https://data.humancellatlas.org/project-assets/project-matrices/cc95ff89-2e68-4a08-a234-480eca21ce79.homo_sapiens.mtx.zip"

immune-cell-census.loom:
	curl -L "https://data.humancellatlas.org/project-assets/project-matrices/cc95ff89-2e68-4a08-a234-480eca21ce79.homo_sapiens.loom" -o $@

.INTERMEDIATE: $(ALL:=.mtx.zip)
