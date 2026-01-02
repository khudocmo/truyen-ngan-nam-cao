SRCS = $(sort $(wildcard truoc-cach-mang/*.md))
METADATA = metadata.yaml
CSS = minimal.css

BOOK = truoc-cach-mang.epub

CC = pandoc
CFLAGS = --from=markdown --to=epub --toc

all: $(BOOK)

$(BOOK): $(METADATA) $(SRCS) $(CSS)
	$(CC) $(CFLAGS) --output=$(BOOK) $(METADATA) $(SRCS)

.PHONY: clean

clean:
	rm -f $(BOOK)

