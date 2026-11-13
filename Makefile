# The repository's check: lint everything, then run every test.
# pytest exits with status 5 when it collects no tests, which passes.
.PHONY: check
check:
	uv run ruff check
	uv run pytest || [ $$? -eq 5 ]
